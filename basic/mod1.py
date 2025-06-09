# 확장자 py인 것은 모두 모듈임


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# test 코드 작성 시 아래 if 넣고 쓰면 됨
if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 2))
