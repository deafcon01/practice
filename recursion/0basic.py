def factorial(num: int)-> int:
    if num<2:
        return 1
    factorial = 1
    for i in range(1, num+1):
        factorial*=i
    return factorial

def factorialrec(num: int)-> int:
    if num<2:
        return 1
    factorial = num*factorialrec(num-1)
    return factorial

if __name__ == '__main__':
    print(factorial(100))
    print(factorialrec(100))