color1 = input('Please enter the color1: ')
color2 = input('Please enter the color2: ')
color3 = input('Please enter the color3: ')

if color1 == color2 and color2 == color3:
    print('The three colors are equal.')
elif color1 == color2 or color1 == color3 or color2 == color3:
    print('The two colors are equal.')
else:
    print('The colors are not the same.')

