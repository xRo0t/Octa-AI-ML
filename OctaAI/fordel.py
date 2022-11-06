#import webbrowser
from Modules import *

while 1==1:

    _words = input().lower() #speech2text()

    result =_words.split()

    for i in range(len(result)):
        result[i]
        if result[i] == "open" or result[i] == "run":
            app = result[i+1]
            if result[i+2] == "firefox" or result[i+3] == "firefox" or result[i+4] == "firefox":
                _browser = result[i]
            elif result[i+2] == "google" or result[i+3] == "google" or result[i+4] == "google":
                _browser = result[i]
            elif result[i+2] == "tor" or result[i+3] == "tor" or result[i+4] == "tor":
                _browser = result[i]
    
    
            _elink = 'http://www.'+app+'.com'
            os.system(_browser+" "+_elink)



