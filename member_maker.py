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
