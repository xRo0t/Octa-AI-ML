#please Dont edit or delete anything !
#----------------------------------
from Modules import *
#----------------------------------
"""                                                                                                                            All Functions:                                                                                                           """

#Onready Live Functions:

def x_HumCount(): pass
    #its will count how many one of humans in the room

def x_SpeakToMeCount(): pass
    #how many one speaking to it in the momnt

def x_LiveProcess(): 
    #calling functions and process data every secound! which inside it 
    while 1==1:

        continue

def x_Replay(): pass
    #aaa

def x_randomMsg(DB_MSG_ValRanStr):   

    while 1==1:
        valmsg = random.choice(DB_MSG_ValRanStr.split(","))
        if valmsg == "": 
            continue
        else:
            return valmsg

def x_SelctSameWrdDB(txtword):

    mycursor = db.cursor()
    mind2do = "SELECT words_str FROM words_tb WHERE words_str like '%,"+txtword+",%';"
    try:
        mycursor.execute(mind2do)
        myresult = mycursor.fetchone()
        db.commit()
    except:
        conn.rollback()
    x = (','.join(myresult))
    return x

def x_InsertSameWrd2DB(txtword2):

    mycursor = db.cursor()
    mind2do = "UPDATE  words_tb SET words_str = '"+txtword2+"' WHERE words_str like '%,"+txtword+",%';"
    try:
        mycursor.execute(mind2do)
        db.commit()
    except:
     conn.rollback()

def x_createOBJ():
    pass

def x_alertOBJ():
    pass

#-------------else : not in mind functions
def x_NewL(num):

    for i in range(num):
        print("\n")

#--------------words_func: 
def x_open(nxtobj):
    if nxtobj == app:
        xcore = "softwarly"
    else:
        xcore = "phisicaly"

    return xcore


#---------------------------
def x_input_now():
    _words = input().lower()
    x_input_now.result1 =_words.split()

def x_Check():
    for i in range(len(x_input_now.result1)):
        if x_input_now.result1[i] == "open" or "run":
            x_OpenApp()

def x_listening():
   # while 1==1:
   # while 1==1:
        print("listening...") 
        _words =input().lower()
        result =_words.split()
        return result #['open,youtube,on,firefox']
    #inside it we will use many of functions:








#-----------------------------------solving....
resultAs = x_listening()

def x_sentenceProcess():
        result = resultAs #['open,youtube,on,firefox']
        for i in range(len(result)):
            result[i]
            if runner(result[i]) == True: #open application 
                x_OpenApp(result[i+1])   



def x_OpenApp(app): 
   if  isOnBrowser(app[i])== True:
        _elink = 'http://www.'+app+'.com'
        os.system("firefox"+" "+_elink)
   else:
        os.system(app)

#--------------------

def isOnBrowser(_browser):
    if _browser[i+1] == "firefox" or _browser[i+2] == "firefox" or _browser[i+3] == "firefox" or _browser[i+4] == "firefox":
        return True
    else:
        return False

#-------------------keywords function-----------
def runner(keyword):
        if keyword == "open" or keyword == "run" or keyword == "start" or keyword == "play":
            return True
        else:
            return False
