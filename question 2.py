r = list((input('enter a word: ')))

for i in r[:]:
    if r.count(i)>1:
        index = r.index(i)
        second= r.index(i,index+1)
        
        r.pop(second)

print(''.join(r))
