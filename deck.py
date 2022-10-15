from card import Card


class Deck:
    def __init__(self, name):
        assert type(name) == str, 'Name of deck must be a string!'

        self.__name = name
        self.__deck = []

    def __str__(self):
        """

        Returns string representation of deck

        :param:
            None

        :return:
            deckStr (str): String representation of deck.

        """

        temp = self.__deck.copy()
        temp.reverse()

        result = self.__name + ' [ '
        for card in temp:
            result += str(card) + ' '
        result += ']'
        return result

    def __repr__(self):
        """

        Returns string representation of deck class

        :param:
            None

        :return:
            deckRep (str): String representation of deck class

        """

        temp = self.__deck.copy()
        temp.reverse()

        result = self.__name + ' [ '
        for card in temp:
            result += repr(card) + ' '
        result += ']'
        return result

    def deckName(self):
        """

        Returns name of deck

        :param:
            None

        :return:
            self.__name (str): Name of deck

        """
        return self.__name

    def deckSize(self):
        """

        Returns size of deck

        :Param:
            None

        :return:
            self.__size (int): Size of deck

        """

        return len(self.__deck)

    def isDeckEmpty(self):
        """

        Returns if deck is empty. Empty = True, not empty = False

        :Param:
            None

        :return:
            self.__size <= 0 (bool): If deck is empty

        """

        return len(self.__deck) <= 0

    def pushDeck(self, card):
        """

        Pushes card to top of deck.

        :param:
            card (Card): Card to push to deck
        :return:
            None

        """
        assert type(card) == Card, 'You must push a card from the Card class!'

        self.__deck.append(card)

    def popDeck(self):
        """

        Removes card from top of deck and returns it.

        :Param:
            None

        :return:
            card (Card): Card from top of deck
        """
        if len(self.__deck) <= 0:
            return None
        else:
            return self.__deck.pop(-1)

    def peekDeck(self):
        """

        Returns card from top of deck. Does not makes changes to deck.

        :Param:
            None

        :return:
            card (Card): Card from top of deck
        """

        if len(self.__deck) > 0:
            return self.__deck[-1]
        else:
            return None
