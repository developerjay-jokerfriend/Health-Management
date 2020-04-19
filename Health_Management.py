# Health Management System v1.0 by JAY AKBARI
# Suggestions & More on GITHUB = https://github.com/developerjay-jokerfriend

# DOCUMENTATION v1.0
 # Supports Register & Login as a client.
 # Make a log of your Food Habbits and Exercise Routines with automatic timestamps.
 # Note down what you eat at what time and what workout you perform at what time.
 # Retrieve whatever you have written in your food log and exercise log anytime.
 # Stores and Retrieves your Food & Exercise logs using file system of your OS.

clients=[]
buffer={}
entry=0
gname=""
def Menu():
    # Main Menu
    print("===================================================\n",
          "****** Health Management System v1.0 by Jay ******\n",
          "==================================================\n",
          "Suggestions & More on developerjay.joker@gmail.com\n",
          "==================================================")
    while(True):
        print(" ==================== MENU ========================\n",
              "Press 1 to Register\n",
              "Press 2 to Log Activity\n",
              "Press 3 to Retrieve Activity\n",
              "Press * to Exit program"
              )
        menu_choice=(input("Enter: "))
        if menu_choice=="*": exit()
        if int(menu_choice)==1: Register()
        elif int(menu_choice)==2: Log_Activity()
        else: Retrieve_Activity()

def Register():
    # User Registration
    print("==== PRESS # anytime to go back to MENU ====")
    print("=====Please Register=====")
    name=input("Enter New Username: ")
    if (name == "#"): Menu()
    pwd=input("Enter New Password: ")
    if(pwd == "#"): Menu()
    clients.insert(0,name.upper())
    clients.insert(1,pwd)
    Update_Clients_File() #Update new client in file
    Retrieve_Clients_File() #Update buffer with latest clients
    print("Welcome,",name.upper(),"!")

def Update_Clients_File():
    # Registered User is add in clients file and total users 'entry' is updated.
    global entry
    entry = entry + 1
    content=""
    e=open("clients.txt","r+")
    if(e.read()==""):pass #if empty file
    else:
        temp0=e.readline() #skipped
        content=e.read() #backup of existing content
        #print(content)
    e.seek(0)
    e.write(str(entry)) #write entry
    e.write("\n")
    e.close()

    g=open("clients.txt","a")
    if content != "":
        g.write(content) #paste backup
    g.close()

    f=open("clients.txt","a")
    f.write(clients[0]) #username
    f.write(" ")
    f.write(clients[1]) #password
    f.write("\n")
    f.close()

def Retrieve_Clients_File():
    #Retrieves Client.txt File Content in a buffer which is a dictionary before program starts.
    global entry
    buffer.clear()
    f=open("clients.txt")
    skip = f.readline() #skip entry line

    for r in range(entry):
        content=f.readline()
        i=0       #get i which is position of space
        for items in content:
            if items ==" ": break
            i=i+1
        temp_name=content[0:i]
        temp_pwd=content[i+1:(len(content)-1)]
        buffer.update({temp_name:temp_pwd})
        buffer.update({temp_name:temp_pwd})


    f.close()

def Fetch_Entry():
    # Global Entry Varaible is updated to value from Clients File Before Program Starts.
    global entry
    # When No Clients.txt File Exist, Create it
    temp=open("clients.txt","a")
    temp.close()
    # Finished Creating

    f=open("clients.txt")
    temp=f.readline()
    if temp =="":
        pass
    else:
        f.seek(0)
        entry_str=f.readline()
        entry=int(entry_str[0:len(entry_str)-1])

    f.close()

def Log_Activity():
    # User Authentication and asks for Food Log or Exercise Log
    print("==== PRESS # anytime to go back to MENU ====")
    print("========== WHAT YOU WANT TO LOG? ===========\n",
          "Press 1 - Food\n","Press 2 - Exercise")
    num=input("Enter: ")
    if(num=="#"): Menu()
    if int(num)==1: Food_Logging()
    else: Exercise_Logging()

def Get_Date():
    # Fetch and return timestamp
    import datetime
    return datetime.datetime.now()

def Food_Logging():
    global gname
    while(True):
        if(Authentication()):break
    filename = gname+"_FOOD.txt"
    f=open(filename,"a")
    str_temp = Get_Date()
    print("============ PRESS # anytime to go back to MENU ============")
    print("================",str_temp,"================")
    uinput=input("Enter Your Food Activity: ")
    if(uinput=="#"): Menu()
    f.write("[")
    f.write(str(str_temp))
    f.write("] : ")
    f.write(uinput)
    f.write("\n")
    f.close()
    print("============== SUCCESSFULLY SAVED ! ==============")

def Exercise_Logging():
    while(True):
        if (Authentication()):break
    filename = gname + "_EXERCISE.txt"
    f = open(filename, "a")

    str_temp = Get_Date()
    print("=================== PRESS # anytime to go back to MENU ==================")
    print("=======================", str_temp, "=======================")
    uinput = input("Enter Your Exercise Activity: ")
    if(uinput=="#"): Menu()

    f.write("[")
    f.write(str(str_temp))
    f.write("] : ")
    f.write(uinput)
    f.write("\n")
    f.close()
    print("============== SUCCESSFULLY SAVED ! ==============")

def Retrieve_Activity():
    # User Authentication and asks for Food or Exercise Retrieval
    print("==== PRESS # anytime to go back to MENU ====")
    print("=== WHAT YOU WANT TO RETRIEVE ? ===\n", "Press 1 - Food\n", "Press 2 - Exercise")
    num = input("Enter: ")
    if num=="#": Menu()
    if int(num) == 1:
        Food_Ret()
    else:
        Exercise_Ret()

def Food_Ret():
    global gname
    while (True):
        if (Authentication()): break
    filename = gname + "_FOOD.txt"
    temp=open(filename,"a") #Create file when file does not exist
    temp.close()

    f = open(filename,"r")
    if (f.read()==""):
        print(" FOOD LOG DOES NOT EXIST.\n",
              "Press 0 to start Log Activity\n",
              "Press # to go back to MENU")
        i= input("Enter: ")
        if i=="0":
            Log_Activity()
            Menu()
        if i=="#": Menu()

    print("**********",gname,"'s FOOD LOG **********")
    f.seek(0)
    print(f.read())
    f.close()
    print("========= FINISHED FOOD RETRIEVAL! ========")

def Exercise_Ret():
    global gname
    while (True):
        if (Authentication()): break

    filename = gname + "_EXERCISE.txt"
    temp=open(filename,"a") #Create file to check emptyness to handle case when file does not exist
    temp.close()
    f = open(filename,"r")

    if (f.read() == ""):  # When file does not exist and hence empty

        print(" EXERCISE LOG DOES NOT EXIST.\n",
              "Press 0 to start Log Activity\n",
              "Press # to go back to MENU")
        i = input("Enter: ")
        if i == "0":
            Log_Activity()
            Menu()
        if i == "#": Menu()

    print("**********",gname,"'s EXERCISE LOG **********")
    f.seek(0)
    print(f.read())
    f.close()
    print("========= FINISHED EXERCISE RETRIEVAL! ========")

def Authentication():
    global gname
    print("==== PRESS # anytime to go back to MENU ====")
    print("=============== Please Login ===============")
    uname=input("Your Username: ")
    if(uname=="#"): Menu()
    uname=uname.upper()
    pwd=input("Password: ")
    if(pwd=="#"): Menu()
    temp=buffer.copy() #make copy of buffer dictionary
    for key in buffer:
        val=temp.pop(key) # get password corresponding to username
        if uname==key and pwd==val:
            gname=key
            print("============================================\n",
                  "Logged In Successfully!\n",
                  "============================================")
            return True
    print("XXX Invalid Username or Password ! XXX")
    return False


Fetch_Entry()
Retrieve_Clients_File()
Menu()

