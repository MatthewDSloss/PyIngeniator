import pandas as pd
import member_maker
import steel_solver


def main():
    aisc_df = pd.read_excel('__aisc-database-v15__.xlsx', sheet_name='Database v15.0')
    member = member_maker.MemberMaker(aisc_df, 'W12X279', 10)
    calc_tension = steel_solver.TensionMember(member, 250)
    print(calc_tension.check_slenderness())

if __name__ == "__main__":
    main()
