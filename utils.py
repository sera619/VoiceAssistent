import os
from time import time, sleep
from termcolor import *
import json

class BColors:
    BACKBLUE = '\033[44m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033[0m'

CLEARWIN = print("\033c")
CLEARCONSOLE = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def Blue(text):
    return (BColors.OKCYAN+BColors.BOLD + text + BColors.CLEAR)

def Green(text):
    return (BColors.OKBLUE+BColors.BOLD + text + BColors.CLEAR)

def Orange(text):
    return (BColors.ORANGE+BColors.BOLD + text + BColors.CLEAR)       

def Red(text):
    return (BColors.RED+BColors.BOLD + text + BColors.CLEAR)


BANNERTOP = Orange('___________________________________________________________________________')
BANNER = (rf"""
  ______ _     _ _______    _______ _______ _______ ___   _______ _______ 
 / _____) |   (_|_______)  (_______|_______|_______|___) (_______|_______)
( (____ | |_____ _  _  _    _______ ______  ______    _   ______     _    
 \____ \|_____  | ||_|| |  |  ___  (_____ \(_____ \  | | (_____ \   | |   
 _____) )     | | |   | |  | |   | |_____) )_____) )_| |_ _____) )  | |   
(______/      |_|_|   |_|  |_|   |_(______/(______/(_____|______/   |_|   
""")
COPYRIGHT = (rf"""
                           Dev-Alpha v0.4
                      copyright 2022 © S3R43o3              
             
    Willkommen, 'SAM' ist ein virtueller Sprachassistent für deinen
                PC! Sage 'Hallo' um mit SAM zu sprechen!
""")

INITMENU =(rf"""
{Orange('___________________________________________________________________________')}
    
                           {Red('>>>>ACHTUNG<<<<')}
           
       {Green('SAM hat festgestellt das du noch keine Konfiguration hast.')}
               {Green('Starte bitte den Konfigurations-Assistent.')} 
{Orange('___________________________________________________________________________')}    
    
    {Blue('1) Starte Konfigurations-Assistent')}
    {Blue('0) Beenden')}
    
{Orange('Wähle eine Option')}""")

MENUTEMP = CLEARWIN ,print(BANNERTOP + Blue(BANNER)+ Orange(COPYRIGHT))

selected = None

def FirstMenu():
    while True:
        try:
            global selected
            MENUTEMP
            print(BANNERTOP+Blue(INITMENU))
            selected = int(input(Green("\n>>>> "))) 
            if selected == None:
                print(colored("\n\nERROR\nDie letzte Eingabe war ungültig!\nBitte versuche es noch einmal.\n\nKehre zum Hauptmenü zurück ...",'white','on_red'))
                sleep(4)
                selected = None
                FirstMenu()
            elif selected == 1:
                start()
            elif selected == 0:
                print(Red('\n\nSAM wurde vom Nutzer beendet.\n\n'))
                exit(0)
            else:
                print(colored("ERROR\nDie letzte Eingabe war ungültig!\nBitte versuche es noch einmal.\n\nKehre zum Hauptmenü zurück ...",'white','on_red'))
                sleep(3)
                selected = None
                FirstMenu()
        except KeyboardInterrupt:
            CLEARWIN
            print(Red('\n\nSAM wurde vom Nutzer beendet.\n\n'))
            quit(0)


################################# MENU ENDE ########################################



def start():
    CLEARWIN
    print(Orange("\nSAM - Konfigurationsassisten wird initialisiert ..."))
    print(Orange('\n___________________________________________________________________________'))
    sleep(2)
    print(Blue("\n\nGebe '0' ein zum beenden!\nBitte wähle einen Benutzername: "))
    username = input(Green("\n>>>> "))
    if username == "":
        CLEARWIN
        print(Red("Kein Benutzername gefunden!\nBeende SAM ..."))
        quit(0)
    elif username =="0":
        print(Red('\n\nSAM wurde vom Nutzer beendet!\n'))
        quit(0)
    userExist(username)

def userExist(username):
    usernames =[]
    with open('./save/user.json','r') as file:
        data = json.load(file)
        json_str = json.dumps(data)
        resp = json.loads(json_str)
        #print(resp.get('1')['username'])
        for i in resp:
            # all usernames
            usernames.append(resp[i]['username'])
            #print(usernames)
            # all user ID
            
    if username in usernames:
        print(Red("\nUser existiert bereits!\nNeustart..."))
        sleep(1.5)
        start()
    else:
        print("Username available!")
        createUser(username)

def createUser(username):
    userIDs = []
    oldData = None
    maxID = int
    with open('./save/user.json','r') as datafile:
        oldData = json.load(datafile)
        for i in oldData:
            userIDs.append(int(i))
        
        #print(userIDs)
        maxID = max(userIDs)
        #print(maxID)
        datafile.close()
           
    with open('./save/user.json','w') as newData:
        newUser = {str(maxID+1):{"username":username,"userid":str(maxID + 1)}}
        newUser.update(oldData)
        json.dump(newUser,newData)
        datafile.close()        
    print(Orange('Der neue Account ') +Blue(username) + Orange(' wurde erstellt!\n\nKonfiguration abgeschlossen!'))
    print(BANNERTOP)
    print(Orange('Hallo, ')+Red(username)+ Orange('!\nWillkommen bei SAM!\nEs geht bald weiter!\n\n'))
    exit(0)
        
    







            
if __name__ == '__main__':        
    FirstMenu()