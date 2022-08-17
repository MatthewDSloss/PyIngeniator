import pandas as pd
import member_maker
import steel_solver


def main():
    aisc_df = pd.read_excel('__aisc-database-v15__.xlsx', sheet_name='Database v15.0')
    member = member_maker.MemberMaker(aisc_df, 'W12X279', 10)
    calc_tension = steel_solver.TensionMember(member, 25)
    print(calc_tension.check_slenderness())
    print(calc_tension.check_gross_yielding())


if __name__ == "__main__":
    main()
