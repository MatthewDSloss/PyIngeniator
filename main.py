import pandas as pd
import member_maker
import steel_solver
import load_maker


def main():
    aisc_df = pd.read_excel('__aisc-database-v15__.xlsx', sheet_name='Database v15.0')
    member_df = member_maker.MemberMaker(aisc_df, 'W12X279', 10)
    member_df.build_connection()

    # while True:
    #     try:
    #         calculation = str(input("Tension/Compression/Flexural/Combined?"))
    #         if calculation == 'Tension' or calculation == 'tension':
    #             tension()
    #         else: raise ValueError
    #         break
    #     except ValueError:
    #         print("Invalid or Unsupported input")


    # member_df = member_maker.MemberMaker(aisc_df, 'W12X279', 10)
    # calc_tension = steel_solver.TensionMember(member_df, 25)
    # print(calc_tension.check_slenderness())
    # print(calc_tension.check_gross_yielding())

def tension():
    length = input("How long is the member being designed?")


if __name__ == "__main__":
    main()
