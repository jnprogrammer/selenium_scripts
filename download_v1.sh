#!/bin/bash
#simple bash script that allows the user to download one of my 10 
#selenium python scripts for demo or what they may want from it.
url="https://raw.githubusercontent.com/jnprogrammer/selenium_scripts/master/"

echo "Enter in the name of the file with extention to download it"
printf "SE1.py\nSE1.py\nSE2.py\nSE3.py\nSE4.py\nSE5.py\nSE6.py\nSE7.py\nSE8.py\nSE9.py\nSE10.py\n"

read file
wget "${url}$file"

        
