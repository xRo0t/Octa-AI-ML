
def TakeCheck():
    mycursor = db.cursor()
    kword = "SELECT words_str FROM words_tb WHERE words_str like '%,"+oldword+",%';" #"open,run,start" 
    try:
        mycursor.execute(mind2do)
        myresult = mycursor.fetchone()
        db.commit()
    except:
        db.rollback()

def ma_Open():
    return  kword
     
ma_Open = "open,run,start"
     
#open the door

#main_word its an column 
# if i said open :
    #TakeCheck():
        #if physiscal:
            #do 123
        #elif softwarely:
            # start statments: select main_word from words_tb where word_str is like '+"_word"+'
                #do(_word)

    #else: ignore

#do(_word):
    #if _word == "m_OpenApp":
        #OpenApp()
    #elif _word == "m_welcoming"
        #replay random message
    #elif _word == ""
    



#mai_words:
    #DoIt:
        #physicaly:
        #softwarly:
            
    #ask()

