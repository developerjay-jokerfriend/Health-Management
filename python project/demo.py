from tabulate import tabulate
# Attributes = ["Item Code", "Item", "Quantity", "SUPPLIER/CUSTOMER NAME", "DOCUMENT NO.", "Date", "Remarks"]
# files
file_inward_log="InwardItemLog.txt"
file_outward_log="OutwardItemLog.txt"
file_net_stock="NetStock.txt"
file_inward_stock="InwardItemStock.txt"
file_CAS_stock="CASItemStock.txt"
file_CAS_log="CASItemLog.txt"

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
#=========== CAS LIST BUFFERS ====================
List_CAS_ItemCode = []
List_CAS_Item =  []
List_CAS_Quantity = []

def CreateFileIfNotExist(file):
    f= open(file,"a")
    f.close()

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

    CreateFileIfNotExist(file_inward_stock)
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
    CreateFileIfNotExist(file_inward_stock)
    f = open(file_inward_stock, "w")
    i=0
    s=""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i=i+1
    f.write(s)
    f.close()

def AddItem(InputList):
# Inward Item is is added into list bufferes  / the inward stock / CAS STOCK which ever party calls...
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
        print(f"\n    OUTWARD ITEM DETAILS : \n"
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

    CreateFileIfNotExist(file_net_stock)
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
    CreateFileIfNotExist(file_net_stock)
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

    CreateFileIfNotExist(file_inward_log)
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

    CreateFileIfNotExist(file_outward_log)
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
    global List_ItemCode, List_Item, List_Quantity
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

    headers = ["SR NO.","I-CODE", "I-NAME", "QTY."]
    print("\n\n\n    *** NET-STOCK TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def TableInwardStock():
    global  List_ItemCode, List_Item, List_Quantity
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

    headers = ["SR NO.", "I-CODE", "I-NAME", "QTY."]
    print("\n\n\n    *** INWARD-STOCK TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def TableCASStock():
    global List_ItemCode, List_Item, List_Quantity
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

    headers = ["SR NO.", "I-CODE", "I-NAME", "QTY."]
    print("\n\n\n    *** (CAS) COMPLETE ASSEMBLED SHAFTS - STOCK TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")

def ReadCASLog():
    global List_ItemCode, List_Item, List_Quantity, List_TimeStamp
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    List_TimeStamp = []

    CreateFileIfNotExist(file_CAS_log)
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
    f.close()


def TableCASLog():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity
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
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "CAS-ENTRY-TIME", "I-CODE", "I-NAME", "QTY."]
    print("\n\n\n    *** (CAS) COMPLETE ASSEMBLED SHAFTS - LOG TABLE ***")
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

    elif file==file_CAS_stock:
        ReadCAS()
        TableCASStock()

    elif file==file_CAS_log:
        ReadCASLog()
        TableCASLog()

    else:
        print("    ERROR MATCHING FILE NAME")
        pass
    #========================================================================
#========================================== CAS =========================================================

def EnterCAS():
    # Menu to capture CAS Item details
    while (True):
        while (True):
            print("\n    ENTER COMPLETE ASSEMBLED SHAFTS (CAS) DETAIL : ")
            i = input("    Enter CAS Product Code = ")  # PK
            n = input("    Enter CAS Product Name = ")
            q = input("    Enter Quantity = ")
            try:
                temp = int(q)
                break
            except:
                print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")

        i = i.upper()  # MAKE CODE UPPERCASE
        print(f"\n    COMPLETE ASSEMBLED SHAFTS (CAS) DETAIL: \n"
              f"    CAS PRODUCT CODE : {i}\n"
              f"    CAS PRODUCT NAME : {n}\n"
              f"    QUANTITY : {q}\n"
              )
        confirm = input("    Press 1 to confirm CAS entry: ")
        if confirm == "1": break

    return [i, n, q]  # dont change the list item index order here.

def Read_CAS_SubASSEMBLIES(ListOfCASInputs):
    global List_CAS_Item, List_CAS_ItemCode, List_CAS_Quantity
    # CLear the CAS LIST Buffers
    List_CAS_ItemCode = []
    List_CAS_Item = []
    List_CAS_Quantity = []

    # Open the Item-Code File to load the subassemblies in CAS List Buffers
    CreateFileIfNotExist(f"{ListOfCASInputs[0]}.txt")
    f = open(f"{ListOfCASInputs[0]}.txt", "r")

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
                List_CAS_ItemCode.append(temp_list2[0])
                List_CAS_Item.append(temp_list2[1])
                List_CAS_Quantity.append(temp_list2[2])
    f.close()


def TableMissingItems(temp_icode, temp_iname, temp_iquantity, ListOfCASInputs):

    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(temp_icode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(temp_icode[i])
        temp_list.append(temp_iname[i])
        temp_list.append(temp_iquantity[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.","I-CODE", "I-NAME", "QTY."]
    print(f"\n\n\n    *** >>> {ListOfCASInputs[1]} - {ListOfCASInputs[0]} <<< MISSING SUB ASSEMBLIES TABLE ***")
    print("\n\n", tabulate(mydata, headers=headers), "\n\n")




def CAS_Subtract(ListOfCASInputs):
    global List_ItemCode, List_Item, List_Quantity, List_CAS_Item, List_CAS_ItemCode, List_CAS_Quantity
    temp_icode = []
    temp_iname = []
    temp_iquantity = []
    Read_CAS_SubASSEMBLIES(ListOfCASInputs) # CAS LIST BUFFERS ARE FILLED WITH SUBASSEMBLY DATA
    ReadNetStock()

    # MATCH for each item in CAS BUFFERS is == NET STOCK BUFFERS.
    # >>> MEANS ALL SUBASSEMBLIES ARE PRESENT IN STOCK.
    #        IF SO THEN SUBTRACT QUANTITY OF ALL SUB ASSEMBLIES FROM  RESPECTIVE NET STOCK ITEMS
    #           THEN WRITE THE UPDATED NET STOCK
    # IF SOME SUBASSEMBLY ITEM ABSENT
    #       THEN DONT WRITE NET STOCK
    #       PRINT INSUFFIENT ITEMS AND WHICH ARE INSUFFCIENT ITEMS.

    MISSING = 0
    for c_item in List_CAS_ItemCode:
        flg = 0  # Item no present
        for n_item in List_ItemCode:
            # EACH SUB_ASSEMBLY ITEM IS SEARCHED IN NETSTOCK BY MATCHING ITEM CODE WITH EACH ITEM IN NETSTOCK.
            if c_item == n_item:
                # SUBTRACT THAT ITEM QUANTITY FROM NETSTOCK
                i1 = List_CAS_ItemCode.index(c_item)
                i2 = List_ItemCode.index(n_item)
                List_Quantity[i2] = int(List_Quantity[i2]) - int(List_CAS_Quantity[i1])
                flg=1
                break

        #INNER FOR LOOP ENDS HERE
        if flg == 0:
            # SPECIFIC C_ITEM NOT PRESENT IN NETSTOCK
            i=List_CAS_ItemCode.index(c_item) # Get index of missing item
            # FIll THE TEMP BUFFERS WITH MISSING ITEM DETAILS:
            temp_icode.append(List_CAS_ItemCode[i])
            temp_iname.append(List_CAS_Item[i])
            temp_iquantity.append(List_CAS_Quantity[i])
            MISSING = 1

    # OUTER FOR LOOP ENDS HERE
    if MISSING == 1:
        print(f"\n\n\n==========================================================================\n"
              f"INSUFFICIENT SUB-ASSEMBLIES IN NET-STOCK WHILE ENTERING"
              f" {ListOfCASInputs[1]} - {ListOfCASInputs[0]} IN CAS!\n"
              f"==========================================================================\n")
        TableMissingItems(temp_icode, temp_iname, temp_iquantity, ListOfCASInputs)
        return False
    # IF CONTROL REACHES HERE
    # MEANS ALL SUB ASSEMBLIES ARE PRESENT AND NET STOCK QUANTITY MUST BE WRITTEN WITH UPDATED LIST BUFFERS.
    WriteNetStock()
    return True


def ReadCAS():
    # Load the list buffers with the fresh data from the CAS Item Stock File.
    global List_ItemCode, List_Item, List_Quantity
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []

    CreateFileIfNotExist(file_CAS_stock)
    f = open(file_CAS_stock, "r")
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



def WriteCAS():
    # Updates the CAS Stock ITEM file from the list buffers.
    global List_ItemCode, List_Item, List_Quantity
    CreateFileIfNotExist(file_CAS_stock)
    f = open(file_CAS_stock, "w")
    i = 0
    s = ""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i = i + 1
    f.write(s)
    f.close()

def LogCASItem(ListOfInputs):
    temp_date = Get_Date()
    f = open(file_CAS_log, "a")
    string = f"\n[{temp_date}] ---#--- {ListOfInputs[0]} ---#--- {ListOfInputs[1]} ---#--- {ListOfInputs[2]}"
    f.write(string)
    f.close()


def CAS():
    temp1 = EnterCAS()

    if (CAS_Subtract(temp1)): # IF ALL SUBASSEMBLIES ARE SUBTRACTED FROM NETSTOCK - (FEASIBLE)
        LogCASItem(temp1)

        ReadCAS() # FILL BUFFERS OF CAS STOCK FILE
        AddItem(temp1)  # if condition is true : INCREMENT CAS STOCK with the user CAS Input.
        WriteCAS() # WRITE THE UPDATED BUFFERS BACK TO CAS STOCK FILE.


#========================================================================================================
#MENU
def Menu():

    while(True):
        print("\n\n*** DND PLOUGH - AGRICULTURAL SHAFTS AND ACCESSORIES ***\n\n"
              "======================== MENU ======================\n"
              "    ENTER 1 - ENTER INWARD AN ITEM\n"
              "    ENTER 2 - ENTER OUTWARD AN ITEM\n"
              "    ENTER 3 - ENTER COMPLETE ASSEMBLED SHAFTS (CAS)\n\n"
              "    ENTER 4 - VIEW INWARD LOG\n"
              "    ENTER 5 - VIEW OUTWARD LOG\n"
              "    ENTER 6 - VIEW CAS LOG\n\n"
              "    ENTER 7 - VIEW INWARD STOCK\n"
              "    ENTER 8 - VIEW NET STOCK\n"
              "    Enter 9 - VIEW CAS STOCK\n\n"
              "    ENTER # - TO EXIT APPLICATION\n"
              "====================================================\n")
        x=input("    Enter: ")
        if x=="1":
            InwardItem()

        elif x=="2":
            OutwardItem()

        elif x=="3":
            CAS()

        elif x=="4":
            View(file_inward_log)

        elif x=="5":
            View(file_outward_log)

        elif x=="6":
            View(file_CAS_log)

        elif x=="7":
            View(file_inward_stock)

        elif x=="8":
            View(file_net_stock)

        elif x=="9":
            View(file_CAS_stock)

        elif x=="#":
            break
        else: print("\n    PLEASE ENTER CORRECT INPUT!\n")


Menu()
