#!/usr/bin/env bash
clear
tput setaf 2;
echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
echo "sz-1.0-se"
tput sgr0;
echo ""
sleep 2
echo "Installing required tools..."
echo ""
sudo apt install zip -y # Installing zip for creating zip files with password.
sudo apt install ncurses-utils -y # Installing ncurses-utils for text colors.
sudo apt install python3 -y # Installing Python3 for extracting zip files without password.
sudo apt install unzip -y # Installing unzip for extracting zip files with password.
clear
tput setaf 2;
clear
printf "-" && python3 --version
sleep 1.0
printf "-" && tput -V
sleep 1.0
printf "-" && unzip -version
sleep 1.0
printf "-" && zip --version
tput sgr0;
sleep 1.0
clear
tput sgr0;
clear
tput setaf 2;
echo "Required tools are installed"
sleep 2
tput sgr0;
clear
exit
