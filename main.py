from random import choice

from art import logo

goal = 21
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

decks = {
    "user_cards": [],
    "computer_cards": []
}


def deal_card() -> int:
    return choice(cards)


def add_card(target: str):
    decks[target].append(deal_card())


def init_cards():
    for i in range(1, 3):
        decks["user_cards"].append(deal_card())
        decks["computer_cards"].append(deal_card())


def blackjack():
    init_cards()
    getting_cards = True
    while True:
        computer_score = sum(decks['computer_cards'])
        user_score = sum(decks['user_cards'])

        if 11 in decks['user_cards'] and user_score > goal:
            user_score -= 11
            user_score += 1

        if 11 in decks['computer_cards'] and computer_score > goal:
            computer_score -= 11
            computer_score += 1

        if user_score > goal:
            print('win computer')
            break

        print(logo)
        print(f""" Your cards: {decks['user_cards']}, current score: {user_score} 
 Computer's first card: {decks['computer_cards'][0]}
        """)

        if getting_cards:
            get_card = input("""Type 'y' to get another card, type 'n' to pass:
            """)

        if get_card == 'y':
            add_card('user_cards')
            continue
        else:
            getting_cards = False

        if computer_score == goal:
            print('win blackjack computer')
            break
        elif user_score == goal:
            print('win blackjack user')
            break

        if computer_score < 16:
            add_card('computer_cards')
            continue

        user_score_goal = goal - user_score
        computer_score_goal = goal - computer_score

        if user_score_goal > computer_score_goal:
            print('computer wins')
            print(f"""
                       user_score_goal: {user_score_goal}
                       computer_score_goal: {computer_score_goal}
                   """)
            break
        else:
            print('user wins')
            print(f"""
                       user_score_goal: {user_score_goal}
                       computer_score_goal: {computer_score_goal}
                   """)
            break


if __name__ == '__main__':
    blackjack()
