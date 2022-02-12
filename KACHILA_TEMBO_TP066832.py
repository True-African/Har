import pickle
import os
import pathlib
from datetime import date

class Account :
    accNo = 0
    name = ''
    deposit=0
    age = 0
    passwd=''
    accounttype = ['C','S']
    now = date.today()
    
    def createAccount(self):
        def accountNOGenerator():
            value = 18765457648
            return value
        def passwordGenerator():
            password = '1234'
            return password
        self.accNo= accountNOGenerator()
        self.name = input("Enter the account holder name : ")
        self.accounttype = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount: "))
        self.age  = int(input("Enter Age: "))
        self.passwd = passwordGenerator()
        self.now = date.today()
        print("\n\n\nAccount Created")
        print("Default Password: ", self.passwd)
        print("Account No: ", self.accNo)
        print("As of: ",self.now)
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name : ")
        self.type = input("Modify type of Account : ")
        self.deposit = int(input("Modify Balance : "))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit, " ", self.now, "", self.passwd)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tWelcome! Thank you for choosing:")
    print("\t\t\t\t\tKachila Bank")
    input()



def writeAccount():
    account = Account()
    account.createAccount()
    if account.age < 18:
        print("Can't create account at age less than 18. ")
    else:
       
        writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.accounttype, " ",item.deposit," ",item.now)
        infile.close()
    else :
        print("No records to display.")
        

def displaySp(num): 
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search. ")
    if not found :
        print("No existing record with this number. ")

def customerLogin(num1, _password): 
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print (item.accNo)
            print (item.passwd)
            if item.accNo == num1 and item.passwd == _password :
                return True
            else:
                return False
        infile.close()                   
def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.txt')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updated. ")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if item.accounttype == 'C':
                        if amount <= item.deposit and amount > 1000 :
                            item.deposit -=amount
                    elif  item.accounttype == 'S':  
                        if amount <= item.deposit and amount > 500 :
                            item.deposit -=amount 
                    else :
                        print("You cannot withdraw larger amount. ")
                
    else :
        print("No records to Search. ")
    outfile = open('newaccounts.txt','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.txt', 'accounts.txt')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.txt')
        outfile = open('newaccounts.txt','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.txt', 'accounts.txt')

 #modifying customer account      
def modifyAccount(num):
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.txt')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.accounttype = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.txt','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.txt', 'accounts.txt')
   
def loginAdmin():   #this function is used to login an admin (SuperUser) with default password
        f = open("login.txt","r")
        lines=f.readlines()
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        usernameFile=lines[0]
        passwordFile=lines[1]
        usernameFile = usernameFile.rstrip()
        passwordFile = passwordFile.rstrip()
        credentials = [ str(usernameFile), str(passwordFile)]
        if (username== credentials[0] and password==credentials[1]):
            print("Correct user name and password. ")
            return True
        else:
            print("Incorrect username or password. ")
        f.close()  
def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.txt')
    else :
        oldlist = [account]
    outfile = open('newaccounts.txt','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.txt', 'accounts.txt')

#customer change password        
def changePassword(self, _password):
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.txt')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.accounttype = input("Enter the account Type : ")
                item.passwd = input("Enter new password: ")
        
        outfile = open('newaccounts.txt','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.txt','accounts.txt')
    
    
class AccountStaff :
    new_staff = ''
    new_staff_Password = ''
    def createStaff(self):
        self.new_staff = input("Enter new staff name: ")
        self.new_staff_Password = input("Enter the new staff password ")
        print("\n\n\nAccount Created")
        
def writeStaff():
    staff = AccountStaff()
    staff.createStaff()
    writeStaffFile(staff)

#creating new account record 
def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.txt")
    if file.exists ():
        infile = open('accounts.txt','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.txt')
    else :
        oldlist = [account]
    outfile = open('newaccounts.txt','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.txt', 'accounts.txt')
    
#new staff login
def staffLogin(name, _password): 
    file = pathlib.Path("staff.txt")
    if file.exists ():
        infile = open('staff.txt','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            if item.new_staff== name and item.new_staff_Password== _password :
                return True
            else:
                return False
        infile.close()

#adding new staff   
def writeStaffFile(account) : 
    
    file = pathlib.Path("staff.txt")
    if file.exists ():
        infile = open('staff.txt','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('staff.txt')
    else :
        oldlist = [account]
    outfile = open('newstaff.txt','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newstaff.txt', 'staff.txt')

    
    
        
    
    
        
# Start of the program (Main Logic)
ch=True 
num1=0
intro()
adminOption = ''
customerOption = ''
_password= ' '


while ch:
    print("\tMAIN MENU")
    print("Enter Option 1 Register as Customer ")
    print("Enter Option 2 To Login as Customer ")
    print("Enter Option 3 To Login as Admin ")
    print("Enter Option 4 To Login as Staff ")
    ch = str(input("Enter choice: ")) 
    if ch == '1':   
        writeAccount() #function to create new user accounts
    elif ch == '2':
        customerLogin(num1, _password)
        num1 = int(input("\tEnter The account No. : "))
        _password = input("\tEnter password: ")
        print(customerLogin(num1,_password))
        if (customerLogin(num1, _password)==True):
            while (customerOption != '6'):
                print("Enter Option 1 to Deposit Money. ")
                print("Enter Option 2 to Withdraw Money. ")
                print("Enter Option 3 to view Statement of Accounts Report. ")
                print("Enter Option 4 to change password. ")
                print("Enter Option 5 to logout. ")
                customerOption = str(input("Enter option: "))
                if customerOption=='1':
                    num = int(input("\tEnter The account No. : "))
                    depositAndWithdraw(num, 1)
                    exit()
                elif customerOption == '2':
                    num = int(input("\tEnter The account No. : "))
                    depositAndWithdraw(num, 2)
                    exit()
                elif customerOption == '3':
                    displayAll()
                elif customerOption == '4':
                     num = input("Enter new password. ")
                     changePassword(num,_password,newpasswd)
                elif customerOption == '5':
                    print(" \n ")
                    print("Thank you for banking with us. Goodbye!")
                exit()
                    
                    
                    
    elif ch == '3':
        loginAdmin() #login the SuperUser who can create Staff Accounts
        if(loginAdmin()==True):
            while(adminOption != '7'):
                print("\t1. BALANCE ENQUIRY")
                print("\t2. VIEW REPORT ")
                print("\t3. CLOSE AN ACCOUNT")
                print("\t4. MODIFY AN ACCOUNT")
                print("\t5. NEW STAFF ACCOUNT")
                print("\t6. LOGOUT")
                adminOption = str(input("Enter option: "))
                if adminOption == '1':
                    num = int(input("\tEnter The account No. : "))
                    displaySp(num)
                elif adminOption == '2':
                    displayAll()
                elif adminOption == '3':
                    num =int(input("\tEnter The account No. : "))
                    deleteAccount(num)
                elif adminOption == '4':
                    num = int(input("\tEnter The account No. : "))
                    modifyAccount(num)
                elif adminOption == '5':
                    writeStaff()
                elif adminOption == '6':
                    print("\n")
                    print("Thank you for banking with us. Goodbye!")
                exit()
    elif ch == '4':
        name= (input("\tEnter name of staff: "))
        _password = input("\tEnter password: ")
        if staffLogin(name, _password) == True:
            while(adminOption != '6'):
                print("\t1. BALANCE ENQUIRY")
                print("\t2. VIEW REPORT ")
                print("\t3. CLOSE AN ACCOUNT")
                print("\t4. MODIFY AN ACCOUNT")
                print("\t5. EXIT")
                adminOption = str(input("Enter option: "))
                if adminOption == '1':
                    num = int(input("\tEnter The account No. : "))
                    displaySp(num)
                elif adminOption == '2':
                    displayAll()
                elif adminOption == '3':
                    num =int(input("\tEnter The account No. : "))
                    deleteAccount(num)
                elif adminOption == '4':
                    num = int(input("\tEnter The account No. : "))
                    modifyAccount(num)
                elif adminOption == '5':
                    print("\n")
                    print("Thank you for banking with us. Goodbye!")
                exit()
