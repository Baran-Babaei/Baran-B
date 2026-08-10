rekord=0
tekrari=0
while tekrari < 10:
    tekrari+=1
    sabt=int(input("latfan ertefae paresh ra sabt konid:"))
    if sabt > rekord:
        rekord = sabt
        print('rekorde jadid sabt shod:',rekord)
    else:
        print("in rekord ghablan sabt shodeh ast.")


