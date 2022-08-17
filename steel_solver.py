import pandas as pd
import numpy as np


# class SteelSolver is a superclass under which solvers for different load conditions are stored. The input is a
# member object.
class SteelSolver:
    yield_strength = 50  # ksi
    rupture_strength = 65  # ksi
    yield_resistance_factor = 0.9
    rupture_resistance_factor = 0.75

    def __init__(self, member):
        self.member = member


# class TensionMember contains methods that complete checks on an inputted method based on a given load case
class TensionMember(SteelSolver):
    def __init__(self, member, loading):
        self.loading = loading
        super().__init__(member)

    # check_slenderness() checks member against non-mandatory limit of L/r <= 300
    def check_slenderness(self):
        member = self.member
        length = member.length
        rz = member.get_rz()

        pass_slenderness = True
        if length / rz >= 300:
            pass_slenderness = False

        return pass_slenderness

    # check_gross_yielding() checks member yielding in the gross section phi * P(n) <= F(y) * A(g)
    def check_gross_yielding(self):
        member = self.member
        area = member.get_area()
        nominal_resistance = area * self.yield_strength
        factored_resistance = nominal_resistance * self.yield_resistance_factor
        load_effect = self.loading * area

        pass_gross_yielding = True
        if load_effect > factored_resistance:
            pass_gross_yielding = False

        return pass_gross_yielding

    # check_gross_rupture() checks member rupture in the effective section based of AISC tbl 6-2 assuming Ae = 0.75Ag
    def check_net_rupture(self):
        member = self.member
        net_area = member.get_area() * 0.75  # conservative if Ae > 0.75Ag
        nominal_resistance = net_area * self.rupture_strength
        factored_resistance = nominal_resistance * self.rupture_resistance_factor
        load_effect = self.loading * net_area

        pass_net_rupture = True
        if load_effect > factored_resistance
            pass_net_rupture = False

        return pass_net_rupture
