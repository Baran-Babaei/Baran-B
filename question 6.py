G=int(input('mablagh:'))
if G>1000000:
    print(G-G*0.15)
elif 500000<=G<=1000000:
    print(G-G*0.1)
else: print(G)
