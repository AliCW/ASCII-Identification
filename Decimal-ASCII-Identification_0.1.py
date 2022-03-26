import sys
import msvcrt
import time
#from ast import literal_eval #formerly required for hex conversion
#import cv2 #pip3 install opencv-python - code ran to install module

yes = str('y') #lower case = 121 #upper case = 89
no = str('n')  #lower case = 110 #upper case = 78
#special_keys = str('special') #formerly required for special key functions - most have no ACSII value
shut_down = str('exit')
decimal = str('decimal')
hexa = str('hex')

#SPECIAL CHARACTER CONVERSION # NO LONGER REQUIRED
#def select_special_key(): #doesnt work as many have no ASCII decimal value                             #formerly required for special key functions - most have no ACSII value
#    for time_remaining in range(1,0,-1):            #awaits keyboard input without enter requirement   #formerly required for special key functions - most have no ACSII value
#        special_key_press = input('Awaiting key press \n')                                             #formerly required for special key functions - most have no ACSII value
#                                                                                                       #formerly required for special key functions - most have no ACSII value
#        #special_key_press = ord(msvcrt.getch())     #retrieves the decimal code pressed               #formerly required for special key functions - most have no ACSII value
#        int(special_key_press)                                                                         #formerly required for special key functions - most have no ACSII value
#END OF SPECIAL CHARACTER CONVERSION # NO LONGER REQUIRED

#CHARACTER TO HEXIDECIMAL CONVERSION
def character_to_hex(): #
    enter_value_hex = input('\nType your key / keys or exit to return to the start\n') #enter key / keys
    if enter_value_hex.lower() == shut_down:    #exit clause to go back to program start
        await_key_press() #exit clause to go back to program start
    #if enter_value_hex.lower() == hexa:
    #    hex_to_character()
    try:
        print('ASCII value: ' + str(enter_value_hex) + '\nCharacter:') #print key / keys supplied
        hex_string = str(enter_value_hex).encode('utf-8') #encodes the string into bytes - hex() function can only receive intergers
        print('0x' + hex_string.hex()) #prints hex - see the .hex() suffix which performs conversion - 0x prefix is missed by python so added manually
              #(hex(int(enter_value_hex))))#old code - used before byte encoding
        character_to_hex() #restarts the definition
    except ValueError:#standard value error loop
        print('\nFailed to recognise input - type error\n') #prints a failed message
        character_to_hex()
#END OF CHARACTER TO HEXIDECIMAL CONVERSION

#HEXIDECIMAL TO CHARACTER CONVERSION ------ WORK IN PROGRESS
#def hex_to_character():
#    enter_hex = input('\nType a Hexidecimal value\nType hex again to convert into hexidecimal or exit to return to the start\n')
#    if enter_hex == shut_down:
#        await_key_press()
#    if enter_hex == hexa:
#        character_to_hex()
#    try:
#        print('Hexidecimal value: 0x' + str(enter_hex) + '\nCharacter:',
#            (ord, enter_hex.encode('utf-8')))
#            hex_to_character()
#    except ValueError:
#        print('\nFailed to recognise input - type error\n')
#        hex_to_character()
#END OF HEXIDECIMAL TO CHARACTER CONVERSION

#DECIMAL TO CHARACTER CONVERSION
def identify_from_decimal(): #Identify keys from numerical code given
    enter_unicode_value = input('\nType in an ASCII value or exit to go back to the start\n') #enter the key's unicode interger
    if enter_unicode_value.lower() == shut_down: #exit switch to go back to the program start
        await_key_press() #sends back to start
    try:
        print('ASCII value: ' + str(enter_unicode_value) + '\nCharacter:', #prints the unicode supplied
              (chr(int(enter_unicode_value)))) #converts string to interger - uses chr() to determine character from supplied interger
        print('\n\n')#prints a gap
        identify_from_decimal() #sends back to the definition start
    except ValueError: #type error if wrong interger to character supplied
        print('\nFailed to recognise input - type error\n') #prints a failed message
        identify_from_decimal() #sends back to definition start
#END OF DECIMAL TO CHARACTER CONVERSION

#INITIAL PROMPT - CHARACTER TO DECIMAL CONVERSION
def await_key_press():
    select_key = input('\n Type "decimal" to identify letters from unicode values\n Type Hex to convert characters to Hexidecimal Values\n'
                       ' Type "exit" to quit\n'
                       '\n\n Type your key to receive unicode value\n\n')
    if select_key.lower() == shut_down:# or shut_down_cap:
        sys.exit()
    #if select_key.lower() == special_keys: # switch for special keys
    #    select_special_key()
    if select_key.lower() == decimal: #decimal number conversion user switch
        identify_from_decimal()
    if select_key.lower() == hexa: #hexidecimal conversion user switch
        character_to_hex()
    try: #configure as the list interrupt as with the special keys?
        print('Key: ' + str(select_key) + '\nUnicode Value:',
              (ord(select_key)))                     #trys to find unicode of single character
        await_key_press()                            #returns to the beginning
    except ValueError:                                #detects incorrect input & displays message
        print('\nFailed to recognise input - type error\n')
        await_key_press()                            #returns to the beginning after error result
#END OF INITIAL PROMPT - CHARACTER TO DECIMAL CONVERSION

await_key_press()

#ScrapBrain
