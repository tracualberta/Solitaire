"""
;==========================================
; Title:  Solitaire: Klondike
; Author: Ethan Trac
; Date:   Nov 19, 2021
;==========================================
"""


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


class Solitaire:
    def __init__(self):
        # Stock decks
        self.stock = Deck('Stock')
        self.discard = Deck('Discard')

        # Suit decks
        self.spades = Deck('Spades')
        self.hearts = Deck('Hearts')
        self.diamonds = Deck('Diamonds')
        self.clubs = Deck('Clubs')

        # Pile decks
        self.pile1 = Deck('PILE-1')
        self.pile2 = Deck('PILE-2')
        self.pile3 = Deck('PILE-3')
        self.pile4 = Deck('PILE-4')
        self.pile5 = Deck('PILE-5')
        self.pile6 = Deck('PILE-6')
        self.pile7 = Deck('PILE-7')

        self.__pileShortHand = {'1': self.pile1.deckName(), '2': self.pile2.deckName(), '3': self.pile3.deckName(),
                                '4': self.pile4.deckName(), '5': self.pile5.deckName(), '6': self.pile6.deckName(),
                                '7': self.pile7.deckName(), 'stock': self.stock.deckName()}

        self.__validMoves = ['1', '2', '3', '4', '5', '6', '7', 'stock', 'suit']

        self.__dictOfDecks = {self.stock.deckName(): self.stock, self.discard.deckName(): self.discard,
                              self.spades.deckName(): self.spades, self.hearts.deckName(): self.hearts,
                              self.diamonds.deckName(): self.diamonds, self.clubs.deckName(): self.clubs,
                              self.pile1.deckName(): self.pile1, self.pile2.deckName(): self.pile2,
                              self.pile3.deckName(): self.pile3, self.pile4.deckName(): self.pile4,
                              self.pile5.deckName(): self.pile5, self.pile6.deckName(): self.pile6,
                              self.pile7.deckName(): self.pile7}

        self.__commands = ['discard', 'reset', 'board', 'cheat', 'comment', 'move']

    # Interface
    def saveGame(self, fileName):
        """

        Creates new save file based on the current state of the game

        :param:
            gameName (str): Name of file user wishes to create

        :return:
            None

        """
        try:
            assert fileName.endswith('.txt'), 'File must end with .txt!'
            newGame = open(fileName, 'x')
        except AssertionError:
            print('Invalid file name. File must end with .txt')
        # Overwrite file if file already exists
        except FileExistsError:
            newGame = open(fileName, 'w')
            # Go through all the decks in the game
            for deck in self.__dictOfDecks:
                newGame.write(repr(self.__dictOfDecks[deck]) + '\n')
            newGame.close()

        # Create new game file
        else:
            newGame = open(fileName, 'x')
            # Go through all the decks in the game
            for deck in self.__dictOfDecks:
                newGame.write(repr(self.__dictOfDecks[deck]) + '\n')
            newGame.close()

    def loadGame(self, fileName):
        """

        Loads game file.

        :param:
            gameName (str): Name of file user wishes to load

        :return:
            None

        """
        try:
            loadedGame = open(fileName, 'r')

            for line in loadedGame:
                # Get name of deck from line
                deckName = line[:line.index(' [')]

                # Get list of cards in string form
                cardLine = line[line.index('[ '):line.index(' ]')].strip('[ ')
                # print(cardLine)

                # Convert string list into real list
                cardList = cardLine.split(' ')
                cardList.reverse()

                for card in cardList:
                    rank = card[0:1]
                    suit = card[1:2]
                    visibility = card[2:]

                    # Create card to insert into deck
                    if card != '':
                        insertCard = Card(rank, suit)
                        # Set visibility of card
                        if visibility == '+':
                            insertCard.setVisibility(True)
                        else:
                            insertCard.setVisibility(False)
                        self.__dictOfDecks[deckName].pushDeck(insertCard)
        except OSError:
            print('%s cannot be opened: file was not found!' % fileName)
            return Exception
        except ValueError:
            print('File in incorrect save format!')
        loadedGame.close()

    def displayBoard(self):
        """

        Prints representation of game

        :param:
            None

        :return:
            None

        """
        print('\n# Board #\n---------')
        for deck in self.__dictOfDecks:
            print(str(self.__dictOfDecks[deck]))
        print()

    def debug(self):
        """

        Prints board with all cards visible

        :param:
            None
        :return:
            None

        """
        print('\n*** DEBUG ***\n')
        for deck in self.__dictOfDecks:
            print(repr(self.__dictOfDecks[deck]))

    # Game mechanic functions
    def runGame(self, move):
        """

        This function is in charge of managing the functions that are called based on the user input.

        :param:
            move (str): Move input from user

        :return:
            None

        """
        if move == 'done':
            return True

        # Create list from elements in list
        move = move.split(' ')

        # Run correct function based on input
        if move[0] == 'cheat':
            try:
                assert len(move) == 1
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                # Print all cards facing up
                self.debug()
        elif move[0] == 'comment':
            print('Executing:', move)
            move.remove(move[0])
            # Print comment
            print(' '.join(move))
        elif move[0] == 'move':
            print('Executing:', move)

            # Assert that the correct params are being entered for the command
            try:
                assert len(move) == 3, 'Invalid number of arguments for "move"'
                assert move[1] in self.__validMoves, "Deck(s) do not exist!"
                assert move[2] in self.__validMoves, "Deck(s) do not exist!"
                assert move[1] != 'suit', 'Cannot move a card out of a suit deck!'
            except AssertionError as e:
                print(e)
            else:
                # Separate command into two functions, to suit and to pile
                if move[2] == 'suit':
                    self.toSuit(self.__pileShortHand[move[1]])
                else:
                    self.toPile(self.__pileShortHand[move[1]], self.__pileShortHand[move[2]])
        elif move[0] == 'board':
            try:
                assert len(move) == 1
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                self.displayBoard()
        elif move[0] == 'discard':
            try:
                assert len(move) == 1
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                self.discardFunction()
        elif move[0] == 'reset':
            try:
                assert len(move) == 1
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                self.reset()
        elif move[0] == 'load':
            try:
                assert len(move) == 2
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                self.loadGame(move[1])
        elif move[0] == 'save':
            try:
                assert len(move) == 2
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                self.saveGame(move[1])
        elif move[0] == 'menu':
            try:
                assert len(move) == 1
            except AssertionError:
                print('Invalid number of arguments for', move[0])
            else:
                print('Executing:', move)
                inp = input('\nYour game will not auto save if you exit to menu. Do you still wish to exit to menu? (y/n): ')
                while inp != 'y' and inp != 'n':
                    inp = input('Invalid input. Please type "y" or "n": ')
                if inp == 'y':
                    print()
                    main()
                else:
                    print('menu was not executed')
        else:
            print('Not a valid command. Try again!')

    def toSuit(self, fromDeckName):
        """

        Moves card from a deck to a suit. This function automatically recognizes what cards are valid to be moved.

        :param:
            fromDeckName (str): Name of deck user wishes to move card from.

        :return:
            None

        """
        try:
            # Assert that the from deck is not empty
            assert self.__dictOfDecks[fromDeckName].peekDeck() != None
        except AssertionError:
            print('No card in from deck!')
        else:
            # Get from deck
            fromDeck = self.__dictOfDecks[fromDeckName]
            card = fromDeck.peekDeck()
            suitDeckVal = 0

            # If suit deck is not empty, set suitDeckValue to the value of the card on the top
            # The value will be 0 if the deck is empty
            if self.__dictOfDecks[card.cardSuit()].deckSize() != 0:
                suitDeckVal = self.__dictOfDecks[card.cardSuit()].peekDeck().cardRank()

            # Check to see if the card user wants to move is one value larger than the card on the suit deck
            if suitDeckVal + 1 == card.cardRank():
                self.__dictOfDecks[card.cardSuit()].pushDeck(fromDeck.popDeck())
                if fromDeck.peekDeck() != None:
                    fromDeck.peekDeck().setVisibility(True)
            # Print error if the move is not valid
            else:
                print('Not a valid move!')

    def toPile(self, fromDeckName, toDeckName):
        """

        Moves card(s) from a deck to a deck. This function automatically recognizes what cards are valid to be moved.

        :param:
            fromDeckName (str): Name of deck user wishes to move card(s) from.
            toDeckName (str): Name of deck user wishes to move card(s) to.

        :return:
            None

        """
        try:
            assert self.__dictOfDecks[fromDeckName].peekDeck() != None, 'No card in from deck!'
        except AssertionError as e:
            print(e)
        else:
            # Get from deck and to deck
            fromDeck = self.__dictOfDecks[fromDeckName]
            toDeck = self.__dictOfDecks[toDeckName]

            toDeckRank = 0
            # If suit deck is not empty, set toDeckVal to the value of the card on the top
            # The value will be 0 if the deck is empty
            if toDeck.peekDeck() is not None:
                toDeckRank = toDeck.peekDeck().cardRank()

            # Get cards that are visible
            cards = []
            if fromDeck.deckSize() > 0:
                temp = fromDeck.peekDeck()
                while temp != None and temp.isVisibleCard() == True:
                    cards.append(fromDeck.popDeck())
                    temp = fromDeck.peekDeck()

            # Reverse cards list so when you run it through a for loop it pushes in the correct order
            cards.reverse()

            newCards = []
            for card in cards:
                if card.cardRank() < toDeckRank or (cards[0].cardRank() == 13 and toDeck.deckSize() == 0):
                    newCards.append(card)
                else:
                    fromDeck.pushDeck(card)

            # Check if the largest value in the cards list is one less than the card on the top of the toDeck or
            # If the toDeck is empty and the largest value in cards is equivalent to a king
            if toDeckRank - 1 == newCards[0].cardRank() or (newCards[0].cardRank() == 13 and toDeck.deckSize() == 0):
                # Push cards to toDeck
                for card in newCards:
                    toDeck.pushDeck(card)

                # Set top card visible on toDeck
                if fromDeck.peekDeck() != None:
                    fromDeck.peekDeck().setVisibility(True)
            else:
                print('Not a valid move!')
                # Put cards back into the toDeck if the move is invalid
                for card in cards:
                    fromDeck.pushDeck(card)

    def discardFunction(self):
        """

        Takes cards from stock and puts them into discard. It will discard 3 cards if there is enough in the deck.
        Otherwise, it will discard the remaining amount in the stock.

        :param:
            None

        :return:
            None

        """
        try:
            # Assert stock is not empty
            assert self.stock.deckSize() > 0
        except AssertionError:
            print('Cannot discard, stock is empty!')
        else:
            # Discard 3 if stock has more than 3 cards
            if self.stock.deckSize() >= 3:
                for i in range(3):
                    self.discard.pushDeck(self.stock.popDeck())
                    self.discard.peekDeck().setVisibility(False)
            # Discard 2 if stock has 2 cards
            elif self.stock.deckSize() == 2:
                for i in range(2):
                    self.discard.pushDeck(self.stock.popDeck())
            # Discard 1 if stock has 1 card
            else:
                self.discard.pushDeck(self.stock.popDeck())
                self.discard.peekDeck().setVisibility(False)

            # Set new top of stock deck visible if the stock deck isn't empty already
            if self.stock.peekDeck() != None:
                self.stock.peekDeck().setVisibility(True)

    def reset(self):
        """

        Puts all the cards from discard back into stock if the stock deck is empty.

        :param:
            None

        :return:
            None

        """
        try:
            # Assert that the stock deck is empty
            assert self.stock.deckSize() == 0
        except AssertionError:
            print('Stock must be empty!')
        else:
            # Put all the cards from discard into a temp list
            temp = []
            for i in range(self.discard.deckSize()):
                temp.append(self.discard.popDeck())

            temp.reverse()

            # Push all cards back into the stock
            for card in temp:
                self.stock.pushDeck(card)

        # Set top of stock deck visible
        if self.stock.peekDeck() != None:
            self.stock.peekDeck().setVisibility(True)


def inputGame():
    print('Welcome to Klondike!')
    game = Solitaire()

    stop = False
    while not stop:
        # Get input
        move = input('Your move: ')

        if game.runGame(move) == True:
            stop = True
    print('Thank you for playing!')


def testGame():
    print('Welcome to Klondike!')
    file = open('samplegame.txt', 'r')

    game = Solitaire()

    stop = False
    while not stop:
        for line in file:
            move = line.strip('\n')

            if game.runGame(move) == True:
                stop = True
    game.saveGame('hello.txt')
    print('Thank you for playing!')

    main()


def main():
    print('# Main Menu #')
    print('1. Input Game')
    print('2. Sample Game')
    print('3. Exit')

    mode = input('Please select an option using the numbers: ')

    while mode != '1' and mode != '2' and mode != '3':
        print('Input must be a number from the options!')
        mode = input('Please select a game mode: ')
    if mode == '1':
        print()
        inputGame()
    if mode == '2':
        print()
        testGame()
    if mode == '3':
        print('\nGoodbye!')


if __name__ == '__main__':
    main()
