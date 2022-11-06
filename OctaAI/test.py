import random
from config2db import *
import mysql.connector
#from test import oldword 
#from test import words_str_indx
from _LiveMindAction import *
from HearRecogSpeech import *

#mind2do = "SELECT words_str FROM words_tb WHERE words_str like '%,"+oldword+",%';"

#mycursor.execute(mind2do)

#myresult = mycursor.fetchall()

##for row in myresult:
##    print(row)
#words_str_indx = myresult

#words_str_indx = "select words_str from words_tb where words_str is like '%,"+oldword+",%'; "
#words_id = "select words_id from words_tb where words_str is like '%,"+oldword+",%'; "
#------------------------------------------
# 250 char -> ,hi,hello,hey,yo,heya,hai,

_sentence = speech2text().split(" ")
for i in range(len(_sentence)):
    senwordscount = len(_sentence)
    if _sentence[i] == "like" or _sentence[i] == "mean":
        oldword = _sentence[i+1]
    if _sentence[i] == "is" and _sentence[i+1] == "like" or _sentence[i] == "is" and _sentence[i+1] == "mean" or _sentence[i] == "are" and _sentence[i+1] == "like":
         newword = _sentence[i-1]
#--------------------------
mycursor = db.cursor()
mind2do = "SELECT words_str FROM words_tb WHERE words_str like '%,"+oldword+",%';"
try:
    mycursor.execute(mind2do)
    myresult = mycursor.fetchone()
    db.commit()
except:
   db.rollback()
#--------------------------
#used join() func to remove the brackets from the list or to change its to normal string :
words_str_indx = (','.join(myresult))
#oldword = words_str_indx.split(",")
for i in range(len(words_str_indx.split(","))):
    if words_str_indx.split(",")[i] == oldword:
        words_str_indx2_new = str(words_str_indx)+newword+","      
#--------------------------
mycursor = db.cursor()
mind2do = "UPDATE  words_tb SET words_str = '"+words_str_indx2_new+"' WHERE words_str like '%,"+oldword+",%';"
try:
    mycursor.execute(mind2do)
    db.commit()
except:
   db.rollback()
#--------------------------
print(x_randomMsg(words_str_indx))
db.close()
#---------------------------------------------------------



"""
#if u said somthin this AI machin will take ur sentances and search about its words to take there's id and save them as numbers wich the id numbers
#its can use them after saving it as genaration random system
#its will query the id numbers and procces them to select the words of them as random words like 10 = hi or hey or hello and more ...
#then print them that will make it more realstic like its wont speak the same words in the same meaning of these words :D
# its not need to save big file coz its will save the id of these words that's realy good idea !
#u can tell to EVE20 to save more words like u can tell her that the bonjour is like hello so its will save it inside the database with the same words in the same row! 
# hey = 10, im = 49 , fine = 43 , thx = 223 , what = 345, about = 235, you = 3234, ? = 125
#sentences_tb = this is a row : 10,49,43,223,345,235,3234,125 == hey im fine thx what about you ?
# _senten = "10,49,43,223,345,235,3234,125".split(",")
#for i in range(len(_senten)):
#   select id from words_tb where id = _senten[i]
#   print(random.choice(_senten[i]).split(","), end=" ")

"""

  
