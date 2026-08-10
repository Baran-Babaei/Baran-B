for i in range(5):
    num1 = int(input('enter the first number: '))
    num2 = int(input('enter the second number: '))
    H = input('* + / -: ')

    if H == '*':
        print(num2 * num1)

    elif H == '/':
        print(num1 / num2)

    elif H == '+':
        print(num1 + num2)

    elif H == '-':
        print(num1 - num2)

    else:
        print('It's not true')

