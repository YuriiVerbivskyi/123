class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def divide(self):
        return self.num_1 / self.num_2

    def add(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2


if __name__ == '__main__':

    num_1 = float(input('Enter first number: '))
    num_2 = float(input('Enter second number: '))

    lalala = input(" 1: multiply\n 2: divide\n 3: add\n 4: subtract\n Choose an operation\n ")

    if lalala == '1':
        print (Calculator(num_1, num_2).multiply())
    elif lalala == '2':
        print (Calculator(num_1, num_2).divide())
    elif lalala == '3':
        print (Calculator(num_1, num_2).add())
    elif lalala == '4':
        print (Calculator(num_1, num_2).subtract())
