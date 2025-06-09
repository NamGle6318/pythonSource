class Calc:

    # 연산자 생성자
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    # 사칙연산 함수들
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


if __name__ == "__main__":
    calc = Calc(3, 7)
    print(calc.add())
    print(calc.sub())
    print(calc.multiply())
    print(calc.divide())
