import pandas as pd

class MemberMaker:
    def __init__(self, aisc_dataframe, section_name, length):
        self.aisc_df = aisc_dataframe
        self.section = self.aisc_df.loc[self.aisc_df['AISC_Manual_Label'] == section_name]
        self.section_name = section_name
        self.length = length

    def get_section(self):
        return self.section.iloc[0]["AISC_Manual_Label"]

    def get_weight(self):
        return self.section.iloc[0]["W"]

    def get_area(self):
        return self.section.iloc[0]["A"]

    def get_rz(self):
        rx = self.section.iloc[0]["rx"]
        ry = self.section.iloc[0]["ry"]

        rz = ry

        if rx < ry:
            rz = rx

        return rz
