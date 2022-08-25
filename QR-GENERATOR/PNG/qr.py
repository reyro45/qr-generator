import pyqrcode 
import png 
from pyqrcode import QRCode 
import os

os.system('clear')
print ('''

 .88888.    888888ba   a88888b.  .88888.  888888ba   88888888b .d88888b  
d8'   `8b   88    `8b d8'   `88 d8'   `8b 88    `8b  88        88.    "' 
88     88  a88aaaa8P' 88        88     88 88     88 a88aaaa    `Y88888b. 
88  db 88   88   `8b. 88        88     88 88     88  88              `8b 
Y8.  Y88P   88     88 Y8.   .88 Y8.   .8P 88    .8P  88        d8'   .8P 
 `8888PY8b  dP     dP  Y88888P'  `8888P'  8888888P   88888888P  Y88888P  
                                                                         
                 ALL THE FILES WILL BE SAVED IN PNG FOLDER

''')

text = input(' The text you want to convert :  ')
filename = input(' Name of the file without .png :  ')

url = pyqrcode.create(text) 
url.png(filename + '.png') 

x = (filename + '.png')
yn = ' (Y/N)'
yorn = input(' Want to display on the screen?'+ yn + '  :  ')

if yorn == 'Y' :
    os.system('termimage ' + x)
elif yorn == 'y' :
    os.system('termimage ' + x)
elif yorn == 'n' :
    print('    ')
elif yorn == 'N' :
    print('    ')
else :
    print('    ')
