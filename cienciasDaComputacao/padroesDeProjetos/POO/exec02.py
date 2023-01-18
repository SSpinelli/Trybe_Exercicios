import math
import statistics


class Estatistica:
    @classmethod
    def media(cls, list):
        a = 0

        for num in list:
            a += num

        result = a / len(list)

        return result

    @classmethod
    def mediana(cls, list):
        numbers = list.sort()
        if len(numbers) % 2 != 0:
            return numbers[math.floor(len(numbers) / 2)]
        else:
            index = int(len(numbers) / 2)

            calc = (numbers[index] + numbers[index - 1]) / 2
            return calc

    @classmethod
    def moda(cls, list):
        return statistics.mode(list)


print(Estatistica.moda([1, 5, 4, 5, 2]))
