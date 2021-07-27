import os
import pathlib

os.system("clear")
def greencolor(skk): print("\033[92m {}\033[00m" .format(skk))
def redcolor(skk): print("\033[91m {}\033[00m" .format(skk))

greencolor("""
█▀ █▀█ █░░ █▀█ █ ▀█▀   ▀█ █ █▀█
▄█ █▀▀ █▄▄ █▄█ █ ░█░   █▄ █ █▀▀
""")
greencolor("sz-1.0-se")
print("")
print("[0] Install required tools")
print("[1] Crack zip file")
print("[2] About")
print("[3] Exit")
print("")

menu = input("Choose: ")

if (menu == "0"):
    os.system("bash requirements.sh")
elif (menu == "1"):
    print("")
    zname = input("Zip file name: ")
    zfile = pathlib.Path(zname)
    if zfile.exists():
        os.system("clear")
        redcolor("- Getting zip hashes...")
        os.system("sleep 3")
        os.system('zip2john ' +(zname)+' > test.hash')
        os.system("clear")
        redcolor("- Checking zip hashes...")
        os.system("sleep 2.5")
        os.system("clear")
        redcolor("- Finding password... ")
        os.system("john test.hash")
        os.system("clear")
        os.system("john --show test.hash")
        os.remove("test.hash")
    else:
        print("")
        redcolor("| Zip file not found. |")
elif (menu == "2"):
    print("")
    greencolor("Sploit Zip is created by Sploit Eye. Tool is")
    greencolor("open source, source code is available on")
    greencolor("GitHub.")
    print("")
    redcolor("https://github.com/Sploit-Eye/sploit-zip")
    print("")
    greencolor("Thanks for using Sploit Zip.")
elif (menu == "3"):
    os.system("clear")
    exit()
else:
    print("")
    redcolor("Please type the given numbers.")
