import itertools
import string
from pyautogui import press, typewrite, hotkey
charlist = []
def start():
    enter = input("Enter a character that is not in the password\n")
    charlist.append(str(enter))
    choose = input("Any more?\n")
    if "y" in choose:
        start()
        
    else:
        pass

password = input("Enter the password\n")
start()

if "-1" in charlist:
    print(''.join(charlist))
print("""* Now Processing
* Comparing Values
* Matching Possibilities""")

    


    

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        
            for guess in itertools.product(chars, repeat=password_length):
                glist = list(guess)
                
            
                
                length = len(charlist)
                for i in range (length):
                    if not charlist[i] in glist: 
                    #if glist[0] != charlist[i]:
                        if glist[0] != charlist[i]:
                            attempts += 1
                            
                            guess = ''.join(guess)
                            if len(guess) > 5:
                                
                                typewrite(guess, interval=2)
                                press('enter')
                            
                            if guess == real:
                                print('password is {}. found in {} guesses.'.format(guess, attempts))
                                """hotkey('win')
                                press('space')
                                press('space')
                                press('space')
                                press('space')
                                typewrite('physics.pdf')
                                press('enter')
                                PAUSE = 100

                                hotkey('f5')
                                
                                
                                press('enter')"""
                            if guess == real:
                                
                                
                                
                                print(guess, attempts)
                    
                            
                                
print(guess_password(password))
"""
def guesspassword2():
    plist = []
    plists.append('password')
    plists.append('Password')
    plists.append('123456')
"""
    
    
