import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
                      copyright 2022 © S3R43o3              
             
    Willkommen, 'SAM' ist ein virtueller Sprachassistent für deinen
              PC! Sage 'Hallo' um mit SAM zu sprechen!
                           PRE-Alpha v0.2
{Orange('___________________________________________________________________________')}             
""")



clearConsole()
print(BANNERTOP+Blue(BANNER))
print(Red(COPYRIGHT))