class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def to_dict(self):
        return {"front": self.front, "back": self.back}

    @staticmethod
    def from_dict(data):
        return Card(data["front"], data["back"])


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def to_dict(self):
        return {
            "name": self.name,
            "cards": [card.to_dict() for card in self.cards]
        }

    @staticmethod
    def from_dict(data):
        deck = Deck(data["name"])
        deck.cards = [Card.from_dict(c) for c in data["cards"]]
        return deck
