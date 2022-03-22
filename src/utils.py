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

def CLEARCONSOLE():
    return lambda: os.system('cls' if os.name == 'nt' else 'clear')

def CLEARWIN():
    return "\033c"
    


def Blue(text):
    return (BColors.OKCYAN+BColors.BOLD + text + BColors.CLEAR)

def Green(text):
    return (BColors.OKBLUE+BColors.BOLD + text + BColors.CLEAR)

def Orange(text):
    return (BColors.ORANGE+BColors.BOLD + text + BColors.CLEAR)       

def Red(text):
    return (BColors.RED+BColors.BOLD + text + BColors.CLEAR)

def BANNER():
    return (Blue(rf"""
      ______ _     _ _______    _______ _______ _______ ___   _______ _______ 
     / _____) |   (_|_______)  (_______|_______|_______|___) (_______|_______)
    ( (____ | |_____ _  _  _    _______ ______  ______    _   ______     _    
     \____ \|_____  | ||_|| |  |  ___  (_____ \(_____ \  | | (_____ \   | |   
     _____) )     | | |   | |  | |   | |_____) )_____) )_| |_ _____) )  | |   
    (______/      |_|_|   |_|  |_|   |_(______/(______/(_____|______/   |_|   
    """))
    
def INITMENU():
    return (rf"""{Orange('___________________________________________________________________________')}
        
                            {Red('>>>>ACHTUNG<<<<')}
            
        {Green('SAM hat festgestellt das du noch keine Konfiguration hast.')}
                {Green('Starte bitte den Konfigurations-Assistent.')} 
    {Orange('___________________________________________________________________________')}    
        
        {Blue('1) Starte Konfigurations-Assistent')}
        {Blue('0) Beenden')}
        
    {Orange('Wähle eine Option')}""")
    
def BANNERLINE():
    return (rf"""{Orange('________________________________________________________________________________')}""")

def COPYRIGHT():
    return (rf"""
                                Dev-Alpha v0.5
                            copyright 2022 © S3R43o3              
                
                Willkommen, 'SAM' ist ein virtueller Sprachassistent
                                für deinen PC! 
    """)


def SAMMENU():
    return (rf"""1) SAM starten
2) Hauptmenü

0) Beenden
            
""")



def USEREND():
    return Red('\n\nSAM wurde vom Nutzer beendet.\n\n')

def INPUTERROR():
    return colored("\n\nERROR\nDie letzte Eingabe war ungültig!\nBitte versuche es noch einmal.\n\nKehre zum Hauptmenü zurück ...",'white','on_red')

def DEFAULTINPUT():
    return Orange('\nWähle eine Option: ')

selected = None



################################# MENU ENDE ########################################



        
    