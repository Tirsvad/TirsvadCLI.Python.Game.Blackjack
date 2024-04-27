from random import shuffle


class Cards:
    types = {}
    suits = {}
    deck = {}
    # cards [name, icon, type]
    cards = []

    def __init__(self, types: dict[str, int] = None):
        """
        Prepare deck of a´cards without jokers

        Args:
            types: Card type and it's value.
        Examples: my_cards = Cards({"J": 11, "Q": 12, "K":13, "A": })
        """

        self.types = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }

        if types:
            self.types.update(types)

        self.suits = {
            "heart": {"icon": "\033[91m\u2665\033[0m", "color": "red"},
            "spade": {"icon": "\u2660", "color": "black"},
            "diamond": {"icon": "\033[94m\u2666\033[0m", "color": "blue"},
            "club": {"icon": "\033[92m\u2663\033[0m", "color": "green"},
        }

        for suit in self.suits:
            dct = {}
            dct.update({suit: self.suits[suit]})
            dct[suit].update({"types": self.types})
            self.deck.update(dct)

        self.generate_deck_of_cards()

    def generate_deck_of_cards(self, decks: int = 6):
        """
        Make stack of card of the card deck.
        Default it use 6 deck of cards

        :param decks: Number of decks to use. Default value 6
        :return:
        """
        for _ in range(1, decks):
            for suit in self.deck:
                # for card_type in self.deck[suit]["types"]:
                for card_type in self.deck[suit]["types"]:
                    self.cards.append(
                        [
                            suit,
                            self.deck[suit]["icon"],
                            card_type,
                            self.deck[suit]["types"][card_type],
                        ]
                    )
        shuffle(self.cards)

    def get_numbers_of_cards_in_deck(self):
        return len(self.cards)


class BlackJack:

    def __init__(self):
        self.cards = Cards()

    def deal_card(self):
        card = self.cards.cards.pop()
        return card

    def calculate_score(self, cards: list):
        score = 0
        for index in cards:
            score += index[3]
        if score == 21 and len(cards) == 2:
            return 0
        if score > 21 and self.has_an_ace(cards):
            i = 0
            for index in cards:
                if index[3] == 11:
                    cards[i][3] = 1
                i += 1
        return score

    def compare_score(self, user_score: int, dealer_score: int):
        if user_score == dealer_score:
            return "Draw"
        elif dealer_score == 0:
            return "Lose, opponent has Blackjack"
        elif user_score == 0:
            return "Win with a Blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif dealer_score > 21:
            return "Opponent went over. You win"
        elif user_score > dealer_score:
            return "You win"
        else:
            return "You lose"

    def has_an_ace(self, cards):
        for index in cards:
            if index[2] == 11:
                return True
        return False

    def output_user_card(self, cards):
        output = ""
        for card in cards:
            output += f"{card[1]}{card[2]} "
        return output
