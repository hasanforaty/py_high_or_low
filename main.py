from art import logo, vs
from random import randint
from game_data import data


def choose_data(previews_data_index: list):
    """select a random data index excluded previews_data_index"""
    index = randint(0, len(data) - 1)
    while index in previews_data_index:
        index = randint(0, len(data) - 1)
    return index


def read_data(index):
    """read data from data and return a summarize string"""
    description = ""
    object = data[index]
    description += object["name"] + " ,"
    description += object["description"] + " ,"
    description += f"from {object['country']}."
    return description


def get_follower(index):
    """get follower of data in Index given"""
    return data[index]["follower_count"]


def calculate_winner(a_index, b_index):
    """calculate which index is winner and return 'A' for a_index and 'B' for b_index"""
    if get_follower(a_index) > get_follower(b_index):
        return "a"
    else:
        return "b"


def game():
    """game logic"""
    preiviues_data_index = []
    score = 0
    a_index = choose_data(preiviues_data_index)
    preiviues_data_index.append(a_index)
    b_index = choose_data(preiviues_data_index)
    preiviues_data_index.append(b_index)
    while True:
        print(logo)
        print(f"your score is {score}")
        print(f"Compare A:{read_data(a_index)}")
        print(vs)
        print(f"Compare B:{read_data(b_index)}")
        correct_answer = calculate_winner(a_index, b_index)
        # print(f"correct answer is {correct_answer}")
        answer = input("How has more follower? 'A' for A and 'B' for B: ").lower()

        if answer == correct_answer:
            print("Correct!")
            print("You win")
            score += 1
            a_index = b_index
            b_index = choose_data(preiviues_data_index)
            preiviues_data_index.append(b_index)
        else:
            print("Wrong!")
            print("You lose")
            print(f'your final score is {score}')
            return


game()
