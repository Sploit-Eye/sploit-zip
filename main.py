import os
import pathlib
import sys
import time

class design():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tanimate(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
version = "sz-1.1-se"
print(design.OKBLUE + """
█▀ █▀█ █░░ █▀█ █ ▀█▀   ▀█ █ █▀█
▄█ █▀▀ █▄▄ █▄█ █ ░█░   █▄ █ █▀▀
""" + design.ENDC)
print(design.OKCYAN + version + design.ENDC)
print("")
print(design.BOLD + "[0] Install required tools" + design.ENDC)
print(design.BOLD + "[1] Crack zip file" + design.ENDC)
print(design.BOLD + "[2] About" + design.ENDC)
print(design.BOLD + "[3] Exit" + design.ENDC)
print("")
menu = input(design.OKBLUE + "Choose: " + design.ENDC)

if (menu == "0"):
    os.system("bash requirements.sh")
elif (menu == "1"):
    os.system("clear")
    print(design.OKBLUE + """
█▀ █▀█ █░░ █▀█ █ ▀█▀   ▀█ █ █▀█
▄█ █▀▀ █▄▄ █▄█ █ ░█░   █▄ █ █▀▀
    """ + design.ENDC)
    print(design.OKCYAN + version + design.ENDC)
    print("")
    zname = input(design.WARNING + "Zip file name: " + design.ENDC)
    zfile = pathlib.Path(zname)
    if zfile.exists():
        os.system("clear")
        tanimate(design.WARNING + "- Getting zip hashes..." + design.ENDC)
        os.system("sleep 3")
        os.system('zip2john ' +(zname)+ ' > zip.hash')
        os.system("clear")
        tanimate(design.WARNING + "- Checking zip hashes..." + design.ENDC)
        os.system("sleep 2.5")
        os.system("clear")
        tanimate(design.WARNING + "- Finding password... " + design.ENDC)
        os.system("john zip.hash &> /dev/null")
        os.system("clear")
        os.system("john --show zip.hash")
        os.remove("zip.hash")
    else:
        print("")
        tanimate(design.FAIL + "| Zip file not found, type correct name of your zip file. |" + design.ENDC)
        os.system("sleep 1.4")
        os.system("python3 main.py")
elif (menu == "2"):
    os.system("clear")
    tanimate(design.OKBLUE + "Sploit Zip cracks zip file password, " + design.ENDC + design.OKGREEN + "Tool is created by Sploit Eye." + design.ENDC)
    os.system("clear")
    tanimate(design.OKCYAN + "Sploit Zip uses " + design.ENDC + design.OKGREEN + "Python & Shell language." + design.ENDC)
    os.system("clear")
    tanimate(design.WARNING + "Link - " + design.ENDC + design.OKGREEN + "https://github.com/Sploit-Eye/sploit-zip" + design.ENDC)
    os.system("sleep 2")
    os.system("python3 main.py")
elif (menu == "3"):
    os.system("clear")
    exit()
else:
    print("")
    tanimate(design.FAIL + "| Please type the given numbers. |" + design.ENDC)
    os.system("python3 main.py")
