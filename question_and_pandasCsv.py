import pandas as pd

question_src = "question.csv"
df = pd.read_csv(question_src, delimiter=",", encoding='utf-8')


def random_question(df):
    return df.sample(2)


def choice_ans():
    player_input = input("Your answer (A/B/C/D): ").upper()
    while True:
        if player_input in ["A", "B", "C", "D"]:
            return player_input
        else:
            print("retype again")
            continue


question_list = random_question(df)


def game():
    for index, row in question_list.iterrows():
        print(f'cau hoi  {row["Câu hỏi"]}')
        for ans_index in ["A", "B", "C", "D"]:
            print(f'Dáp án {ans_index}: {row[" Lựa chọn " + ans_index]}')
        right_ans=row[" Đáp án"]
        print(right_ans)
        choice = choice_ans()
        choice
        playerans=row[" Lựa chọn "+choice]
        if right_ans==playerans:
            print("chinh xac")
        else:
            print("sai")





game()
