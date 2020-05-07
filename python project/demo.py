from tabulate import tabulate
# Attributes = ["Item Code", "Item", "Quantity", "SUPPLIER/CUSTOMER NAME", "DOCUMENT NO.", "Date", "Remarks"]
# files
file_inward_log="InwardItemLog.txt"
file_outward_log="OutwardItemLog.txt"
file_net_stock="NetStock.txt"
file_inward_stock="InwardItemStock.txt"

#List Buffers
List_ItemCode = []
List_Item = []
List_Quantity = []
List_Date = []
List_Remarks = []
List_Supplier = []
List_Customer = []
List_Document = []
List_TimeStamp = []



def EnterInwardItem():
# Menu to capture Inward Item details
    while (True):
        while (True):
            print("\n    ENTER INWARD ITEM DETAILS : ")
            i = input("    Enter Item Code = ")  # PK
            n = input("    Enter Item Name = ")
            q = input("    Enter Quantity = ")
            sn = input("    Enter Supplier Name = ")
            dn = input("    Enter Document No. = ")
            d = input("    Enter Date dd/mm/yy = ")
            ds = input("    Enter Remarks = ") # Description

            try:
                temp=int(q)
                break
            except:
                print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")

        i=i.upper() #MAKE CODE UPPERCASE
        print(f"\n    INWARD ITEM DETIALS: \n"
              f"    ITEM CODE : {i}\n"
              f"    ITEM NAME : {n}\n"
              f"    QUANTITY : {q}\n"
              f"    SUPPLIER : {sn}\n"
              f"    DOCUMENT NO. : {dn}\n"
              f"    DATE : {d}\n"
              f"    REMARKS : {ds}\n")
        confirm = input("    Press 1 to confirm INWARD entry: ")
        if confirm == "1" : break

    return [i, n, q, d, ds, sn, dn ]  # dont change the list item index order here.

def Get_Date():
# Fetch and return timestamp
    import datetime
    return datetime.datetime.now()

def LogInwardItem(ListOfInputs):
# Inward item User input is logged in the inward log file.
    temp_date = Get_Date()
    f=open(file_inward_log, "a")
    string = f"\n[{temp_date}] ---#--- {ListOfInputs[0]} ---#--- {ListOfInputs[1]} ---#--- {ListOfInputs[2]} ---#--- {ListOfInputs[3]} ---#--- {ListOfInputs[4]} ---#--- {ListOfInputs[5]} ---#--- {ListOfInputs[6]}"
    f.write(string)
    f.close()

def ReadInwardItem():
# Load the list buffers with the fresh data from the Inward Item Stock File.
    global List_ItemCode, List_Item, List_Quantity
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    f=open(file_inward_stock,"r")
    s = f.read()
    if len(s) == 0 : pass # if file is empty
    else: # If file is not Empty
        temp_list1 = s.split("\n") # got all rows in the list.
        for item in temp_list1: # for each row in list
            temp_str = str(item)
            temp_list2 = temp_str.split(" ---#--- ") # got attributes of a row as list

            if temp_list2[0]=="": pass # By pass "" empty item of the list due to \n
            else:
                List_ItemCode.append(temp_list2[0])
                List_Item.append(temp_list2[1])
                List_Quantity.append(temp_list2[2])
    f.close()

def WriteInwardItem():
# Updates the inward stock file using content of List Buffers.
    global List_ItemCode, List_Item, List_Quantity
    f = open(file_inward_stock, "w")
    i=0
    s=""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i=i+1
    f.write(s)
    f.close()

def AddItem(InputList):
# Inward Item is is added into list bufferes  / the inward stock
    global List_ItemCode,List_Item,List_Quantity
    # When item is present in List Buffers/file
    if InputList[0] in List_ItemCode:
        for item in List_ItemCode:
            if item == InputList[0]:
                i=List_ItemCode.index(item) # Find the index (row) of the item in Buffer Lists.
                List_Quantity[i] = int(List_Quantity[i] )+ int(InputList[2]) # Increment Quantity List Buffer When Item Already present

    # When item not in Buffers/file
    else: #Append New Item in the list buffers
        List_ItemCode.append(InputList[0])
        List_Item.append(InputList[1])
        List_Quantity.append(InputList[2])

def InwardItem():
# Capture Inward Item, Log it, Update Inward Stock File, Update with increment in Net Stock File.
    temp1=EnterInwardItem()
    LogInwardItem(temp1)
    # ============Update the Inward Stock file with updates=============
    ReadInwardItem()
    AddItem(temp1)
    WriteInwardItem() # Write down the Inward Stock file with updates.
    #============ Update NetStock with the Inward Item ==================
    ReadNetStock()
    AddItem((temp1))
    WriteNetStock()  # Write down the Net Stock file with updates.

#========================================================================================================

def EnterOutwardItem():
# Menu to capture OUTWARD FILE DETAILS
    while(True):
        while(True):

            print("\n    ENTER OUTWARD ITEM DETAILS : ")
            i = input("    Enter Item Code = ") #PK
            n = input("    Enter Item Name = ")
            q = input("    Enter Quantity = ")
            cn = input("    Enter Customer Name = ")
            dn = input("    Enter Document No. = ")
            d = input("    Enter Date dd/mm/yy = ")
            ds = input("    Enter Remarks = ")
            try:
                temp=int(q)
                break
            except:
                print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")

        i = i.upper()  # MAKE CODE UPPERCASE
        print(f"\n    OUTWARD ITEM DETIALS : \n"
              f"    ITEM CODE : {i}\n"
              f"    ITEM NAME : {n}\n"
              f"    QUANTITY : {q}\n"
              f"    CUSTOMER : {cn}\n"
              f"    DOCUMENT NO. : {dn}\n"
              f"    DATE : {d}\n"
              f"    REMARKS : {ds}\n")
        confirm = input("    Press 1 to confirm OUTWARD entry: ")
        if confirm == "1": break

    return [i, n, q, d, ds, cn, dn] # dont change the list item index order here.

def LogOutwardItem(ListOfInputs):
# Logs outward Entry of user input in the Outward Log File.
    temp_date = Get_Date()
    f = open(file_outward_log, "a")
    string = f"\n[{temp_date}] ---#--- {ListOfInputs[0]} ---#--- {ListOfInputs[1]} ---#--- {ListOfInputs[2]} ---#--- {ListOfInputs[3]} ---#--- {ListOfInputs[4]} ---#--- {ListOfInputs[5]} ---#--- {ListOfInputs[6]}"
    f.write(string)
    f.close()

def ReadNetStock():
# Load the list buffers with the fresh data from the Net Stock File.
    global List_ItemCode, List_Item, List_Quantity
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    f = open(file_net_stock, "r")
    s = f.read()
    if len(s) == 0:
        pass  # if file is empty
    else:  # If file is not Empty
        temp_list1 = s.split("\n")  # got all rows in the list.
        for item in temp_list1:  # for each row in list
            temp_str = str(item)
            temp_list2 = temp_str.split(" ---#--- ")  # got attributes of a row as list

            if temp_list2[0] == "":
                pass  # By pass "" empty item of the list due to \n
            else:
                List_ItemCode.append(temp_list2[0])
                List_Item.append(temp_list2[1])
                List_Quantity.append(temp_list2[2])
    f.close()

def WriteNetStock():
# Updates the Net Stock file from the list buffers.
    global List_ItemCode, List_Item, List_Quantity
    f = open(file_net_stock, "w")
    i = 0
    s = ""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i = i + 1
    f.write(s)
    f.close()


def SubtractItem(InputList):
# Subtracts item entered by user for outward from list buffers / net stock. Returns True if outwarding is feasible.
    global List_ItemCode,List_Item,List_Quantity
    # When Item is present in Net Stock
    if InputList[0] in List_ItemCode:
        for item in List_ItemCode:
            if item == InputList[0]:
                i = List_ItemCode.index(item)  # Find the index (row) of the item in Buffer Lists.
                if (( int(List_Quantity[i]) - int(InputList[2]) ) >= 0 ):
                    # Update Quantity List Buffer When Item Already present
                    List_Quantity[i] = int(List_Quantity[i]) - int(InputList[2])
                    return True
                else:
                    print("\n\n\n    ==========================================================\n"
                          "    INSUFFICIENT ITEMS IN STOCK. PLEASE PLACE AN INWARD ORDER.\n"
                          "    ==========================================================\n\n\n")
                    return False
    else:  # When Item is not present in stock
        print(f"\n\n\n    =================================================================================\n"
              f"    {InputList[1]}-{InputList[0]} : ZERO ITEMS IN STOCK. PLEASE PLACE AN INWARD ORDER.\n"
              f"    ==================================================================================\n\n\n")
        List_ItemCode.append(InputList[0])
        List_Item.append(InputList[1])
        List_Quantity.append("0")  # Make an entry in Net Stock file that item quantity is zero.
        return False

def OutwardItem():
# Outwards an item if possible and makes outward log and updates net stock file.
    temp1 = EnterOutwardItem()
    #==============================
    ReadNetStock()
    if(SubtractItem(temp1)): LogOutwardItem(temp1) # if feasible to outward then only log
    #================================
    WriteNetStock()  # Write down the Net Stock file with updates.
    #=============================


def ReadInwardLog():
    global List_ItemCode, List_Item, List_Quantity, List_Date, List_Remarks, List_TimeStamp, List_Supplier, List_Document
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    List_Date = []
    List_Remarks = []
    List_TimeStamp = []
    List_Supplier = []
    List_Document = []
    f = open(file_inward_log, "r")
    s = f.read()
    if len(s) == 0:
        pass  # if file is empty
    else:  # If file is not Empty
        temp_list1 = s.split("\n")  # got all rows in the list.
        for item in temp_list1:  # for each row in list
            temp_str = str(item)
            temp_list2 = temp_str.split(" ---#--- ")  # got attributes of a row as list

            if temp_list2[0] == "":
                pass  # By pass "" empty item of the list due to \n
            else:
                List_TimeStamp.append(temp_list2[0])
                List_ItemCode.append(temp_list2[1])
                List_Item.append(temp_list2[2])
                List_Quantity.append(temp_list2[3])
                List_Date.append(temp_list2[4])
                List_Remarks.append(temp_list2[5])
                List_Supplier.append(temp_list2[6])
                List_Document.append(temp_list2[7])
    f.close()

def ReadOutwardLog():
    global List_ItemCode, List_Item, List_Quantity, List_Date, List_Remarks, List_TimeStamp, List_Document, List_Customer
    # Clear the list buffers.
    List_TimeStamp = []
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    List_Date = []
    List_Remarks = []
    List_Customer = []
    List_Document = []


    f = open(file_outward_log, "r")
    s = f.read()
    if len(s) == 0:
        pass  # if file is empty
    else:  # If file is not Empty
        temp_list1 = s.split("\n")  # got all rows in the list.
        for item in temp_list1:  # for each row in list
            temp_str = str(item)
            temp_list2 = temp_str.split(" ---#--- ")  # got attributes of a row as list

            if temp_list2[0] == "":
                pass  # By pass "" empty item of the list due to \n
            else:
                List_TimeStamp.append(temp_list2[0])
                List_ItemCode.append(temp_list2[1])
                List_Item.append(temp_list2[2])
                List_Quantity.append(temp_list2[3])
                List_Date.append(temp_list2[4])
                List_Remarks.append(temp_list2[5])
                List_Customer.append(temp_list2[6])
                List_Document.append(temp_list2[7])

    f.close()



def TableOutwardLog():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity, List_Date, List_Remarks, List_Customer, List_Document
    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_ItemCode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  #  For Serial No.
        temp_list.append(List_TimeStamp[i])
        temp_list.append(List_ItemCode[i])
        temp_list.append(List_Item[i])
        temp_list.append(List_Quantity[i])
        temp_list.append(List_Customer[i])
        temp_list.append(List_Document[i])
        temp_list.append(List_Date[i])
        temp_list.append(List_Remarks[i])
        #=======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "OUTWARD-ENTRY-TIME", "I-CODE", "I-NAME", "QTY.","CUSTOMER", "DOC NO.", "OUTWARD-DATE", "REMARKS"]
    print("\n\n\n    *** OUTWARD-LOG TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")


def TableInwardLog():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity, List_Date, List_Remarks, List_Supplier, List_Document
    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_ItemCode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_TimeStamp[i])
        temp_list.append(List_ItemCode[i])
        temp_list.append(List_Item[i])
        temp_list.append(List_Quantity[i])
        temp_list.append(List_Supplier[i])
        temp_list.append(List_Document[i])
        temp_list.append(List_Date[i])
        temp_list.append(List_Remarks[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "INWARD-ENTRY-TIME", "I-CODE", "I-NAME", "QTY.","SUPPLIER", "DOC NO.", "INWARD-DATE", "REMARKS"]
    print("\n\n\n    *** INWARD-LOG TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def TableNetStock():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity
    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_ItemCode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_ItemCode[i])
        temp_list.append(List_Item[i])
        temp_list.append(List_Quantity[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.","ITEM-CODE", "ITEM-NAME", "QTY."]
    print("\n\n\n    *** NET-STOCK TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def TableInwardStock():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity
    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_ItemCode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_ItemCode[i])
        temp_list.append(List_Item[i])
        temp_list.append(List_Quantity[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "ITEM-CODE", "ITEM-NAME", "QTY."]
    print("\n\n\n    *** INWARD-STOCK TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def View(file):

    #============= Fill the required buffers and Tabulate==============================
    if file==file_outward_log:
        ReadOutwardLog()
        TableOutwardLog()

    elif file==file_inward_log:
        ReadInwardLog()
        TableInwardLog()

    elif file==file_net_stock:
        ReadNetStock()
        TableNetStock()

    elif file==file_inward_stock:
        ReadInwardItem()
        TableInwardStock()

    else:
        print("    ERROR MATCHING FILE NAME")
        pass
    #========================================================================






#========================================================================================================
#MENU
def Menu():

    while(True):
        print("\n\n*** DND PLOUGH - AGRICULTURAL SHAFTS AND ACCESSORIES ***\n\n"
              "================== MENU ================\n"
              "    ENTER 1 - INWARD AN ITEM\n"
              "    ENTER 2 - OUTWARD AN ITEM\n\n"
              "    ENTER 3 - VIEW INWARD LOG\n"
              "    ENTER 4 - VIEW OUTWARD LOG\n\n"
              "    ENTER 5 - VIEW INWARD STOCK\n"
              "    ENTER 6 - VIEW NET STOCK\n"
              "    ENTER # - TO EXIT APPLICATION\n\n"
              "========================================\n")
        x=input("    Enter: ")
        if x=="1":
            InwardItem()

        elif x=="2":
            OutwardItem()

        elif x=="3":
            View(file_inward_log)

        elif x=="4":
            View(file_outward_log)

        elif x=="5":
            View(file_inward_stock)

        elif x=="6":
            View(file_net_stock)

        elif x=="#":
            break
        else: print("\n    PLEASE ENTER CORRECT INPUT!\n")


Menu()
