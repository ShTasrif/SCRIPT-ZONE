import os, sys, time
from time import sleep
from datetime import date

today = date.today()

rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def logo ():
  os.system("clear")
  #change ascii or names
  os.system("""echo '
      ████████╗░█████╗░░██████╗██████╗░██╗███████╗
      ╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║██╔════╝
      ░░░██║░░░███████║╚█████╗░██████╔╝██║█████╗░░
      ░░░██║░░░██╔══██║░╚═══██╗██╔══██╗██║██╔══╝░░
      ░░░██║░░░██║░░██║██████╔╝██║░░██║██║██║░░░░░
      ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░                                        
-------------------------------------------------------
   ╔═══════════════════════════════════════════════╗
   ║       [✓] TOOL NAME : TERMUX HOME             ║ 
   ║       [✓] YOUTUBE : CYBER SH                  ║
   ║       [✓] GITHUB : SHTASRIF                   ║
   ║       [✓] FACEBOOK : H.CYBERSH                ║
   ║       [✓] TELEGRAM : TASRIF_HOSSEN_SHUVO      ║
   ║       [✓] INSTAGRAM : TASRIF.HOSSEN.SHUVO     ║
   ║       [✓] EMAIL : CYBERSHBD@GMAIL.COM         ║
   ╚═══════════════════════════════════════════════╝\n--------------------------------------------------------'|lolcat""")
  #your slogan
  ani(r+"\t<"+bl+"p"+r+">"+g+" ALWAYS ALLAH IS WATCHING ME :) "+r+"<"+bl+"/p"+r+">")
#  print(today.strftime("%b-%d-%Y"))
  #welcome voice
 # os.system("termux-tts-speak Welcome SH TASRIF ")
  os.system("echo '--------------------------------------------------------\n'| lolcat")
  

correctuser = "CYBER SH"
correctpwd = "SH TASRIF"

def login ():
  logo ()
  user = str(input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m ENTER USERNAME : "+c))
  if user == correctuser:
    pwd = str(input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m ENTER PASSWORD : "+c))
    print(g+"\n\t\tLOGIN SUCCESSFULL [✓]")
    time.sleep(1)
    if pwd == correctpwd:
      logo ()
    else:
      ani("\n\t\033[1;30;31m</> PLEASE ENTER CORRECT PASSWORD </>")
      time.sleep(2)
      login ()
  else:
    ani("\n\t\033[1;30;31m</> PLEASE ENTER CORRECT USERNAME </>")
    time.sleep(2)
    login ()
    
login()