class Item:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.weight == other.weight and self.value == other.value

    def __repr__(self):
        return f"Item(W:{self.weight}, V:{self.value})"
    