"""
The first thing to note is the use of collections.namedtuple to construct a simple
class to represent individual cards. We use namedtuple to build classes of objects that
are just bundles of attributes with no custom methods, like a database record. In the
example, we use it to provide a nice representation for the cards in the deck.
"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
    >>> deck = FrenchDeck()
    >>> deck[:3]
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


"""
Here is a function that ranks cards by that rule, returning 0 for the 2 of clubs
and 51 for the ace of spades:
"""

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
