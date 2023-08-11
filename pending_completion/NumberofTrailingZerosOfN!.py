# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

# hint: you're not meant to calculate the factorial. find another way to
# find the number of zeros.

def zeros(n):
    a = []
    for i in range(0, n + 1):
        if i % 5 == 0:
            a.append(i)

    return len(a) - 1

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = 30
    print(zeros(n))

    for i in range(2, n+1):
        print(i, factorial(i))