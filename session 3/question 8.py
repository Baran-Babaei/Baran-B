a = int(input('Enter balance: '))
b = int(input('Enter withdrawal: '))

if b <= 0:
    print('Invalid amount')

elif a >= b:
    c = a - b
    print('Withdrawal successful.')
    print('Remaining balance:', c)

elif a < b:
    print('Not enough balance.')

