D=int(input('time:'))
if D<0 or D>23:
    print('False')
elif 6<= D <= 12:
    print('morning')
elif 12<= D <14:
    print('afternoon')
elif 14<= D <=19:
    print('evening')
else: print('night')
