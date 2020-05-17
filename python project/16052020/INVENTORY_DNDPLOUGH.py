from tkinter import *
import pandas as pd
from tabulate import tabulate
import  tkinter.messagebox as tmsg

def fun1(): pass

# Attributes = ["Item Code", "Item", "Quantity", "SUPPLIER/CUSTOMER NAME", "DOCUMENT NO.", "Date", "Remarks"]
PassWord = "testdndplough"
# files
file_inward_log="InwardItemLog.dnd"
file_outward_log="OutwardItemLog.dnd"
file_net_stock="NetStock.dnd"
file_inward_stock="InwardItemStock.dnd"
file_CAS_stock="CASItemStock.dnd"
file_CAS_log="CASItemLog.dnd"
file_CAS_Entry = "CASEntry.dnd"
file_Grouped_Inward_Entry = "GroupedInwardEntry.dnd"
file_MIN_Entry = "MIN_Entry.dnd"
file_outward_stock = "OutwardItemStock.dnd"


# Feasible then proceed or not
proceed_flag = 1 # default

#Input
input_buffer = [] # To store the user inputs during inward, outward, CAS logging.
destroy_flag = 0
# Entry Lists
List_CAS_Entry = []
List_CAS_Entry_iname = []
List_CAS_SubAssemblies = []

List_Grouped_Inward_Entry = []
List_GIE_name = []
List_GIE_SubAssemblies = []

List_MIN_iCode_Entry = []
List_MIN_iName_Entry = []
List_MIN_iValue_Entry = []


# MIN ALERT WIDGET
List_NetStock_Min = []
List_NetStock_Alert = []


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

def UpdateBody(string):
    global f2
    bodytext = StringVar()
    bodytext.set("")
    Body = Label(f2, textvariable=bodytext)
    Body.pack(fill=BOTH)
    import time
    time.sleep(1)
    bodytext.set(string)
    Body.update()

def UpdateHead(string):
    global headingtext, Head
    import time
    time.sleep(1)
    headingtext.set(string)
    Head.update()

def UpdateStatus(string):
    global Status, statustext
    import time
    time.sleep(1)
    statustext.set(f"Status - {string}")
    Status.update()

def GoToMenu(inpt): pass
    # if(inpt.upper() == "U"): Menu()

def CreateFileIfNotExist(file):
    f= open(file,"a")
    f.close()

def EnterInwardItem():
# Menu to capture Inward Item details
#     while (True):
#         while (True):
#             while(True):
#                 print("\n    ENTER INWARD ITEM DETAILS : ")
#                 i = input("    Enter Item Code = ")  # PK
#                 GoToMenu(i)
#                 n = input("    Enter Item Name = ")
#                 GoToMenu(n)
#                 q = input("    Enter Quantity = ")
#                 GoToMenu(q)
#                 sn = input("    Enter Supplier Name = ")
#                 GoToMenu(sn)
#                 dn = input("    Enter Document No. = ")
#                 GoToMenu(dn)
#                 d = input("    Enter Date dd/mm/yy = ")
#                 GoToMenu(d)
#                 ds = input("    Enter Remarks = ") # Description
#                 GoToMenu(ds)
#                 if (i != "" and n != ""): break
#                 else:
#                     print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
#
#             try:
#                 temp=int(q)
#                 break
#             except:
#                 print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
#
#         i=i.upper() #MAKE CODE UPPERCASE
#         print(f"\n    INWARD ITEM DETIALS: \n"
#               f"    ITEM CODE : {i}\n"
#               f"    ITEM NAME : {n}\n"
#               f"    QUANTITY : {q}\n"
#               f"    SUPPLIER : {sn}\n"
#               f"    DOCUMENT NO. : {dn}\n"
#               f"    DATE : {d}\n"
#               f"    REMARKS : {ds}\n")
#         confirm = input("    Press 1 to confirm INWARD entry: ")
#         GoToMenu(confirm)
#         if confirm == "1" : break
#     return [i, n, q, d, ds, sn, dn ]  # dont change the list item index order here.

    global f2 ,input_buffer, temp_frame

    UpdateHead("Log Inward Item")
    UpdateStatus("Waiting for user to enter an inward item ...")
    #=============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get()=="" or iname.get()=="" or iqty.get()=="" or  isupplier.get() == "" or idate.get()=="" or iremarks.get()=="" or idocument.get()==""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)
        sn = isupplier.get()
        dn = idocument.get()
        d = idate.get()
        ds = iremarks.get()

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n    INWARD ITEM DETIALS:\n\n"
                                              f"    ITEM CODE : {i}\n"
                                              f"    ITEM NAME : {n}\n"
                                              f"    QUANTITY : {q}\n"
                                              f"    SUPPLIER : {sn}\n"
                                              f"    DOCUMENT NO. : {dn}\n"
                                              f"    DATE : {d}\n"
                                              f"    REMARKS : {ds}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q, d, ds, sn, dn):  # dont change the list item index order here.
            input_buffer.append(x)

        InwardItem() # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame=Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="Item Code", font="TimesNewRoman 12").grid(row=0,column=0)
    Label(temp_frame, text="Item Name",font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Quantity",font="TimesNewRoman 12").grid(row=2, column=0)
    Label(temp_frame, text="Supplier",font="TimesNewRoman 12").grid(row=3, column=0)
    Label(temp_frame, text="Document No.",font="TimesNewRoman 12").grid(row=4, column=0)
    Label(temp_frame, text="Date",font="TimesNewRoman 12").grid(row=5, column=0)
    Label(temp_frame, text="Remarks",font="TimesNewRoman 12").grid(row=6, column=0)
    for dot in range(7):
        Label(temp_frame, text=":",font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()
    isupplier = StringVar()
    idocument = StringVar()
    idate = StringVar()
    iremarks = StringVar()

    Entry(temp_frame, textvariable = icode,font="TimesNewRoman 12", width="80").grid(row = 0, column = 2)
    Entry(temp_frame, textvariable = iname,font="TimesNewRoman 12", width="80").grid(row = 1, column = 2)
    Entry(temp_frame, textvariable = iqty,font="TimesNewRoman 12", width="80").grid(row=2, column=2)
    Entry(temp_frame, textvariable = isupplier,font="TimesNewRoman 12", width="80").grid(row=3, column=2)
    Entry(temp_frame, textvariable = idocument,font="TimesNewRoman 12", width="80").grid(row=4, column=2)
    Entry(temp_frame, textvariable = idate,font="TimesNewRoman 12", width="80").grid(row=5, column=2)
    Entry(temp_frame, textvariable = iremarks,font="TimesNewRoman 12", width="80").grid(row=6, column=2)

    Button(temp_frame,text="Submit",font="TimesNewRoman 12", width="80",command= GET_VAL).grid( row = 7, column =2)

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
# Inward Item\Outward Item is is added into list bufferes  / the inward stock / Outward Stock / CAS STOCK which ever party calls...
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

    temp1=input_buffer
    UpdateStatus("Inward item data submitted ...")
    LogInwardItem(temp1)
    # ============Update the Inward Stock file with updates=============
    ReadInwardItem()
    AddItem(temp1)
    WriteInwardItem() # Write down the Inward Stock file with updates.
    #============ Update NetStock with the Inward Item ==================
    ReadNetStock()
    AddItem((temp1))
    WriteNetStock()  # Write down the Net Stock file with updates.
    UpdateStatus("Inward item logged successfully !    |    Waiting for user to enter an inward item ...")
    tmsg.showinfo("Successful ! " ,f"{temp1[0]} - {temp1[1]} Logged Successfully in the Inward Stock")

#========================================================================================================

def EnterOutwardItem():
# # Menu to capture OUTWARD FILE DETAILS
#     while(True):
#         while(True):
#             while(True):
#                 print("\n    ENTER OUTWARD ITEM DETAILS : ")
#                 i = input("    Enter Item Code = ") #PK
#                 GoToMenu(i)
#                 n = input("    Enter Item Name = ")
#                 GoToMenu(n)
#                 q = input("    Enter Quantity = ")
#                 GoToMenu(q)
#                 cn = input("    Enter Customer Name = ")
#                 GoToMenu(cn)
#                 dn = input("    Enter Document No. = ")
#                 GoToMenu(dn)
#                 d = input("    Enter Date dd/mm/yy = ")
#                 GoToMenu(d)
#                 ds = input("    Enter Remarks = ")
#                 GoToMenu(ds)
#                 if (i != "" and n != ""): break
#                 else:
#                     print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
#             try:
#                 temp=int(q)
#                 break
#             except:
#                 print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
#
#         i = i.upper()  # MAKE CODE UPPERCASE
#         print(f"\n    OUTWARD ITEM DETAILS : \n"
#               f"    ITEM CODE : {i}\n"
#               f"    ITEM NAME : {n}\n"
#               f"    QUANTITY : {q}\n"
#               f"    CUSTOMER : {cn}\n"
#               f"    DOCUMENT NO. : {dn}\n"
#               f"    DATE : {d}\n"
#               f"    REMARKS : {ds}\n")
#         confirm = input("    Press 1 to confirm OUTWARD entry: ")
#         GoToMenu(confirm)
#         if confirm == "1": break
#
#     return [i, n, q, d, ds, cn, dn] # dont change the list item index order here.

    global f2 ,input_buffer, temp_frame

    UpdateHead("Log Outward Item")
    UpdateStatus("Waiting for user to enter an outward item ...")
    #=============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get()=="" or iname.get()=="" or iqty.get()=="" or  icustomer.get() == "" or idate.get()=="" or iremarks.get()=="" or idocument.get()==""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)
        cn = icustomer.get()
        dn = idocument.get()
        d = idate.get()
        ds = iremarks.get()

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n    INWARD ITEM DETIALS:\n\n"
                                              f"    ITEM CODE : {i}\n"
                                              f"    ITEM NAME : {n}\n"
                                              f"    QUANTITY : {q}\n"
                                              f"    CUSTOMER : {cn}\n"
                                              f"    DOCUMENT NO. : {dn}\n"
                                              f"    DATE : {d}\n"
                                              f"    REMARKS : {ds}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q, d, ds, cn, dn):  # dont change the list item index order here.
            input_buffer.append(x)

        OutwardItem() # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame=Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="Item Code", font="TimesNewRoman 12").grid(row=0,column=0)
    Label(temp_frame, text="Item Name",font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Quantity",font="TimesNewRoman 12").grid(row=2, column=0)
    Label(temp_frame, text="Customer",font="TimesNewRoman 12").grid(row=3, column=0)
    Label(temp_frame, text="Document No.",font="TimesNewRoman 12").grid(row=4, column=0)
    Label(temp_frame, text="Date",font="TimesNewRoman 12").grid(row=5, column=0)
    Label(temp_frame, text="Remarks",font="TimesNewRoman 12").grid(row=6, column=0)
    for dot in range(7):
        Label(temp_frame, text=":",font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()
    icustomer = StringVar()
    idocument = StringVar()
    idate = StringVar()
    iremarks = StringVar()

    Entry(temp_frame, textvariable = icode,font="TimesNewRoman 12", width="80").grid(row = 0, column = 2)
    Entry(temp_frame, textvariable = iname,font="TimesNewRoman 12", width="80").grid(row = 1, column = 2)
    Entry(temp_frame, textvariable = iqty,font="TimesNewRoman 12", width="80").grid(row=2, column=2)
    Entry(temp_frame, textvariable = icustomer,font="TimesNewRoman 12", width="80").grid(row=3, column=2)
    Entry(temp_frame, textvariable = idocument,font="TimesNewRoman 12", width="80").grid(row=4, column=2)
    Entry(temp_frame, textvariable = idate,font="TimesNewRoman 12", width="80").grid(row=5, column=2)
    Entry(temp_frame, textvariable = iremarks,font="TimesNewRoman 12", width="80").grid(row=6, column=2)

    Button(temp_frame,text="Submit",font="TimesNewRoman 12", width="80",command= GET_VAL).grid( row = 7, column =2)

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
# Also updates the net stock if feasible.
    global List_ItemCode,List_Item,List_Quantity, proceed_flag
    proceed_flag = 1
    ReadNetStock()
    # When Item is present in Net Stock
    if InputList[0] in List_ItemCode:
        for item in List_ItemCode: # Item is surely present in Net Stock.
            if item == InputList[0]:
                i = List_ItemCode.index(item)  # Find the index (row) of the item in Buffer Lists.
                if (( int(List_Quantity[i]) - int(InputList[2]) ) >= 0 ):
                    question = tmsg.askyesno("Feasible !", f"Current outward operation on {InputList[0]} - {InputList[1]} is feasible.\n\nComplete the current outward operation?")
                    if not (question):
                        proceed_flag = 0
                        return False
                    # Update Quantity List Buffer When Item Already present
                    List_Quantity[i] = int(List_Quantity[i]) - int(InputList[2])
                    WriteNetStock()
                    return True
                else:
                    # print("\n\n\n    ==========================================================\n"
                    #       "    INSUFFICIENT ITEMS IN STOCK. PLEASE PLACE AN INWARD ORDER.\n"
                    #       "    ==========================================================\n\n\n")
                    tmsg.showerror("NOT Feasible !", f"Insufficient items in Inward Stock.\nPlease log {InputList[0]} - {InputList[1]} in Inward Stock.")
                    return False
    else:  # When Item is not present in stock
        # print(f"\n\n\n    =================================================================================\n"
        #       f"    {InputList[1]}-{InputList[0]} - NEVER APPEARED IN YOUR INVENTORY.\n"
        #       f"    ==================================================================================\n\n\n")
        tmsg.showerror("Item not present in stock ",f"{InputList[0]} - {InputList[1]} never appeared in your inventory !")
        return False

def Subtract_CAS_Stock(InputList):
    global List_ItemCode, List_Item, List_Quantity, proceed_flag
    proceed_flag = 1
    ReadCAS()
    for item in List_ItemCode:  # (Item is surely present in CAS coz then only this fn is called.)
        if item == InputList[0]:
            i = List_ItemCode.index(item)  # Find the index (row) of the item in Buffer Lists.
            if ((int(List_Quantity[i]) - int(InputList[2])) >= 0):
                question = tmsg.askyesno("Feasible !", f"Current outward operation on CAS item {InputList[0]} - {InputList[1]} is feasible.\n\nComplete the current outward operation?")
                if not (question):
                    proceed_flag=0
                    return False
                # Update Quantity List Buffer When Item is sufficient to outward.
                List_Quantity[i] = int(List_Quantity[i]) - int(InputList[2])
                WriteCAS()
                return True
            else:
                # print("\n\n\n    ==========================================================\n"
                #         "    INSUFFICIENT ITEMS IN CAS STOCK. PLEASE PLACE CAS ENTRY!\n"
                #         "    ==========================================================\n\n\n")
                tmsg.showerror("NOT Feasible !", f"Insufficient items in CAS Stock.\nPlease log {InputList[0]} - {InputList[1]} in CAS Stock.")
                return False


def Subtract_Grouped_Inward_Item(ListOfCASInputs):
    # (Consider CAS word as Grouped Inward Item)
    global List_ItemCode, List_Item, List_Quantity, List_CAS_Item, List_CAS_ItemCode, List_CAS_Quantity,proceed_flag
    proceed_flag = 1
    temp_icode = []
    temp_iname = []
    temp_iquantity = []
    Read_CAS_SubASSEMBLIES(ListOfCASInputs)  # CAS LIST BUFFERS ARE FILLED WITH SUBASSEMBLY DATA
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
        flg = 0  # Item not present
        That_NetStock_item_quantity = 0
        for n_item in List_ItemCode:
            # EACH SUB_ASSEMBLY ITEM IS SEARCHED IN NETSTOCK BY MATCHING ITEM CODE WITH EACH ITEM IN NETSTOCK.
            if c_item == n_item:
                # SUBTRACT THAT ITEM QUANTITY FROM NETSTOCK
                i1 = List_CAS_ItemCode.index(c_item)
                i2 = List_ItemCode.index(n_item)
                if ((int(List_Quantity[i2]) - (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i1]))) >= 0):
                    List_Quantity[i2] = int(List_Quantity[i2]) - (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i1]))
                    flg = 1
                    break
                else:
                    # Saved the quantity of the item in netstock which is insufficient.
                    That_NetStock_item_quantity = int(List_Quantity[i2])
                    break

        # INNER FOR LOOP ENDS HERE
        if flg == 0:
            # SPECIFIC C_ITEM NOT PRESENT IN NETSTOCK
            i = List_CAS_ItemCode.index(c_item)  # Get index of missing item
            # FIll THE TEMP BUFFERS WITH MISSING ITEM DETAILS:
            temp_icode.append(List_CAS_ItemCode[i])
            temp_iname.append(List_CAS_Item[i])
            net_missing_quantity = (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i])) - That_NetStock_item_quantity

            temp_iquantity.append(net_missing_quantity)
            MISSING = 1

    # OUTER FOR LOOP ENDS HERE
    if MISSING == 1:
        # print(f"\n\n\n==========================================================================\n"
        #       f"INSUFFICIENT SUB-ASSEMBLIES IN NET-STOCK WHILE ENTERING"
        #       f" {ListOfCASInputs[1]} - {ListOfCASInputs[0]} IN OUTWARD!\n"
        #       f"==========================================================================\n")
        tmsg.showerror("NOT Feasible !",f"Insufficient SUB-ASSEMBLIES IN NET STOCK for GIE item {ListOfCASInputs[0]} - {ListOfCASInputs[1]} ")
        TableMissingItems(temp_icode, temp_iname, temp_iquantity, ListOfCASInputs)
        return False
    # IF CONTROL REACHES HERE
    # MEANS ALL SUB ASSEMBLIES ARE PRESENT AND NET STOCK QUANTITY MUST BE WRITTEN WITH UPDATED LIST BUFFERS.
    question = tmsg.askyesno("Feasible !",f"Current outward operation on GIE item {ListOfCASInputs[0]} - {ListOfCASInputs[1]} is feasible.\n\nComplete the current outward operation?")
    if not (question):
        proceed_flag = 0
        return False
    WriteNetStock()
    return True


def Read_CAS_Entry():
    global List_CAS_Entry, List_CAS_SubAssemblies, List_CAS_Entry_iname
    # Clear Buffer
    List_CAS_Entry = []
    List_CAS_Entry_iname = []
    List_CAS_SubAssemblies = []
    CreateFileIfNotExist(file_CAS_Entry)

    f = open(file_CAS_Entry,"r")
    s = f.read()
    if len(s) == 0:
        pass  # if file is empty
    else:  # If file is not Empty
        temp_list1 = s.split("\n")  # got all rows in the list.
        for item in temp_list1:  # for each row in list
            temp_str = str(item) # Convert the row into string
            temp_list2 = temp_str.split(" ---#--- ")  # got attributes of a row as list

            if temp_list2[0] == "":
                pass  # By pass "" empty item of the list due to \n
            else:
                List_CAS_Entry.append(temp_list2[0]) # Fill the buffer with CAS item code from the CAS Entry file.
                List_CAS_Entry_iname.append(temp_list2[1])
                List_CAS_SubAssemblies.append(temp_list2[2])

    f.close()



def Read_Grouped_Inward_Entry():
    global List_Grouped_Inward_Entry, List_GIE_name, List_GIE_SubAssemblies
    # Clear Buffer
    List_Grouped_Inward_Entry = []
    List_GIE_name = []
    List_GIE_SubAssemblies = []
    CreateFileIfNotExist(file_Grouped_Inward_Entry)

    f = open(file_Grouped_Inward_Entry, "r")
    s = f.read()
    if len(s) == 0:
        pass  # if file is empty
    else:  # If file is not Empty
        temp_list1 = s.split("\n")  # got all rows in the list.
        for item in temp_list1:  # for each row in list
            temp_str = str(item)  # Convert the row into string
            temp_list2 = temp_str.split(" ---#--- ")  # got attributes of a row as list

            if temp_list2[0] == "":
                pass  # By pass "" empty item of the list due to \n
            else:
                List_Grouped_Inward_Entry.append(temp_list2[0])  # Fill the buffer with Grouped-item code from the Grouped-Inward-Entry file.
                List_GIE_name.append(temp_list2[1])
                List_GIE_SubAssemblies.append(temp_list2[2])
    f.close()

def ReadOutwardItem():
    # Load the list buffers with the fresh data from the Outward Item Stock File.
    global List_ItemCode, List_Item, List_Quantity
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []

    CreateFileIfNotExist(file_outward_stock)
    f = open(file_outward_stock, "r")
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

def WriteOutwardItem():
    # Updates the outward stock file using content of List Buffers.
    global List_ItemCode, List_Item, List_Quantity
    CreateFileIfNotExist(file_outward_stock)
    f = open(file_outward_stock, "w")
    i = 0
    s = ""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i = i + 1
    f.write(s)
    f.close()


def OutwardItem():
    global input_buffer, proceed_flag
# Outwards an item if possible and makes outward log and updates net stock file.
    temp1 = input_buffer
    UpdateStatus("Outward item data submitted ...")
    #============== FILL THE ENTRY LIST BUFFERS ================
    Read_CAS_Entry()
    Read_Grouped_Inward_Entry()
    #===========================================================
    if temp1[0] in List_CAS_Entry: # If input item is present in list of CAS Entry.
        if (Subtract_CAS_Stock(temp1)):
            UpdateStatus("Outward is Feasible for CAS ...")
            LogOutwardItem(temp1)
            ReadOutwardItem()
            AddItem(temp1)
            WriteOutwardItem()  # Write down the Outward Stock file with updates.
            UpdateStatus("Outward CAS item logged successfully !    |    Waiting for user to enter an outward item ...")
            tmsg.showinfo("Successful ! ", f" CAS {temp1[0]} - {temp1[1]} Logged Successfully in the Outward Stock")
        else:
            if proceed_flag == 0:
                UpdateStatus(" Feasible outward CAS operation ABORTED !    |    Waiting for user to enter an outward item ...")
                return

            else:
                UpdateStatus("Outward is NOT Feasible for CAS ...    |    Waiting for user to enter an outward item ...")

    elif temp1[0] in List_Grouped_Inward_Entry: # If input item is present in the list of Grouped Inward Entry.
        if (Subtract_Grouped_Inward_Item(temp1)):
            UpdateStatus("Outward is Feasible for GIE ...")
            LogOutwardItem(temp1)
            ReadOutwardItem()
            AddItem(temp1)
            WriteOutwardItem()  # Write down the Outward Stock file with updates.
            UpdateStatus("Outward GIE item logged successfully !    |    Waiting for user to enter an outward item ...")
            tmsg.showinfo("Successful ! ", f"GIE {temp1[0]} - {temp1[1]} Logged Successfully in the Outward Stock")
        else:
            if proceed_flag == 0:
                UpdateStatus(" Feasible outward GIE operation ABORTED !    |    Waiting for user to enter an outward item ...")
                return
            else:
                UpdateStatus("Outward is NOT Feasible for GIE ...    |    Waiting for user to enter an outward item ...")
    else:
        if(SubtractItem(temp1)):
            UpdateStatus("Outward is Feasible for entered simple item ...")
            LogOutwardItem(temp1) # if feasible to outward then only log
            ReadOutwardItem()
            AddItem(temp1)
            WriteOutwardItem()  # Write down the Outward Stock file with updates.
            UpdateStatus("Outward simple item logged successfully !    |    Waiting for user to enter an outward item ...")
            tmsg.showinfo("Successful ! ", f"Item {temp1[0]} - {temp1[1]} Logged Successfully in the Outward Stock")
        else:
            if proceed_flag == 0:
                UpdateStatus("Feasible outward operation ABORTED !    |    Waiting for user to enter an outward item ...")
                return
            else: UpdateStatus("Outward is NOT Feasible for entered simple item ...    |    Waiting for user to enter an outward item ...")
    #================================


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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/OUTWARD-LOG-TABLE.xlsx", index=False, sheet_name="OUTWARD-LOG TABLE")
        print("\n\n\n    *** OUTWARD-LOG TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - OUTWARD-LOG-TABLE.xlsx - and try again! ***\n\n")





def TableInwardLog():
    global List_TimeStamp, List_ItemCode, List_Item, List_Quantity, List_Date, List_Remarks, List_Supplier, List_Document

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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/INWARD-LOG-TABLE.xlsx", index=False, sheet_name="INWARD-LOG TABLE")
        print("\n\n\n    *** INWARD-LOG TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - INWARD-LOG-TABLE.xlsx - and try again! ***\n\n")



def TableNetStock():
    global List_ItemCode, List_Item, List_Quantity, List_NetStock_Min, List_NetStock_Alert

    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_ItemCode)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_ItemCode[i])
        temp_list.append(List_Item[i])
        temp_list.append(List_Quantity[i])
        temp_list.append(List_NetStock_Min[i])
        temp_list.append(List_NetStock_Alert[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.","I-CODE", "I-NAME", "QTY.", "MIN", "ALERT"]
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/NET-STOCK-TABLE.xlsx", index=False, sheet_name="NET-STOCK TABLE")
        print("\n\n\n    *** NET-STOCK TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - NET-STOCK-TABLE.xlsx - and try again! ***\n\n")



def TableInwardStock():
    global  List_ItemCode, List_Item, List_Quantity

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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/INWARD-STOCK-TABLE.xlsx", index=False, sheet_name="INWARD-STOCK TABLE")
        print("\n\n\n    *** INWARD-STOCK TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - INWARD-STOCK-TABLE.xlsx - and try again! ***\n\n")



def TableCASStock():
    global List_ItemCode, List_Item, List_Quantity

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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/CAS-STOCK-TABLE.xlsx", index=False, sheet_name="CAS-STOCK TABLE")
        print("\n\n\n    *** (CAS) COMPLETE ASSEMBLED SHAFTS - STOCK TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")

    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - CAS-STOCK-TABLE.xlsx - and try again! ***\n\n")


def ReadCASLog():
    global List_ItemCode, List_Item, List_Quantity, List_TimeStamp
    # Clear the list buffers.
    List_ItemCode = []
    List_Item = []
    List_Quantity = []
    List_TimeStamp = []

    CreateFileIfNotExist(file_CAS_log)
    f = open(file_CAS_log, "r")
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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/CAS-LOG-TABLE.xlsx", index=False, sheet_name="CAS-LOG TABLE")
        print("\n\n\n    *** (CAS) COMPLETE ASSEMBLED SHAFTS - LOG TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - CAS-LOG-TABLE.xlsx - and try again! ***\n\n")




def Read_MIN_Entry():
    global List_MIN_iCode_Entry, List_MIN_iValue_Entry, List_MIN_iName_Entry
    # Clear the buffers
    List_MIN_iCode_Entry = []
    List_MIN_iValue_Entry = []
    List_MIN_iName_Entry = []

    CreateFileIfNotExist(file_MIN_Entry)
    f = open(file_MIN_Entry, "r")
    s= f.read()
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
                List_MIN_iCode_Entry.append(temp_list2[0])
                List_MIN_iName_Entry.append(temp_list2[1])
                List_MIN_iValue_Entry.append(temp_list2[2])


    f.close()

def Widget_MINALERT():
    global List_MIN_iCode_Entry, List_MIN_iValue_Entry, List_NetStock_Min, List_NetStock_Alert, List_ItemCode, List_Item, List_Quantity
    Read_MIN_Entry()
    # Clear the bufffers
    List_NetStock_Min = []
    List_NetStock_Alert = []

    for item1 in List_ItemCode:
        match = 0 # ITEM1!= ITEM2 >>> match is 0.
        for item2 in List_MIN_iCode_Entry:
            if( item1 == item2 ):
                # Find index of item1 and item2
                i1 = List_ItemCode.index(item1)
                i2 = List_MIN_iCode_Entry.index(item2)
                # APPEND Corresponding MIN VALUE matching to ITEM CODE for EACH ITEM IN NETSTOCK.
                List_NetStock_Min.append(List_MIN_iValue_Entry[i2])

                if int(List_Quantity[i1]) < int(List_MIN_iValue_Entry[i2]):
                    # Quantity in Netstock is less than minimum defined.
                    List_NetStock_Alert.append("PLACE ORDER")
                else: # Quantity in Netstock is >= minimum defined...
                    List_NetStock_Alert.append("-----------")
                match = 1
                break
        # OUTSIDE INNER FOR LOOP
        if match == 0:
            # MIN VALUE NOT DEFINED FOR THIS PARTICULAR ITEM1. HENCE DEFAULT MIN VAL IS 1.
            List_NetStock_Min.append("1")

            # Find Index of current item1 of NetStock which does not have MIN val defined.
            n = List_ItemCode.index(item1)
            if int(List_Quantity[n]) < 1:
                # Quantity in Netstock is less than default MIN (1)
                List_NetStock_Alert.append("PLACE ORDER")
            else:  # Quantity in Netstock is >= minimum defined...
                List_NetStock_Alert.append("-----------")



def TableShowSubAssemblies(temp_input, CAT):
    global List_CAS_Entry, List_Grouped_Inward_Entry, List_ItemCode, List_Item, List_Quantity
    # Clear the buffers
    List_ItemCode = []
    List_Item = []
    List_Quantity = []

    flag = 0
    if CAT == "CAS":
        if temp_input in List_CAS_Entry:
            CreateFileIfNotExist(f"{temp_input}.dnd")
            f = open(f"{temp_input}.dnd", "r")
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

        else:
            print(f"\n    CAS-CODE - {temp_input} DOES NOT EXIST IN REGISTERED CAS ENTRY LIST !\n")
            flag = 1



    elif CAT == "GIE":
        if temp_input in List_Grouped_Inward_Entry:
            CreateFileIfNotExist(f"{temp_input}.dnd")
            f = open(f"{temp_input}.dnd", "r")
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
        else:
            print(f"\n    GIE-CODE - {temp_input} DOES NOT EXIST IN REGISTERED GIE ENTRY LIST !\n")
            flag = 1

    else:
        print("ERROR : NON OF CAT (CAS/GIE) MATCHED IN TABLE SHOW SUB-ASSEMBLEIS ")
        flag = 1

    #============================= TABULATE ==============================================
    if flag == 0:
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
        try:
            df = pd.DataFrame(mydata, columns=headers)
            df.to_excel(f"EXCEL_OUTPUT/{CAT}-{temp_input}-SUB-ASSEMBLIES-TABLE.xlsx", index=False, sheet_name=f"{CAT} {temp_input} SUB-ASSEMBLIES TABLE")
            print(f"\n\n\n    *** {CAT} {temp_input} SUB-ASSEMBLIES TABLE ***")
            print("\n\n", tabulate(mydata, headers=headers), "\n\n")
        except:
            print(f"\n\n    *** PLEASE CLOSE THE FILE - {CAT}-{temp_input}-SUB-ASSEMBLIES-TABLE.xlsx - and try again! ***\n\n")



    #================================= OVER ==============================================================




def TableCASEntry():
    global List_CAS_Entry, List_CAS_Entry_iname, List_CAS_SubAssemblies
    i = 0
    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_CAS_Entry)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_CAS_Entry[i])
        temp_list.append(List_CAS_Entry_iname[i])
        temp_list.append(List_CAS_SubAssemblies[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "CAS-CODE", "CAS-NAME", "SUB-ASSEMBLIES"]
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/REGISTERED-CAS-ENTIRES-TABLE.xlsx", index=False, sheet_name="REGISTERED CAS ENTIRES TABLE")
        print("\n\n\n    *** REGISTERED ENTRIES TABLE of COMPLETE ASSEMBLED SHAFTS (CAS) ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
        if (len(List_CAS_Entry) != 0):
            temp_input = input("\n\n    *** ENTER CAS-CODE TO VIEW ITS SUB-ASSEMBLIES : ")
            GoToMenu(temp_input)
            TableShowSubAssemblies(temp_input.upper(), "CAS")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - REGISTERED-CAS-ENTIRES-TABLE.xlsx - and try again! ***\n\n")




def TableGIE():
    global List_Grouped_Inward_Entry, List_GIE_name, List_GIE_SubAssemblies

    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_Grouped_Inward_Entry)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_Grouped_Inward_Entry[i])
        temp_list.append(List_GIE_name[i])
        temp_list.append(List_GIE_SubAssemblies[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "GIE-CODE", "GIE-NAME", "SUB-ASSEMBLIES"]
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/REGISTERED-GIE-ENTIRES-TABLE.xlsx", index=False, sheet_name="REGISTERED GIE ENTIRES TABLE")
        print("\n\n\n    *** REGISTERED ENTRIES TABLE of GROUPED INWARD ENTRIES (GIE) ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
        if (len(List_Grouped_Inward_Entry) != 0):
            temp_input = input("\n\n    *** ENTER GIE-CODE TO VIEW ITS SUB-ASSEMBLIES : ")
            GoToMenu(temp_input)
            TableShowSubAssemblies(temp_input.upper(), "GIE")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - REGISTERED-GIE-ENTIRES-TABLE.xlsx - and try again! ***\n\n")





def TableMIN():
    global List_MIN_iCode_Entry, List_MIN_iName_Entry, List_MIN_iValue_Entry

    mydata = []
    n = 1  # For Serial No.
    for i in range(len(List_MIN_iCode_Entry)):
        temp_list = []
        # CHANGE THE ORDER OF STATEMENTS TO CHANGE THE ORDER OF COLUMNS IN OUTPUT.
        temp_list.append(n)  # For Serial No.
        temp_list.append(List_MIN_iCode_Entry[i])
        temp_list.append(List_MIN_iName_Entry[i])
        temp_list.append(List_MIN_iValue_Entry[i])
        # =======================================================================
        n = n + 1  # INCREMENT SERIAL NO.
        temp_tuple = tuple(temp_list)
        mydata.append(temp_tuple)  # AT LAST WE NEED LIST OF TUPLES WHERE EACH TUPLE IS A ROW OF ALL ATTRIBUTES.

    headers = ["SR NO.", "I-CODE", "I-NAME", "MIN QUANTITY"]
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/REGISTERED-MIN-QTY-TABLE.xlsx", index=False, sheet_name="REGISTERED MIN QTY TABLE")
        print("\n\n\n    *** REGISTERED ENTRIES TABLE of MINIMUM QUANTITIES FOR NET-STOCK (MIN) ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - REGISTERED-MIN-QTY-TABLE.xlsx - and try again! ***\n\n")





def TableOutwardStock():
    global List_ItemCode, List_Item, List_Quantity

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
    try:
        df = pd.DataFrame(mydata, columns=headers)
        df.to_excel("EXCEL_OUTPUT/OUTWARD-STOCK-TABLE.xlsx", index=False, sheet_name="OUTWARD-STOCK TABLE")
        print("\n\n\n    *** OUTWARD-STOCK TABLE ***")
        print("\n\n", tabulate(mydata, headers=headers), "\n\n")

    except:
        print("\n\n    *** PLEASE CLOSE THE FILE - OUTWARD-STOCK-TABLE.xlsx - and try again! ***\n\n")



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
        Widget_MINALERT()
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

    elif file==file_CAS_Entry:
        Read_CAS_Entry()
        TableCASEntry()

    elif file==file_Grouped_Inward_Entry:
        Read_Grouped_Inward_Entry()
        TableGIE()

    elif file==file_MIN_Entry:
        Read_MIN_Entry()
        TableMIN()

    elif file==file_outward_stock :
        ReadOutwardItem()
        TableOutwardStock()

    else:
        print("    ERROR MATCHING FILE NAME")
        pass
    #========================================================================
#========================================== CAS =========================================================

def EnterCAS():
    # # Menu to capture CAS Item details
    # while (True):
    #     while (True):
    #         while(True):
    #             print("\n    ENTER COMPLETE ASSEMBLED SHAFTS (CAS) DETAIL : ")
    #             i = input("    Enter CAS Product Code = ")  # PK
    #             GoToMenu(i)
    #             n = input("    Enter CAS Product Name = ")
    #             GoToMenu(n)
    #             q = input("    Enter Quantity = ")
    #             GoToMenu(q)
    #             if (i != "" and n != ""): break
    #             else:
    #                 print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
    #         try:
    #             temp = int(q)
    #             break
    #         except:
    #             print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
    #
    #     i = i.upper()  # MAKE CODE UPPERCASE
    #     print(f"\n    COMPLETE ASSEMBLED SHAFTS (CAS) DETAIL: \n"
    #           f"    CAS PRODUCT CODE : {i}\n"
    #           f"    CAS PRODUCT NAME : {n}\n"
    #           f"    QUANTITY : {q}\n"
    #           )
    #     confirm = input("    Press 1 to confirm CAS entry: ")
    #     GoToMenu(confirm)
    #     if confirm == "1": break
    #
    # return [i, n, q]  # dont change the list item index order here.
    global f2, input_buffer, temp_frame

    UpdateHead("Log Complete Assembled Shafts (CAS) Item")
    UpdateStatus("Waiting for user to enter CAS item ...")

    # =============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get() == "" or iname.get() == "" or iqty.get() == ""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n    INWARD ITEM DETIALS:\n\n"
                                              f"    ITEM CODE : {i}\n"
                                              f"    ITEM NAME : {n}\n"
                                              f"    QUANTITY : {q}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q):  # dont change the list item index order here.
            input_buffer.append(x)

        CAS()  # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="Item Code", font="TimesNewRoman 12").grid(row=0, column=0)
    Label(temp_frame, text="Item Name", font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Quantity", font="TimesNewRoman 12").grid(row=2, column=0)

    for dot in range(3):
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()

    Entry(temp_frame, textvariable=icode, font="TimesNewRoman 12", width="80").grid(row=0, column=2)
    Entry(temp_frame, textvariable=iname, font="TimesNewRoman 12", width="80").grid(row=1, column=2)
    Entry(temp_frame, textvariable=iqty, font="TimesNewRoman 12", width="80").grid(row=2, column=2)

    Button(temp_frame, text="Submit", font="TimesNewRoman 12", width="80", command=GET_VAL).grid(row=7, column=2)


def Read_CAS_SubASSEMBLIES(ListOfCASInputs):
    global List_CAS_Item, List_CAS_ItemCode, List_CAS_Quantity
    # CLear the CAS LIST Buffers
    List_CAS_ItemCode = []
    List_CAS_Item = []
    List_CAS_Quantity = []

    # Open the Item-Code File to load the subassemblies in CAS List Buffers
    CreateFileIfNotExist(f"{ListOfCASInputs[0]}.dnd")
    f = open(f"{ListOfCASInputs[0]}.dnd", "r")

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
    # print(f"\n\n\n    *** >>> {ListOfCASInputs[1]} - {ListOfCASInputs[0]} <<< MISSING SUB ASSEMBLIES TABLE ***")
    # print("\n\n", tabulate(mydata, headers=headers), "\n\n")
    tmsg.showinfo(f"Missing Sub-Assemblies | Outward operation on {ListOfCASInputs[1]} - {ListOfCASInputs[0]}", f"\n\n{tabulate(mydata, headers=headers)}\n\n" )



def CAS_Subtract(ListOfCASInputs):
    global List_ItemCode, List_Item, List_Quantity, List_CAS_Item, List_CAS_ItemCode, List_CAS_Quantity, proceed_flag
    proceed_flag = 1
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
        That_NetStock_item_quantity = 0
        for n_item in List_ItemCode:
            # EACH SUB_ASSEMBLY ITEM IS SEARCHED IN NETSTOCK BY MATCHING ITEM CODE WITH EACH ITEM IN NETSTOCK.
            if c_item == n_item:
                # SUBTRACT THAT ITEM QUANTITY FROM NETSTOCK
                i1 = List_CAS_ItemCode.index(c_item)
                i2 = List_ItemCode.index(n_item)
                if((int(List_Quantity[i2]) - (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i1]))) >= 0):
                    List_Quantity[i2] = int(List_Quantity[i2]) - (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i1]))
                    flg=1
                    break
                else:
                    # Saved the quantity of the item in netstock which is insufficient.
                    That_NetStock_item_quantity = int(List_Quantity[i2])
                    break

        #INNER FOR LOOP ENDS HERE
        if flg == 0:
            # SPECIFIC C_ITEM NOT PRESENT IN NETSTOCK
            i=List_CAS_ItemCode.index(c_item) # Get index of missing item
            # FIll THE TEMP BUFFERS WITH MISSING ITEM DETAILS:
            temp_icode.append(List_CAS_ItemCode[i])
            temp_iname.append(List_CAS_Item[i])
            net_missing_quantity = (int(ListOfCASInputs[2]) * int(List_CAS_Quantity[i])) - That_NetStock_item_quantity

            temp_iquantity.append(net_missing_quantity)
            MISSING = 1

    # OUTER FOR LOOP ENDS HERE
    if MISSING == 1:
        # print(f"\n\n\n==========================================================================\n"
        #       f"INSUFFICIENT SUB-ASSEMBLIES IN NET-STOCK WHILE ENTERING"
        #       f" {ListOfCASInputs[1]} - {ListOfCASInputs[0]} IN CAS!\n"
        #       f"==========================================================================\n")
        tmsg.showerror("NOT Feasible !",f"Insufficient SUB-ASSEMBLIES IN NET STOCK for CAS item {ListOfCASInputs[0]} - {ListOfCASInputs[1]} ")
        TableMissingItems(temp_icode, temp_iname, temp_iquantity, ListOfCASInputs)
        return False
    # IF CONTROL REACHES HERE
    # MEANS ALL SUB ASSEMBLIES ARE PRESENT AND NET STOCK QUANTITY MUST BE WRITTEN WITH UPDATED LIST BUFFERS.
    question = tmsg.askyesno("Feasible !",f"Current log operation on CAS item {ListOfCASInputs[0]} - {ListOfCASInputs[1]} is feasible.\n\nComplete the current CAS log operation?")
    if not (question):
        proceed_flag = 0
        return False
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

def Check_Registration_CAS(user_inputs):
    global List_CAS_Entry, List_CAS_SubAssemblies, List_CAS_Entry_iname
    Read_CAS_Entry()
    if (user_inputs[0] in List_CAS_Entry):
        UpdateStatus("CAS Item is registered ! Proceeding ...")
        return True
    else:
        UpdateStatus("CAS not registered but user is trying to log CAS!    |    Waiting for user to enter a CAS item ...")
        tmsg.showerror("CAS not registered !", f"CAS {user_inputs[0]} - {user_inputs[1]} is not yet registered.\n\nPlease register and try again.")
        return False


def CAS():
    global  input_buffer, proceed_flag
    temp1 = input_buffer
    UpdateStatus("CAS item data submitted ...")
    if not (Check_Registration_CAS(temp1)):
        return

    if (CAS_Subtract(temp1)): # IF ALL SUBASSEMBLIES ARE SUBTRACTED FROM NETSTOCK - (FEASIBLE)
        LogCASItem(temp1)

        ReadCAS() # FILL BUFFERS OF CAS STOCK FILE
        AddItem(temp1)  # if condition is true : INCREMENT CAS STOCK with the user CAS Input.
        WriteCAS() # WRITE THE UPDATED BUFFERS BACK TO CAS STOCK FILE.
        UpdateStatus("CAS item logged successfully !    |    Waiting for user to enter an CAS item ...")
        tmsg.showinfo("Successful ! ", f"{temp1[0]} - {temp1[1]} Logged Successfully in the CAS Stock")
    else:
        if proceed_flag == 0:
            UpdateStatus(" Feasible inward CAS operation ABORTED !    |    Waiting for user to enter a CAS item ...")
            return
        else:UpdateStatus("Logging is NOT Feasible for CAS due to missing sub-assemblies ...    |    Waiting for user to enter a CAS item ...")

def Enter_ENTRY_CAS():
    # # Menu to capture CATEGORY (CAS/ GIE) ENTRY details with SUB ASSEMBILIES
    # name=""
    # if CAT == "CAS":
    #     name = "COMPLETE ASSEMBLED SHAFTS"
    # if CAT == "GIE":
    #     name = "GROUPED INWARD ENTRY"
    # while (True):
    #     while (True):
    #         while(True):
    #             print(f"\n    REGISTER {CAT} - {name} DETAIL : ")
    #             i = input(f"    Enter {CAT} Product Code = ")  # PK
    #             GoToMenu(i)
    #             n = input(f"    Enter {CAT} Product Name = ")
    #             GoToMenu(n)
    #             q = input(f"    Enter TOTAL NUMBER OF SUB-ASSEMBLIES for {i} = ")
    #             GoToMenu(q)
    #             # ==========================================
    #             if (i != "" and n != ""): break
    #             else:
    #                 print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
    #             # ===========================================
    #         try:
    #             temp = int(q)
    #             break
    #         except:
    #             print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
    #             # ===========================================
    #
    #     i = i.upper()  # MAKE CODE UPPERCASE
    #     print(f"\n    CONFIRM {CAT} - {name} DETAIL: \n"
    #           f"    {CAT} PRODUCT CODE : {i}\n"
    #           f"    {CAT} PRODUCT NAME : {n}\n"
    #           f"    TOTAL NUMBER OF SUB-ASSEMBLIES : {q}\n"
    #           )
    #     confirm = input("    Press 1 to confirm: ")
    #     GoToMenu(confirm)
    #     if confirm == "1": break
    #     #=====================================================================
    # return [i,n,q]

    global f2, input_buffer, temp_frame

    UpdateHead("Register Complete Assembled Shafts (CAS) Product")
    UpdateStatus("Waiting for user to register CAS product ...")

    # =============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get() == "" or iname.get() == "" or iqty.get() == ""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n    CAS PRODUCT DETAILS:\n\n"
                                              f"    CAS PRODUCT CODE : {i}\n"
                                              f"    CAS PRODUCT NAME : {n}\n"
                                              f"    TOTAL NO. OF SUB-ASSEMBLIES : {q}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q):  # dont change the list item index order here.
            input_buffer.append(x)

        Register_CAS()  # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="CAS Product Code", font="TimesNewRoman 12").grid(row=0, column=0)
    Label(temp_frame, text="CAS Product Name", font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Total No. of Sub-Assemblies", font="TimesNewRoman 12").grid(row=2, column=0)

    for dot in range(3):
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()

    Entry(temp_frame, textvariable=icode, font="TimesNewRoman 12", width="50").grid(row=0, column=2)
    Entry(temp_frame, textvariable=iname, font="TimesNewRoman 12", width="50").grid(row=1, column=2)
    Entry(temp_frame, textvariable=iqty, font="TimesNewRoman 12", width="50").grid(row=2, column=2)

    Button(temp_frame, text="Submit", font="TimesNewRoman 12", width="50", command=GET_VAL).grid(row=7, column=2)

def Enter_ENTRY_GIE():
    global f2, input_buffer, temp_frame

    UpdateHead("Register Grouped Inward Entry (GIE) Item")
    UpdateStatus("Waiting for user to register GIE ...")

    # =============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get() == "" or iname.get() == "" or iqty.get() == ""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n   GIE DETAILS:\n\n"
                                              f"    GIE CODE : {i}\n"
                                              f"    GIE NAME : {n}\n"
                                              f"    TOTAL NO. OF SUB-ASSEMBLIES : {q}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q):  # dont change the list item index order here.
            input_buffer.append(x)

        Register_GIE()  # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="GIE Code", font="TimesNewRoman 12").grid(row=0, column=0)
    Label(temp_frame, text="GIE Name", font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Total No. of Sub-Assemblies", font="TimesNewRoman 12").grid(row=2, column=0)

    for dot in range(3):
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()

    Entry(temp_frame, textvariable=icode, font="TimesNewRoman 12", width="80").grid(row=0, column=2)
    Entry(temp_frame, textvariable=iname, font="TimesNewRoman 12", width="80").grid(row=1, column=2)
    Entry(temp_frame, textvariable=iqty, font="TimesNewRoman 12", width="80").grid(row=2, column=2)

    Button(temp_frame, text="Submit", font="TimesNewRoman 12", width="80", command=GET_VAL).grid(row=7, column=2)

def Write_Entry(data, filename, CAT):
    global  List_CAS_Entry, List_Grouped_Inward_Entry, List_MIN_iCode_Entry, List_MIN_iName_Entry, List_MIN_iValue_Entry, List_CAS_SubAssemblies, List_CAS_Entry_iname, List_GIE_SubAssemblies, List_GIE_name
    flg=0
    if CAT == "CAS":
        Read_CAS_Entry()
        for item1 in List_CAS_Entry:
            if (item1 == data[0]):

                # print(f"\n\nALERT: CAS {data[0]} - {data[1]} Already Registered!")
                # replace = input(f"Enter 1 - To Replace Existing CAS {data[0]} - {data[1]} Definition : ")
                # GoToMenu(replace)
                ques = tmsg.askyesno("Already Registered !",f"CAS : {data[0]} - {data[1]} is already registered !\n\nDo you want to replace?")
                if ques:
                    UpdateStatus("Replacing existing CAS Entry details...")
                    flg = 1
                    # Write
                    i1=List_CAS_Entry.index(item1) # get index
                    List_CAS_SubAssemblies[i1] = data[2] #SubeAssemblies Updated.
                    f = open(filename, "w")
                    i = 0
                    s = ""
                    for n in range(len(List_CAS_Entry)):
                        s = s + f"\n{List_CAS_Entry[i]} ---#--- {List_CAS_Entry_iname[i]} ---#--- {List_CAS_SubAssemblies[i]}"
                        i = i + 1
                    f.write(s)
                    f.close()
                    return 1
                else:
                    UpdateStatus("CAS Registration - Replacement ABORTED !    |    Waiting for the user to register CAS ...")
                    return 0



    elif CAT == "GIE":
        Read_Grouped_Inward_Entry()
        for item1 in List_Grouped_Inward_Entry:
            if (item1 == data[0]):
                # print(f"\n\nALERT: GIE {data[0]} - {data[1]} Already Registered!")
                # replace = input(f"Enter 1 - To Replace Existing GIE {data[0]} - {data[1]} Definition : ")
                ques = tmsg.askyesno("Already Registered !", f"GIE : {data[0]} - {data[1]} is already registered !\n\nDo you want to replace?")
                #GoToMenu(replace)
                if ques:
                    UpdateStatus("Replacing existing GIE entry details ...")
                    flg = 1
                    # Write
                    i1 = List_Grouped_Inward_Entry.index(item1)  # get index
                    List_GIE_SubAssemblies[i1] = data[2]  # Sub-Assemblies Updated.
                    f = open(filename, "w")
                    i = 0
                    s = ""
                    for n in range(len(List_Grouped_Inward_Entry)):
                        s = s + f"\n{List_Grouped_Inward_Entry[i]} ---#--- {List_GIE_name[i]} ---#--- {List_GIE_SubAssemblies[i]}"
                        i = i + 1
                    f.write(s)
                    f.close()
                    return 1
                else:
                    UpdateStatus("GIE Registration - Replacement ABORTED !    |    Waiting for the user to register GIE ...")
                    return 0

    else:
        if(CAT == "MIN"):
            Read_MIN_Entry()
            for item1 in List_MIN_iCode_Entry:
                if (item1 == data[0]):
                    #print(f"\n\nALERT: MIN | {data[0]} - {data[1]} Already Registered!")
                    ques=tmsg.askyesno("Already Registered !", f"Minimum QTY of {data[0]} - {data[1]} is already registered !\n\nDo you want to replace?")

                    #replace = input(f"Enter 1 - To Replace Existing MIN | {data[0]} - {data[1]} Definition : ")
                    #GoToMenu(replace)
                    if ques:
                        UpdateStatus("Replacing existing MIN Registered QTY ...")
                        flg = 1
                        # Write
                        i1 = List_MIN_iCode_Entry.index(item1)  # get index
                        List_MIN_iValue_Entry[i1] = data[2]  # SubeAssemblies Updated.
                        f = open(filename, "w")
                        i = 0
                        s = ""
                        for n in range(len(List_MIN_iCode_Entry)):
                            s = s + f"\n{List_MIN_iCode_Entry[i]} ---#--- {List_MIN_iName_Entry[i]} ---#--- {List_MIN_iValue_Entry[i]}"
                            i = i + 1
                        f.write(s)
                        f.close()
                        return 1
                    else:
                        UpdateStatus("MIN QTY Registration - Replacement ABORTED !    |    Waiting for the user to register MIN QTY ...")
                        return 0

        else:
            UpdateStatus("ERROR: CATEGORY CAS/GIE/MIN DIDNT MATCH ANY IN WRITE_ENTRY()")
            return 0


    if flg == 0 :
        f = open(filename, "a")
        s = f"\n{data[0]} ---#--- {data[1]} ---#--- {data[2]}"
        f.write(s)
        f.close()
        return 1


def Enter_SubAssemblies(data):
    # global List_ItemCode, List_Item, List_Quantity
    # # Clear Buffers
    # List_Item = []
    # List_Quantity = []
    # List_ItemCode = []
    # p= 1
    # while(p <= int(data[2])):
    #     while (True):
    #         while (True):
    #             while (True):
    #                 print(f"\n    ===== SUB-ASSEMBLY NO - {p} of {data[2]} for {data[0]}-{data[1]} =====")
    #                 i = input("    ENTER ITEM CODE = ")  # PK
    #                 GoToMenu(i)
    #                 n = input("    ENTER ITEM NAME = ")
    #                 GoToMenu(n)
    #                 q = input(f"    ENTER ITEM QUANTITY = ")
    #                 GoToMenu(q)
    #                 # ==========================================
    #                 if (i != "" and n != ""):
    #                     break
    #                 else:
    #                     print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
    #                 # ===========================================
    #             try:
    #                 temp = int(q)
    #                 break
    #             except:
    #                 print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
    #                 # ===========================================
    #
    #         i = i.upper()  # MAKE CODE UPPERCASE
    #
    #         print(f"\n    ===== SUB-ASSEMBLY NO - {p} of {data[2]} for {data[0]}-{data[1]} =====\n"
    #               f"    ITEM CODE : {i}\n"
    #               f"    ITEM NAME : {n}\n"
    #               f"    ITEM QUANTITY : {q}\n"
    #               )
    #         confirm = input("    Press 1 to confirm: ")
    #         if confirm == "1": break
    #         GoToMenu(confirm)
    #
    #
    #     List_ItemCode.append(i)
    #     List_Item.append(n)
    #     List_Quantity.append(q)
    #     p=p+1
    #
    global f2, temp_frame, List_Item, List_ItemCode, List_Quantity
    # Clear buffers
    List_Item = []
    List_Quantity = []
    List_ItemCode = []
    UpdateHead(f"Enter Sub-Assemblies of {data[0]} - {data[1]}")
    # =============================================================================================
    def GET_VAL():
        global List_Item, List_ItemCode, List_Quantity,input_buffer
        for a,b,c in zip(List_ItemCode,List_Item,List_Quantity):
            if (a.get()=="" or b.get()=="" or c.get() == ""):
                tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
                return
            try:
                int(c.get())
            except:
                tmsg.showerror("Incorrect Input", " Please enter quantity in integer value only!")
                return

        # Checks finish if Control reaches here

        confirm = tmsg.askyesno("Confirm",f" Are you sure you want to FINALLY SUBMIT?\nClick Yes to confirm and finally submit.")
        if not (confirm): return

        # Control reaches here means confirmed.
        # Append the global buffer Lists with the all the sub-assemblies data.
        for d,e,f,g in zip(List_ItemCode, List_Item, List_Quantity,range(int(input_buffer[2]))):
            temp = d.get()
            List_ItemCode[g] = temp.upper()
            List_Item[g] = e.get()
            List_Quantity[g] = f.get()
        # Entering sub-assemblies finishes and now write it.
        Write_SubAssemblies(input_buffer)

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()
    k = 0
    # Label Headings
    for p in range(int(data[2])):

        Label(temp_frame, text=f"({(p+1)})", font="TimesNewRoman 12").grid(row=k, column=0)

        Label(temp_frame, text="Sub-Assembly Item Code", font="TimesNewRoman 12").grid(row=k, column=1)
        Label(temp_frame, text="Sub-Assembly Item Name", font="TimesNewRoman 12").grid(row=k+1, column=1)
        Label(temp_frame, text="Sub-Assembly Quantity", font="TimesNewRoman 12").grid(row=k+2, column=1)
        Label(temp_frame, text=" ", font="TimesNewRoman 12").grid(row=k+3, column=1)

        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=k, column=2)
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=k+1, column=2)
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=k+2, column=2)
        Label(temp_frame, text=" ", font="TimesNewRoman 12").grid(row=k + 3, column=2)


        e1 = Entry(temp_frame, font="TimesNewRoman 12", width="80")
        e1.grid(row=k, column=3)
        List_ItemCode.append(e1)

        e2 = Entry(temp_frame, font="TimesNewRoman 12", width="80")
        e2.grid(row=k+1, column=3)
        List_Item.append(e2)

        e3 = Entry(temp_frame, font="TimesNewRoman 12", width="80")
        e3.grid(row=k+2, column=3)
        List_Quantity.append(e3)

        Label(temp_frame, text=" ", font="TimesNewRoman 12").grid(row=k + 3, column=3)
        k=k+4

    Button(temp_frame, text="Submit", font="TimesNewRoman 12", width="80", command=GET_VAL).grid(row=((4*int(data[2]))+1), column=3)



def Write_SubAssemblies(data):
    global List_ItemCode, List_Item, List_Quantity, temp_frame
    CreateFileIfNotExist(f"{data[0]}.dnd")
    f = open(f"{data[0]}.dnd", "w")
    i = 0
    s = ""
    for n in range(len(List_ItemCode)):
        s = s + f"\n{List_ItemCode[i]} ---#--- {List_Item[i]} ---#--- {List_Quantity[i]}"
        i = i + 1
    f.write(s)
    f.close()
    UpdateStatus(f"SUCCESSFUL REGISTRATION OF {data[0]} - {data[1]} WITH {data[2]} SUB-ASSEMBLIES !")
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()
    UpdateHead(" ")
    tmsg.showinfo("Successful",f"SUCCESSFUL REGISTRATION OF {data[0]} - {data[1]} WITH {data[2]} SUB-ASSEMBLIES !")





def Register_CAS():
    global file_CAS_Entry, input_buffer
    temp1= input_buffer #Enter_ENTRY("CAS")
    UpdateStatus("CAS registration data submitted ...")
    o = Write_Entry(temp1, file_CAS_Entry, "CAS")
    if o == 1:
        UpdateStatus(f"Waiting for user to finish entering Sub - Assemblies of CAS {temp1[0]} - {temp1[1]}")
        Enter_SubAssemblies(temp1)
        #Write_SubAssemblies(temp1)

def Register_GIE():
    global file_Grouped_Inward_Entry, input_buffer
    temp1= input_buffer #Enter_ENTRY("GIE")
    UpdateStatus("GIE registration data submitted ...")
    o =Write_Entry(temp1, file_Grouped_Inward_Entry, "GIE")
    if o == 1:
        UpdateStatus(f"Waiting for user to finish entering Sub - Assemblies of CAS {temp1[0]} - {temp1[1]}")
        Enter_SubAssemblies(temp1)
        #Write_SubAssemblies(temp1)

def Enter_MIN_Entry():
    # while (True):
    #     while (True):
    #         while(True):
    #             print(f"\n    REGISTER MINIMUM QUANTITY OF AN ITEM FOR NET-STOCK: ")
    #             i = input(f"    Enter Item Code = ")  # PK
    #             GoToMenu(i)
    #             n = input(f"    Enter Item Name = ")
    #             GoToMenu(n)
    #             q = input(f"    Enter MINIMUM Quantity Needed = ")
    #             GoToMenu(q)
    #             # ==========================================
    #             if (i != "" and n != ""): break
    #             else:
    #                 print("\n\n\n    ERROR: Item Code and Item Name should not be blank! \n\n\n")
    #             # ===========================================
    #         try:
    #             temp = int(q)
    #             break
    #         except:
    #             print("\n\n\n    ERROR ! PLEASE ENTER QUANTITY IN INTEGERS.\n\n\n")
    #             # ===========================================
    #
    #     i = i.upper()  # MAKE CODE UPPERCASE
    #     print(f"\n    CONFIRM  MINIMUM QUANTITY OF AN ITEM FOR NET-STOCK:\n"
    #           f"    ITEM CODE : {i}\n"
    #           f"    ITEM NAME : {n}\n"
    #           f"    MINIMUM QUANTITY NEEDED : {q}\n"
    #           )
    #     confirm = input("    Press 1 to confirm: ")
    #     GoToMenu(confirm)
    #     if confirm == "1": break
    #     #=====================================================================
    # return [i,n,q]
    global f2, input_buffer, temp_frame

    UpdateHead("Register Minimum Quantity of an Item for Net Stock")
    UpdateStatus("Waiting for user to register MIN QTY item details ...")

    # =============================================================================================
    def GET_VAL():
        global input_buffer
        input_buffer = []
        if (icode.get() == "" or iname.get() == "" or iqty.get() == ""):
            tmsg.showerror("Input Cannot be Empty", "Please fill up all the input fields with relevant data!")
            return

        try:

            q = int(iqty.get())

        except:
            tmsg.showerror("Incorrect Input", " Please enter minimum quantity in integer value only!")
            return

        # Checks finish
        # Fetch values
        i = icode.get()
        i = i.upper()
        n = iname.get()
        q = str(q)

        # Confirm
        confirm = tmsg.askokcancel("Confirm", f"\n    INWARD ITEM DETIALS:\n\n"
                                              f"    ITEM CODE : {i}\n"
                                              f"    ITEM NAME : {n}\n"
                                              f"    MINIMUM QUANTITY NEEDED : {q}\n"
                                              f"\n Click OK to CONFIRM ! ")
        if not (confirm): return
        # write into global input buffer
        for x in (i, n, q):  # dont change the list item index order here.
            input_buffer.append(x)

        Register_MIN()  # Input found successfully , Continue the main execution ...

    # =============================================================================
    # Destroy the existing frame and create new frame
    temp_frame.destroy()
    temp_frame = Frame(f2, pady=100)
    temp_frame.pack()

    # Label Headings
    Label(temp_frame, text="Item Code", font="TimesNewRoman 12").grid(row=0, column=0)
    Label(temp_frame, text="Item Name", font="TimesNewRoman 12").grid(row=1, column=0)
    Label(temp_frame, text="Minimum Quantity", font="TimesNewRoman 12").grid(row=2, column=0)

    for dot in range(3):
        Label(temp_frame, text=":", font="TimesNewRoman 12").grid(row=dot, column=1)

    # Variables Defined
    icode = StringVar()
    iname = StringVar()
    iqty = StringVar()

    Entry(temp_frame, textvariable=icode, font="TimesNewRoman 12", width="80").grid(row=0, column=2)
    Entry(temp_frame, textvariable=iname, font="TimesNewRoman 12", width="80").grid(row=1, column=2)
    Entry(temp_frame, textvariable=iqty, font="TimesNewRoman 12", width="80").grid(row=2, column=2)

    Button(temp_frame, text="Submit", font="TimesNewRoman 12", width="80", command=GET_VAL).grid(row=7, column=2)


def Register_MIN():
    global file_MIN_Entry, input_buffer
    temp1= input_buffer
    UpdateStatus("MIN quantity data submitted ...")
    o = Write_Entry(temp1, file_MIN_Entry, "MIN")
    if o == 1:
        UpdateStatus("MIN quantity registered successfully !    |    Waiting for user to enter MIN quantity of an item ...")
        tmsg.showinfo("Successful ! ", f"MIN QTY of {temp1[0]} - {temp1[1]} Registered Successfully !")

#========================================================================================================
#MENU
# def Menu():
#
#     while(True):
#         print("\n\n*** DND PLOUGH - AGRICULTURAL SHAFTS AND ACCESSORIES ***\n\n"
#               "======================== MENU ======================\n"
#               "    ENTER 1 - ENTER AN INWARD ITEM\n"
#               "    ENTER 2 - ENTER AN OUTWARD ITEM\n"
#               "    ENTER 3 - ENTER COMPLETE ASSEMBLED SHAFTS (CAS)\n\n"
#               "    ENTER 4 - VIEW INWARD LOG\n"
#               "    ENTER 5 - VIEW OUTWARD LOG\n"
#               "    ENTER 6 - VIEW CAS LOG\n\n"
#               "    ENTER 7 - VIEW INWARD STOCK\n"
#               "    ENTER 8 - VIEW OUTWARD STOCK\n"
#               "    Enter 9 - VIEW CAS STOCK\n\n"
#               "    Enter 10 - VIEW NET STOCK\n\n"
#               "    Enter A - REGISTER NEW CAS\n"
#               "    ENTER B - REGISTER NEW GROUPED-INWARD-ENTRY (GIE)\n"
#               "    ENTER C - REGISTER NEW MIN QUANTITY\n\n"
#               "    ENTER D - VIEW REGISTERED CAS Entries\n"
#               "    ENTER E - VIEW REGISTERED GIE Entries\n"
#               "    ENTER F - VIEW REGISTERED MIN Entries\n\n"
#               "    ENTER # - TO EXIT APPLICATION\n"
#               "====================================================\n")
#         x=input("    Enter: ")
#         GoToMenu(x)
#
#         if x=="1":
#             InwardItem()
#
#         elif x=="2":
#             OutwardItem()
#
#         elif x=="3":
#             CAS()
#
#         elif x=="4":
#             View(file_inward_log)
#
#         elif x=="5":
#             View(file_outward_log)
#
#         elif x=="6":
#             View(file_CAS_log)
#
#         elif x=="7":
#             View(file_inward_stock)
#
#         elif x=="8":
#             View(file_outward_stock)
#
#         elif x=="9":
#             View(file_CAS_stock)
#
#         elif x=="10":
#             View(file_net_stock)
#
#         elif x=="A" or x=="a":
#             Register_CAS()
#
#         elif x=="B" or x=="b":
#             Register_GIE()
#
#         elif x=="C" or x=="c":
#             Register_MIN()
#
#         elif x=="D" or x=="d":
#             View(file_CAS_Entry)
#
#         elif x=="E" or x=="e":
#             View(file_Grouped_Inward_Entry)
#
#         elif x=="F" or x=="f":
#             View(file_MIN_Entry)
#
#         elif x=="#":
#             break
#         else: print("\n    PLEASE ENTER CORRECT INPUT!\n")
#
# def PASSWORD():
#     global PassWord
#     while(True):
#         print("\n\n*** DND PLOUGH - AGRICULTURAL SHAFTS AND ACCESSORIES ***\n")
#         if PassWord == (input("    ENTER PASSWORD: ")):
#             return True
#
# if PASSWORD(): Menu()



#======================================= GUI ====================================================================

root = Tk()

# Geometry is the default application window size when it is launched.
root.geometry("733x434")

# MINIMUM WINDOW SIZE
root.minsize(733,434)


# Windows's Title
root.title("INVENTORY - DND PLOUGH")

# Label = user can't interact with label
Title=Label(text="INVENTORY - DND PLOUGH", bg="black", fg="white", font=("comicsansms",8))
Title.pack(fill=X)

statustext = StringVar()
statustext.set("Status - Ready !")
Status = Label(textvariable = statustext ,anchor=W, bg = "orange", fg="black", padx="2", pady="2", font=("comicsansms",8))
Status.pack( side=BOTTOM, fill=X )
#========================================================
# Paned Window 1
w1=PanedWindow(root)
w1.pack(fill=BOTH,expand=1)
#=========================================================
f1 = Frame(w1, bg="#2B2D2F", borderwidth=6, relief=RIDGE,padx="4")
w1.add(f1)
#==============================================================
l1=Label(f1,text="MENU", font="Helvetica 8 bold",)
l1.pack(fill=X,pady=5)
#=====================================================
#Log Items
l2=Label(f1,text="LOG ITEMS", font="Helvetica 8 bold",bg="red",fg="#faebd7")
l2.pack(fill=X, pady=10)

b1=Button( f1, text="LOG INWARD ITEM", font="Helvetica 8 bold",bg="#faebd7",fg="red",command=EnterInwardItem)
b1.pack(fill=X)

b2=Button( f1, text="LOG OUTWARD ITEM", font="Helvetica 8 bold",bg="#faebd7",fg="red",command=EnterOutwardItem)
b2.pack(fill=X)

b3=Button( f1, text="LOG COMPLETE ASSEMBLED SHAFTS (CAS)", font="Helvetica 8 bold",bg="#faebd7",fg="red",command=EnterCAS)
b3.pack(fill=X)
#=====================================================================================
# View Logs

l3=Label(f1,text="VIEW LOGS", font="Helvetica 8 bold",bg="#6a097d", fg="#D4AFCD")
l3.pack(fill=X,pady=10)

b4=Button( f1, text="INWARD LOG", font="Helvetica 8 bold",bg="#D4AFCD",fg="#6a097d",command=fun1)
b4.pack(fill=X)

b5=Button( f1, text="OUTWARD LOG", font="Helvetica 8 bold",bg="#D4AFCD",fg="#6a097d",command=fun1)
b5.pack(fill=X)

b6=Button( f1, text="CAS LOG", font="Helvetica 8 bold",bg="#D4AFCD",fg="#6a097d",command=fun1)
b6.pack(fill=X)

#======================================================================================
# View Stocks

l4=Label(f1,text="VIEW STOCKS", font="Helvetica 8 bold",bg="green", fg="#B2DBBF")
l4.pack(fill=X, pady=10)

b7=Button( f1, text="INWARD STOCK", font="Helvetica 8 bold",bg="#B2DBBF",fg="green",command=fun1)
b7.pack(fill=X)

b8=Button( f1, text="OUTWARD STOCK", font="Helvetica 8 bold",bg="#B2DBBF",fg="green",command=fun1)
b8.pack(fill=X)

b9=Button( f1, text="CAS STOCK", font="Helvetica 8 bold",bg="#B2DBBF",fg="green",command=fun1)
b9.pack(fill=X)

b10=Button( f1, text="NET STOCK", font="Helvetica 8 bold",bg="#B2DBBF",fg="green",command=fun1)
b10.pack(fill=X)
#=============================================================================================
# Register
l5=Label(f1,text="REGISTER", font="Helvetica 8 bold",bg="#120136", fg="#40bad5")
l5.pack(fill=X,pady=10)

b11=Button( f1, text="CAS", font="Helvetica 8 bold",bg="#40bad5",fg="#120136",command=Enter_ENTRY_CAS)
b11.pack(fill=X)

b12=Button( f1, text="GROUPED-INWARD-ENTRY (GIE)", font="Helvetica 8 bold",bg="#40bad5",fg="#120136",command=Enter_ENTRY_GIE)
b12.pack(fill=X)

b13=Button( f1, text="MIN QUANTITY", font="Helvetica 8 bold",bg="#40bad5",fg="#120136",command=Enter_MIN_Entry)
b13.pack(fill=X)
#=====================================================================================
# View Registered Entires

l6=Label(f1,text="VIEW REGISTERED ENTRIES", font="Helvetica 8 bold",bg="orange", fg="brown")
l6.pack(fill=X,pady=10)

b14=Button( f1, text="CAS ENTRIES", font="Helvetica 8 bold",bg="brown",fg="orange",command=fun1)
b14.pack(fill=X)

b15=Button( f1, text="GIE ENTRIES", font="Helvetica 8 bold",bg="brown",fg="orange",command=fun1)
b15.pack(fill=X)

b16=Button( f1, text="MIN QTY ENTRIES", font="Helvetica 8 bold",bg="brown",fg="orange",command=fun1)
b16.pack(fill=X)
#======================================================================================
# Paned Window2

w2=PanedWindow(w1, orient=VERTICAL)
w1.add(w2)

headingtext = StringVar()
headingtext.set("")
Head = Label(w2, textvariable=headingtext, relief= RIDGE, font="Georgia 14 bold")
w2.add(Head)

f2=Frame(w2, borderwidth=6, relief=RIDGE)
w2.add(f2)

temp_frame=Frame(f2)
temp_frame.pack()



#======================================================================================
root.mainloop()

