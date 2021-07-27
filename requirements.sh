#!/usr/bin/env bash
clear
echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
echo "sz-1.0-se"
echo ""
sleep 2
echo "Installing required tools..."
echo ""
sudo apt install john -y # Instal JohntheRipper
sudo apt install python3 -y # Installing Python3
clear
printf "-" && python3 --version
sleep 1.0
printf "-" && john
sleep 1.0
clear
echo "- Required tools are installed"
echo "- Running script"
python3 main.py
