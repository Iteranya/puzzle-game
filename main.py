import random
from  models import CardItem

class MemoryGame:
    def __init__(self, pairs):
        self.deck = self.initialize_deck(pairs)
        random.shuffle(self.deck)
        self.first_pick = None

    def initialize_deck(self, pairs):
        """Initialize a deck with pairs of cards based on input"""
        deck = []
        for i in range(pairs):
            deck.append(CardItem(i, f"Card-{i}"))
            deck.append(CardItem(i, f"Card-{i}"))
        return deck

    def reveal_card(self, index):
        """Reveal a card at a given index"""
        if index < 0 or index >= len(self.deck):
            print("Invalid index, try again.")
            return False
        if self.deck[index].revealed:
            print("Card already revealed, choose another one.")
            return False

        self.deck[index].revealed = True
        self.display_deck()
        return True

    def match_cards(self, index1, index2):
        """Check if two cards match"""
        if self.deck[index1].id == self.deck[index2].id:
            print("It's a match!")
        else:
            print("Not a match.")
            self.deck[index1].revealed = False
            self.deck[index2].revealed = False

    def display_deck(self):
        """Print the current state of the deck"""
        for idx, card in enumerate(self.deck):
            if card.revealed:
                print(f"[{card.name}]", end=" ")
            else:
                print("[X]", end=" ")
            if (idx + 1) % 4 == 0:
                print()  # Newline every 4 cards
        print()


def main():
    game = MemoryGame(pairs=8)
    game.display_deck()

    while True:
        idx1 = int(input("Select the first card to reveal (0-15): "))
        if game.reveal_card(idx1):
            idx2 = int(input("Select the second card to reveal (0-15): "))
            if game.reveal_card(idx2):
                game.match_cards(idx1, idx2)
                game.display_deck()


if __name__ == "__main__":
    main()


