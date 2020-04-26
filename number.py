from numeral import *

class Number:

    def __init__(self, value = 0, numeral = None):
        if not numeral:
            self._numeral == Numeral(10)
        elif type(numeral) == Numeral:
            self._numeral = numeral
        else:
            self._numeral = Numeral(numeral)

        value = str(value).lower()
        if self._numeral.check(value):
            self._value = value
        else:
            raise ValueError(f"{value} is not a valid value for a numeral system with the base {self._numeral._base}")

    def __str__(self):
        if self._numeral._base in Numeral.representation:
            return f"{Numeral.representation[self._numeral._base]}{self._value}"
        return str(self._value)

    def __repr__(self):
        return self.__str__()

    def get_base(self):
        return self._numeral

    def convert(self, base):
        value = str(self._value)
        decimal = 0
        for index in range(len(value)):
            significance = len(value)-index-1
            decimal += Numeral.values[value[index]] * self._numeral._base**significance if value[index] in Numeral.values else int(value[index]) * self._numeral._base**significance
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
