import random

user_score = 0
pc_score = 0
run = True
#step1
options = ['s', 'k', 'q']
    
while run:

    #step2
    print('s:سنگ, k:کاغذ,q:قيچي')
    user_choice = input('please choose one of this things:   \n')

    if user_choice in options:
    #step3
        pc_choice = random.choice(options)
        print(f'pc choice:  {pc_choice}')

#step4
        if user_choice == pc_choice:
            print('mosavi ast,dobare talash konid')
        elif user_choice == 's':  
            if pc_choice == 'k':
                pc_score+=1
            else:
                user_score+=1
        elif user_choice == 'k':
            if pc_choice == 'q':
                    pc_score+=1
            else:
                user_score+=1
        elif user_choice == 'q':
            if pc_choice == 's':
                pc_score+=1
            else:
                user_score+=1


#sharte etmam
    if user_score == 3 or pc_score == 3:
        if user_score==3:
            print('user is the winner')
        else:
            print('computer is the winner')
        run = False
    else:
        print(f'user: {user_score} - pc: {pc_score} => berim daste badi')
else:
        print('ERROR=> lotfan az beine gozineha entekhab konid')
