username='abc'
password = 'abc123'

for i in range (2,-1,-1):
   
   u = input('enter username: ')
   p = input('enter password: ')
   
   if u == username and p == password:
       print('login successful')
       break
   else:     
       print(f'wrong username or password \n Attempts remaining:{i}')
       
       if i == 0:
       
           print('your card has been locked!')