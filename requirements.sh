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
sudo apt install ncurses-utils -y # Installing ncurses-utils
sudo apt install python3 -y # Installing Python3
sudo apt install pip -y # Installing Pip
python3 -m pip install tqdm # Installing tqdm
clear
tput setaf 2;
clear
printf "-" && python3 --version
sleep 1.0
printf "-" && tput -V
sleep 1.0
printf "-" && pip --version
sleep 1.0
printf "-" && pip show tqdm
tput sgr0;
sleep 1.0
clear
tput sgr0;
clear
tput setaf 2;
echo "- Required tools are installed"
sleep 1.5
echo "- Running script"
tput sgr0;
python3 main.py
