class Card:
    def __init__(self, rank, suit):
        assert type(suit) == str, 'Suit must be a string!'
        assert type(rank) == str or type(rank) == int, 'Rank must be a string or int!'

        self.__shortSuit = suit
        self.__rank = rank
        self.__isVisible = False
        self.__rankVal = 0

        self.__suit = ''

        # Set full name of suit
        if self.__shortSuit == 's':
            self.__suit = 'Spades'
        elif self.__shortSuit == 'h':
            self.__suit = 'Hearts'
        elif self.__shortSuit == 'd':
            self.__suit = 'Diamonds'
        else:
            self.__suit = 'Clubs'

        # Set rank value
        if rank.upper() == 'A':
            self.__rankVal = 1
        elif rank.upper() == 'T':
            self.__rankVal = 10
        elif rank.upper() == 'J':
            self.__rankVal = 11
        elif rank.upper() == 'Q':
            self.__rankVal = 12
        elif rank.upper() == 'K':
            self.__rankVal = 13
        else:
            self.__rankVal = int(rank)

    def __str__(self):
        """

        Returns string representation of card

        :param:
            None

        :return:
            cardStr (str): String representation of card.

        """
        visibility = ''
        if self.__isVisible:
            return str(self.__rank) + self.__shortSuit
        else:
            return '??'


    def __repr__(self):
        """

        Returns string representation of card class

        :param:
            None

        :return:
            cardRep (str): String representation of card class

        """

        visibility = ''
        if self.__isVisible:
            visibility = '+'
        else:
            visibility = '-'
        return str(self.__rank) + self.__shortSuit + visibility

    def isVisibleCard(self):
        """

        Returns the visibility of the card. True = is visible, False = not visible

        :param:
            None

        :return:
            self.__isVisible (bool): Visibility of card

        """

        return self.__isVisible

    def setVisibility(self, visibility):
        """

        Sets the visibility of the card. True = is visible, False = not visible

        :param:
            visibility (bool): Visibility of card

        :return:
            None

        """
        assert type(visibility) == bool, 'The param must be a bool!'

        self.__isVisible = visibility

    def cardRank(self):
        """

        Returns name of card rank.

        :param:
            None

        :return:
            self.__rankVal (int): Value of card rank.

        """

        return self.__rankVal

    def cardSuit(self):
        """

        Returns name of card suit.

        :param:
            None

        :return:
            self.__rank (str): Name of card rank.

        """

        return self.__suit
