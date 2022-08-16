import pandas as pd
import numpy as np


class SteelSolver:
    def __init__(self, member):
        self.member = member


class TensionMember(SteelSolver):
    def __init__(self, member,loading):
        self.loading = loading
        super().__init__(member)

    def check_slenderness(self):
        member = self.member
        length = member.length
        rz = member.get_rz()

        pass_slenderness = True
        if length / rz >= 300:
            pass_slenderness = False
        return pass_slenderness
