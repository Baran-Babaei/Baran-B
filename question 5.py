l = input('enter your phrase:').split()
c = max(l,key=len)
print(c)
print(f'length: {len(c)}')