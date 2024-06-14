#Create account
def ca():

    a=input("Do you want to create a bank account in Bank-O-ank? \n Enter Y to continue: ")
    if a.upper()=="Y":
        name=input("Enter your name: ")
        if name.isalpha()==True:
            uid=int(input("Enter a 9 digit customer id for yourself: "))
            if len(str(uid))==9:
                b=input("Enter 'S' for savings and 'C' for current account")
                if b.upper()=="S":
                    c=input("Create SAVINGS account? Enter 'Y' to continue or enter any other key to cancel ")
                    sa="SAVINGS"
                    if c.upper()=="Y":
                        bal=float(input("Enter amount to deposit: "))
                        if bal>0:
                            e=input("If you sure about the amount, enter 'Y' ")
                            if e.upper()=="Y":
                                cursor.execute("insert into customers(id,name,bal,type) values(%s,%s,%s,%s)",(uid,name,bal,sa))
                                db.commit()
                            else:
                                print("Mission failed successfully!") 
                        else:
                            print("You've entered invalid balance")
                    else:
                        print("Cancelled...")
                elif b.upper()=="C":
                    c=input("Create CURRENT account? Enter 'Y' to continue or enter any other key to cancel ")
                    cu="CURRENT"
                    if c.upper()=="Y":
                        bal=float(input("Enter amount to deposit (minimum = 8000.00): "))
                        if bal>8000.00:
                            e=input("If you sure about the amount, enter 'Y' ")
                            if e.upper()=="Y":
                                cursor.execute("insert into customers(id,name,bal,type) values(%s,%s,%s,%s)",(uid,name,bal,cu))
                                db.commit()
                            else:
                                print("Mission failed successfully!") 
                        else:
                            print("You've entered invalid input")
                    else:
                        print("Cancelled...")
                else:
                    print("Great job, command cancelled successfully")
            else:
                print("Invalid customer id format")
        else:
            print("Name can't have nothing but alphabets")
    else:
        ca()        


#Withdraw amount
def wd():

    a=input("Do you want to withdraw money from your account?\nEnter Y to continue: ")
    if a.upper()=="Y":
        