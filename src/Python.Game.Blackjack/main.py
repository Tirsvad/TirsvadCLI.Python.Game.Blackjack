from art import logo
import random
from os import system, name

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def logo_print():
    # define our clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    print(logo)


def deal_card() -> int:
    """
        Return a random card from the deck

        Return:
            variable (int): random card value from deck
    """
    return random.choice(cards)


def calculate_score(l_cards: list) -> int:
    """
    Return value of cards

        Parameters:
            l_cards (list): List of cards value

        Return:
            sum (int): Sum value of cards
    """
    if sum(l_cards) == 21 and len(l_cards) == 2:
        return 0
    if 11 in cards and sum(l_cards) > 21:
        l_cards.remove(11)
        l_cards.append(1)
    return sum(l_cards)


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
    is_game_over = False
    user_cards = []
    computer_cards = []
    user_score = None
    computer_score = None
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                while computer_score != 0 and computer_score < 16:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                is_game_over = True
    print("\n" + compare(user_score=user_score, computer_score=computer_score))
    print(f"your hand {' '.join(str(user_cards))} score {user_score}")
    print(f"computer hand {' '.join(str(computer_cards))}  score {computer_score}")
    if input("\nDo you wish to play again? ").lower() == "y":
        play_game()


play_game()
