

class Numeral:

    representation = {2: "0b", 8: "0", 16: "0x"}
    bases = [base for base in range(2, 11)] + [16]
    allowed = {16: [str(i) for i in range(0, 10)] + ["a", "b", "c", "d", "e", "f"]}
    values = {chr(97+offset): 10+offset for offset in range(0, 26)}
    for key, value in list(values.items()):
        values[value] = key

    def __init__(self, base = 10):
        self.base = base

    def check(self, number):
        if self.base <= 10:
            return all((int(char) < self.base for char in number))
        elif self.base in Numeral.allowed:
            return all((char in Numeral.allowed[self.base] for char in number))


class Number:

    def __init__(self, value = 0, numeral = Numeral(10)):
        if type(numeral) == Numeral:
            self.numeral = numeral
        else:
            self.numeral = Numeral(numeral)

        value = str(value).lower()
        if self.numeral.check(value):
            self.value = value
        else:
            raise ValueError(f"{value} is not a valid value for a numeral system with the base {self.numeral.base}")

    def __str__(self):
        if self.numeral.base in Numeral.representation:
            return f"{Numeral.representation[self.numeral.base]}{self.value}"
        return str(self.value)

    def convert(self, base):
        value = str(self.value)
        decimal = 0
        for index in range(len(value)):
            significance = len(value)-index-1
            decimal += Numeral.values[value[index]] * self.numeral.base**significance if value[index] in Numeral.values else int(value[index]) * self.numeral.base**significance
        highest_significance = 0
        while not (base**(highest_significance+1))//decimal:
            highest_significance += 1
        if not (base**(highest_significance+1))%decimal:
            highest_significance += 1
        value = ""
        for significance in range(highest_significance, -1, -1):
            value_ = str(decimal//(base**significance))
            value += Numeral.values[int(value_)] if int(value_) in Numeral.values else value_
            decimal = decimal%(base**significance)
        return Number(value, base)

if __name__ == "__main__":
    n = Number("428", 10).convert(16).convert(8).convert(2)
    print(n)
