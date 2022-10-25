def heading():
    print('''
********************************************************************************
                           .__                     ___.                     __     
  ______ __ __ _______ |__| ___.__._____       \_ |__  _____     ____  |  | __ 
 /  ___/|  |  \\_  __ \|  |<   |  |\__  \       | __ \ \__  \   /    \ |  |/ / 
 \___ \ |  |  / |  | \/|  | \___  | / __ \_     | \_\ \ / __ \_|   |  \|    <  
/____  >|____/  |__|   |__| / ____|(____  /     |___  /(____  /|___|  /|__|_ \ 
     \/                     \/          \/          \/      \/      \/      \/ 
                                                                               
*********************************************************************************                                                                               
    
 
                                                                               ''')
heading()

print("would you like to display the balance on the screen\n")
a=(input("enter the YES (or) NO:"))
if a == 'yes':


     number=int(input("insert the card or 16digit number:"))
     count = 0
     while (number > 0):
        number = number // 10
        count = count + 1

     if(count==16):
        number=int(input("enter the 4 digit pin number:",))
        count = 0
        while (number > 0):
                   number = number // 10
                   count = count + 1
        if count != 4:
            print("pls enter u r pin again")
        if count == 4:
                print("choose the account type\n1)credit\n2)current\n3)savings ")
                print("savings type account only available")
        account_type =input ("choose the account type:")
        if account_type == 'savings':
                    print("available balance default Rs 10,000")


                    amount = int(input("please enter the amount:"))
                    b = amount % 100
                    if amount == 0:
                        choice = input("YES (or) NO:")
                        if choice == 'yes':
                            print("your transcation can be proceed")
                            print("would you like to display the balance on the screen\n")
                            visible = input("enter the YES (or) NO:")
                            if visible == 'yes':
                                balanced = int(10000)
                                print("main balance amount is:Rs 10 ,000")
                                total = balanced - amount
                                print("withdraw after balance amount is:", total)
                    else:
                        print("invalid amount selection ATM conatin Rs 100 or Rs 500")
                        exit()


                    choice = input("YES (or) NO:")
                    if choice == 'yes':
                        print("your transcation can be proceed")
                        print("would you like to display the balance on the screen\n")
                        visible = input("enter the YES (or) NO:")
                        if visible == 'yes':
                            balanced = int(10000)
                            print("main balance amount is:Rs 10 ,000")
                            total = balanced - amount
                            print("withdraw after balance amount is:", total)
     elif (count!=16):
         print("16 digit number is error retry again.")

else:
    print("some process wait a minute")                            
