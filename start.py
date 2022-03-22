import os,sys,json
import logging as logger
from time import time,sleep
from src.utils import *
from termcolor import colored


usernamesList = []
logger.basicConfig(encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y | %I:%M:%S %p', level=logger.DEBUG)

currentUser = str
max_create_user = 6 



def mainStart():
    logger.debug('>>> SAM started ...')
    CLEARCONSOLE()
    while True:
        try:        
            if usernamesList == []:
                loadUser()
            mainMenu()
        except KeyboardInterrupt:
            print(USEREND())
            quit(0)




def loadUser():
    with open('./save/user.json', 'r') as file:
        logger.debug('>>> Load User data')
        data = json.load(file)
        dataString =json.dumps(data)
        resp = json.loads(dataString)
        logger.debug('>>> Usernames: ')
        for i in resp:
            usernamesList.append(resp[i]['username'])
            logger.debug('- '+resp[i]['username'])
        file.close()
        logger.debug('>>> Usernames loaded.')


def mainMenu():

    global currentUser
    useramount = 0
    CLEARCONSOLE()
    print(BANNERLINE())
    print(BANNER()+Orange(COPYRIGHT()))
    print(BANNERLINE()+ '\n')
    for user in usernamesList:
        print(Blue(str(useramount+1) + ') '+ user))
        useramount +=1
    print(Blue('\n9) Benutzer erstellen (WIP)\n\n0) Beenden'))
    selected = int(input(DEFAULTINPUT()))
    logger.debug(selected)
    if selected == "":
        print(INPUTERROR())
        return
    elif selected == 9:
        newUser()        
    elif selected == 0:
        print(USEREND())
        quit(0)
    else:
        selected -=1
        currentUser = usernamesList[int(selected)]
        logger.info('>>> '+currentUser+' is logged in.')
        selected = None
        UserMenu()                            

 
def UserMenu():
    global currentUser
    CLEARCONSOLE()
    print(BANNERLINE()+'\n'+BANNER()+'\n'+BANNERLINE()+'\n')
    print(Red('Willkommen zurück '+currentUser+'!\n\n'))
    print(Blue(SAMMENU()))
    selected = int(input(DEFAULTINPUT()))
    if selected == 1:
        import SAM
        SAM
    elif selected == 2:
        currentUser = None
        mainMenu()
    elif selected == 0:
        print(USEREND())
        quit(0)

            
def newUser():
    CLEARCONSOLE()
    print(Orange("\nSAM: Neuen Benutzer erstellen"))
    print(BANNERLINE())
    sleep(2)
    print(Blue("\n\n0) Beenden\nBitte wähle einen Benutzername: "))
    username = input(Green("\n>>>> "))
    if username == "":
        CLEARWIN()
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
    file.close()     
    if username in usernames:
        print(Red("\nUser existiert bereits!\nNeustart..."))
        sleep(1.5)
        newUser()
    else:
        logger.debug(">>> Username available, Create new user: "+username)
        createUser(username)

def createUser(username):
    global usernamesList
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
    logger.debug('Der neue Account '+username +' wurde erstellt!')
    # Create User dic
    currentPath = os.path.abspath(os.getcwd())
    if not os.path.exists(currentPath+"/"+username):
        os.mkdir(currentPath+"/save/"+username)
        logger.debug('>>> Verzeichnis für '+username+' wurde angelegt.')  
    print(BANNERLINE())
    print(Orange('\n\nHallo, ')+Red(username)+ Orange('!\nWillkommen bei SAM!\n\n'))
    sleep(1.5)
    usernamesList = []
    mainStart()




mainStart()