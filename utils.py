from atexit import register
import os
from time import time, sleep
from termcolor import *
from datetime import *
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
                           PRE-Alpha v0.2
                      copyright 2022 © S3R43o3              
             
    Willkommen, 'SAM' ist ein virtueller Sprachassistent für deinen
              PC! Sage 'Hallo' um mit SAM zu sprechen!
""")

INITMENU =(rf"""
           
        SAM hat festgestellt das du noch keine Konfiguration 
          durchgeführt hast. Starte bitte den Assistenten.

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
                print(colored("ERROR\nDie letzte Eingabe war ungültig!\nBitte versuche es noch einmal.\n\nKehre zum Hauptmenü zurück ...",'white','on_red'))
                sleep(4)
                selected = None
                FirstMenu()
            elif selected == 1:
                start()
            elif selected == 0:
                print(Red('\n\nSAM wurde vom Nutzer beendet.'))
                exit(0)
            else:
                print(colored("ERROR\nDie letzte Eingabe war ungültig!\nBitte versuche es noch einmal.\n\nKehre zum Hauptmenü zurück ...",'white','on_red'))
                sleep(4)
                selected = None
                FirstMenu()
        except KeyboardInterrupt:
            CLEARWIN
            print(Red('SAM wurde vom Nutzer beendet.'))
            print("")
            print("")
            quit(0)


################################# MENU ENDE ########################################



def start():
    CLEARWIN
    print(Orange("\nSAM - Konfigurationsassisten wird initialisiert ..."))
    print(Orange('\n___________________________________________________________________________'))
    sleep(2)
    print(Blue("\n\nBitte wähle einen Benutzername: "))
    username = input(Green("\n>>>> "))
    if username == "" or username == None:
        CLEARWIN
        print(Red("Kein Benutzername gefunden!\nBeende SAM ..."))
        quit(0)
    if userExist(username):
        print("Benutzername existiert bereits")
        exit(0)
    createUser(username)
    print(Orange('Der neue Account ' + username +' wurde erstellt!\n\nKonfiguration abgeschlossen!\n\nHallo '+username+'!\nWillkommen bei SAM!'))
    print(Orange('\n\n________________________________________________________________'))





def userExist(username):
    with open('./save/user.json','r') as file:
        data = json.load(file)
        json_str = json.dumps(data)
        resp = json.loads(json_str)
        #print(resp.get('1')['username'])
        usernames =[]
        for i in resp:
            # all usernames
            usernames.append(resp[i]['username'])
            print(usernames)
            # all user
            # ID´s
        file.close()
        if username in usernames:
            print("User existiert bereits")
            return False
        else:
            print("Username available!")
            return True
        


def createUser(username):
    userIDs = []
    oldData = None
    maxID = int
    now = datetime.now()
    registertime = now.strftime("%m/%d/%Y %H:%M:%S")
    with open('./save/user.json','r') as datafile:
        oldData = json.load(datafile)
        for i in oldData:
            userIDs.append(int(i))
        
        print(userIDs)
        maxID = max(userIDs)
        print(maxID)
        datafile.close()
           
    with open('./save/user.json','w') as newData:
        newUser = {str(maxID+1):{"username":username,"userid":str(maxID + 1),"registerDate":str(registertime)}}
        newUser.update(oldData)
        json.dump(newUser,newData)
        datafile.close()        
            
        
    







            
if __name__ == '__main__':        
    FirstMenu()