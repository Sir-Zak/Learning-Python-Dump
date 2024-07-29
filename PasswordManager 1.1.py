#Password Manager
import random
import os
import platform
import pwinput  #module for masking user input | pip install pwinput

#Setup initial password
Password = 'CHANGE ME' #CHANGE ME


#Prime file path and variables
path = os.path.join(os.getcwd(), 'passman.txt')
args = ['1','2','3']
Chars = [
    '1','2','3','4','5','6','7','8','9',
    'A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z','a',
    'b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z','!','@',
    '%','^','&','*','#','(',')','-','_',
    '+','='
         ]




def clear_Screen():
#Detect OS to set up clears to make app cleaner
    if platform.system() == "Windows":
        os.system('cls')
    else:
       os.system('clear')






def create():
#Function that selects a random number between 8-14 and then selects that many characters from the list
#Those characters get added to list 'RawPassword' and then turned into a string on the following line.
#The final lines write the information to the passman file
    print('\nCreate Password\n==================================\n')
    Account = input('Enter account name: ')
    RawPassword = random.choices(Chars, k=random.randint(10,20))
    Password = ''.join(map(str,RawPassword))
    print('\n++PASSWORD GENERATED++\n\n***********************************\nPassword:', Password,'\n***********************************\n')
    with open(path,'a') as f: 
        f.write("Account:"+Account+" | Password:"+Password+"\n")






def retrieve():
#Function that asks for account name and then searches the passman file, returning lines that match. Case insensitive
    print('\nRetrieve Password\n===================================\n')
    search = input('Enter Account Name:').lower()
    print('\n')
    found = False
    with open(path,'r') as f:
        for line in f:
            if search in line.lower():
                print(line.strip(),"\n")
                found = True
    if not found:
        print('\n++Account not found++\n')        
            


def main():            
    Challenge = 0
    Argument = 0

    #Won't let user access the program without entering the password
    while Challenge != Password:
        Challenge = pwinput.pwinput(prompt = 'Enter password: ', mask='*')
    clear_Screen()
    print ('\n***********************\n++--ACCESS GRANTED--++\n***********************\n')

    #Main function(Not a function, but ya know) Basically loops while the user selects any option other than exit. 
    #only accepts 3 options
    while Argument != '3':    
        print('Please select an option:\n===================================\n1:Create New Password\n2:Retrieve Password\n3:Exit')
        Argument = input('\n#')
        if Argument == '1':
            clear_Screen()
            create()
        if Argument == '2':
            clear_Screen()
            retrieve()
        if Argument not in args:
            clear_Screen
            print('\n*********************************\nPlease enter a valid selection\n*********************************\n')
    if Argument == '3':    
        clear_Screen()
        





if __name__ == "__main__":
    main()