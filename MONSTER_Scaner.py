# __  __  ___  _   _ ____ _____ _____ ____      _   _    _    ____ _  __ 
#|  \/  |/ _ \| \ | / ___|_   _| ____|  _ \    | | | |  / \  / ___| |/ / 
#| |\/| | | | |  \| \___ \ | | |  _| | |_) |   | |_| | / _ \| |   | ' /  
#| |  | | |_| | |\  |___) || | | |___|  _ <    |  _  |/ ___ \ |___| . \  
#|_|  |_|\___/|_| \_|____/ |_| |_____|_| \_\___|_| |_/_/   \_\____|_|\_\ 
#                                         |_____|                        
#      >>> GitHub : https://github.com/MONSTER-hp/MONSTER_HACK <<<
#        >>> Telegram Chanell : https://t.me/MONSTER_SECURIT <<<
#          >>> Web Sayte : www.Monster-Security.blogfa.com <<<
#                         </> MONSTER_hp </>

from requests import get
from colorama import init , Fore

import os
os.system('clear')
init() # colorama initialize

print(" __  __  ___  _   _ ____ _____ _____ ____      ____                            ")
print("|  \/  |/ _ \| \ | / ___|_   _| ____|  _ \    / ___|  ___ __ _ _ __   ___ _ __ ")
print("| |\/| | | | |  \| \___ \ | | |  _| | |_) |   \___ \ / __/ _` | '_ \ / _ \ '__|")
print("| |  | | |_| | |\  |___) || | | |___|  _ <     ___) | (_| (_| | | | |  __/ |   ")
print("|_|  |_|\___/|_| \_|____/ |_| |_____|_| \_\___|____/ \___\__,_|_| |_|\___|_|   ")
print("                                        |_____|                               ")
print("")
print("          >>> GitHub : https://github.com/MONSTER-hp/MONSTER_HACK <<<")
print("")
print("            >>> Telegram Chanell : https://T.me/MONSTER_SECURIT <<<")
print("")
print("              >>> Web Sayte : www.Monster-Security.blogfa.com <<<")
print("")
print("")
url = input("Web Sayte URL : ")

if url.endswith("/"):
    url = url[:-1]

wordlist = input("Dork List : ")
correct_words = []

for word in open(wordlist):
    word = word.strip("\n")
    address = url + "/" + word
    
    response = get(address)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] {} [ Open Address ]".format(word))
        correct_words.append(word)
    else:
        print(Fore.RED + "[-] {} [ Close Address ]".format(word))


print("--------------------")
print(Fore.GREEN + "[+] Found Words : ")
for word in correct_words:
    print("- " + word)
