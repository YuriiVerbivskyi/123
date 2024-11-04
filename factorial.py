class Factorial:
    Cache = {0: 1, 1: 1, 2: 2}

    @staticmethod
    def factorial_calculate(n):
        if n in Factorial.Cache:
            return Factorial.Cache[n]

        result = n * Factorial.factorial_calculate(n-1)

        Factorial.Cache[n] = result

        return result

if __name__ == "__main__":


    number = int(input("Choose a number"))
    print(Factorial.factorial_calculate(number))
