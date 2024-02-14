"""
날짜
이름
"""


def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)


def gugudan(x):
    for a in range(1,10):
        print(x*a)