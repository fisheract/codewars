def privet(x):
    if x == 0:
        return
    else:
        print("Hello world!")
        privet(x-1)

privet(10)
# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         for i in range(2, n + 1):
#             fib = fib


# def main():
#     n = int(input())
#     print(fib(n))


# if __name__ == "__main__":
#     main()


# fib1 = 0
# fib2 = 1
# n = int(input("Номер элемента ряда Фибоначчи: "))
# if n == 0:
#     print(fib1)
#     quit()
# if n == 1:
#     print(fib2)
#     quit()
# print(fib1, end=' ')
# print(fib2, end=' ')

# for i in range(2, n+1):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# print()