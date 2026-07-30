import winsound
import time
MourseCode = {"A" : ".-" ,
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",  
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--.." '','' '':'' '',
        "0" : "-----",
        "1" : "----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",}
              
Mystr=input('پيام را وارد کنيد=')
Mystr=Mystr.upper()
Mourse=''
for c in Mystr:
    Mourse=Mourse+MourseCode[c]+' '
print(Mourse)
for m in Mourse:
    if m=='.':
        winsound.Beep(800,500)
    elif m=='-':
        winsound.Beep(800,1500)
    else:
        time.sleep(1)
