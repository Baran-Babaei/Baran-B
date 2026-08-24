B = input('Enter your password : ')
if len(B) == 8 and B[0:4].isalpha() and B[5:8].isdigit():
    print('Valid')
else:
    print('Invalid')