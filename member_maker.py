import pandas as pd


# Class MemberMaker is responsible for creating member objects based off AISC tables and fetching data
class MemberMaker:
    def __init__(self, aisc_dataframe, section_name, length):
        self.aisc_df = aisc_dataframe
        self.section = self.aisc_df.loc[self.aisc_df['AISC_Manual_Label'] == section_name]
        self.section_name = section_name
        self.length = length

    # get_section() returns the section name
    def get_section(self):
        return self.section.iloc[0]["AISC_Manual_Label"]

    # get_weight() returns the weight of the section in plf
    def get_weight(self):
        return self.section.iloc[0]["W"]

    # get_area() returns the gross area of the section in in.^2
    def get_area(self):
        return self.section.iloc[0]["A"]

    # get_area() returns the least radius of gyration, rz, in in.
    def get_rz(self):
        rx = self.section.iloc[0]["rx"]
        ry = self.section.iloc[0]["ry"]

        rz = ry

        if rx < ry:
            rz = rx

        return rz

    # builds a list of bolt-holes for use in area calculations
    def build_connection(self):
        location_x = []
        location_y = []
        diameter = []

        # get the vertical location of the first hole
        while True:
            try:
                in_loc = float(input("Enter the distance from the top of member of the uppermost innermost bolt-hole: "))
                location_y.append(in_loc)
                break
            except ValueError:
                print("Invalid input (MUST BE TYPE FLOAT)")

        # first hole marks x-origin
        location_x.append(0.0)

        # get the diameter of the first hole
        while True:
            try:
                in_dia = float(input("Enter the diameter of the first hole: "))
                diameter.append(in_dia)
                break
            except ValueError:
                print("Invalid input (MUST BE TYPE FLOAT)")

        # determine if further holes will be added
        further_holes = True
        while further_holes:
            while True:
                try:
                    in_further = input("More bolt-holes? y/n: ")
                    if in_further == 'y' or in_further == 'Y':
                        break
                    elif in_further == 'n' or in_further == 'N':
                        further_holes = False
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input (MUST BE y/n")
            if further_holes:
                print("Coordinates relative to first bolt-hole\n+--> x\n|\nV y")
                while True:
                    try:
                        in_loc = float(input("Enter the y coordinate of the next bolt hole: "))
                        location_y.append(in_loc)
                        break
                    except ValueError:
                        print("Invalid input (MUST BE TYPE FLOAT)")
                while True:
                    try:
                        in_loc = float(input("Enter the x coordinate of the next bolt hole: "))
                        location_x.append(in_loc)
                        break
                    except ValueError:
                        print("Invalid input (MUST BE TYPE FLOAT)")
                while True:
                    try:
                        in_dia = float(input("Enter the diameter of the next bolt hole: "))
                        diameter.append(in_dia)
                        break
                    except ValueError:
                        print("Invalid input (MUST BE TYPE FLOAT)")
        print("Inputted bolt holes:")
        print("#    x      y      dia")
        i = 0
        while i < len(diameter):
            print(str(i)+"    "+str(location_x[i])+"    "+str(location_y[i])+"    "+str(diameter[i]))
            i += 1
        # TODO: rewrite as pandas db
        # TODO: enable editing of entries

    # def get_effective_area(self):
    #     shear_lag_factor = input('Enter the appropriate shear lag factor per Table D3.1: ')
    #
