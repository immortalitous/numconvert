class Numeral:

    representation = {2: "0b", 8: "0", 16: "0x"}
    bases = [base for base in range(2, 11)] + [16]
    allowed = {16: [str(i) for i in range(0, 10)] + ["a", "b", "c", "d", "e", "f"]}
    values = {chr(97+offset): 10+offset for offset in range(0, 26)}
    for key, value in list(values.items()):
        values[value] = key

    def __init__(self, base = 10):
        self._base = base

    def __str__(self):
        return str(self._base)

    def __repr__(self):
        return self.__str__()

    def check(self, number):
        if number[0] == "-":
            number = number[1:]
        if self._base <= 10:
            return all((int(char) < self._base for char in number))
        elif self._base in Numeral.allowed:
            return all((char in Numeral.allowed[self._base] for char in number))
