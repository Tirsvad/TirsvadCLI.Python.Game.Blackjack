from os import system, name

from art import logo
from blackjack import BlackJack


def logo_print():
    # define our clear function
    def clear():
        # for windows
        if name == "nt":
            _ = system("cls")

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    clear()
    print(logo)


def compare(user_score, computer_score):
    """
    Compare score and return a string of game result between user and computer

        Parameters:
            user_score (int): user  cards value
            computer_score(int): computer cards value

        Returns:
            variable (str): game result
    """
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    logo_print()
    blackjack = BlackJack()
    is_game_over = False
    user_cards = []
    computer_cards = []
    user_score = None
    computer_score = None
    for _ in range(2):
        user_cards.append(blackjack.deal_card())
        computer_cards.append(blackjack.deal_card())
    while not is_game_over:
        user_score = blackjack.calculate_score(user_cards)
        # print(user_score)
        computer_score = blackjack.calculate_score(computer_cards)
        print(
            f"Your cards: {blackjack.output_user_card(user_cards)}, current score: {user_score}"
        )
        print(
            f"Computer's first card: {blackjack.output_user_card([computer_cards[0]])}"
        )
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if user_should_deal == "y":
                user_cards.append(blackjack.deal_card())
            else:
                while computer_score != 0 and computer_score < 16:
                    computer_cards.append(blackjack.deal_card())
                    computer_score = blackjack.calculate_score(computer_cards)
                is_game_over = True

    print(
        "\n"
        + blackjack.compare_score(user_score=user_score, dealer_score=computer_score)
    )
    print(f"your hand {blackjack.output_user_card(user_cards)} score {user_score}")
    print(
        f"computer hand {blackjack.output_user_card(computer_cards)}  score {computer_score}"
    )
    if input("\nDo you wish to play again? ").lower() == "y":
        play_game()


play_game()
