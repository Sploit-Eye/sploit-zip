#!/usr/bin/env bash
clear

version="sz-1.1-se"
python="python3"
johntheripper="john"

tput setaf 4;
echo """
█▀█ █▀▀ █▀█ █░█ █ █▀█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▀▀█ █▄█ █ █▀▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
"""
tput sgr0;
tput setaf 6;
echo $version
tput sgr0;
echo ""
sleep 2
echo "Installing required tools..."
echo ""
tput bold;
sudo apt install john -y &> /dev/null # Instal JohntheRipper
sudo apt install python3 -y &> /dev/null # Installing Python3
clear
tput sgr0;

dpkg -s $python &> /dev/null

if [ $? -eq 0 ]; then
  tput setaf 2;
  echo "- Python3 is installed"
  py=true
  sleep 1.5
  tput sgr0;
fi
dpkg -s $johntheripper &> /dev/null

if [ $? -eq 0 ]; then
  tput setaf 2;
  echo "- John & zip2john is installed."
  jn=true
  sleep 1.0
  tput sgr0;
fi

if [ "$py" = "true" ] && [ "$jn" == "true" ]; then
  tput setaf 3;
  echo "- Running script..."
  sleep 1.2
  python3 main.py
else
  tput setaf 1;
  echo "- Python3 is not installed"
  echo "- John & zip2john is not installed"
  tput sgr0;
fi
