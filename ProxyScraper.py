import requests
import time
import os
from colorama import *


def http():
 os.system('title Proxy Tool by ZexFR6#1625 - HTTP SCRAPER')
 ProxyRequest = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=http")
 with open("proxies.txt", "w") as proxywrite:
    proxywrite.write(ProxyRequest.text)
    print(Fore.RED + "Loading..." + Fore.RESET)
    time.sleep(2)
    for i in ProxyRequest:
        
        print(Fore.GREEN + ProxyRequest.text +  Fore.RESET)
    time.sleep(3)
    print(Fore.GREEN + "Succesfully Scraped Proxies And Put Into Proxies.txt"+ Fore.RESET)
    time.sleep(2)
    input(Fore.CYAN + "Press Enter to go to the main menu" + Fore.CYAN)
    time.sleep(0.3)
    os.system("cls")
    main()

def socks4():
 os.system('title Proxy Tool by ZexFR6#1625 - Socks4 Scraper')
 secondone = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=Socks4")
 with open("proxies.txt", "w") as proxywrite:
    proxywrite.write(secondone.text)
    print(Fore.RED + "Loading..." + Fore.RESET)
    time.sleep(2)
    for i in secondone:
     print(Fore.GREEN + secondone.text + Fore.RESET)
    time.sleep(3)
    print(Fore.GREEN + "Succesfully Scraped Proxies And Put Into Proxies.txt"+ Fore.RESET)
    time.sleep(2)
    input(Fore.CYAN + "Press Enter to go to the main menu" + Fore.CYAN)
    time.sleep(0.3)
    os.system("cls")
    main()

def socks5():
 os.system('title Proxy Tool by ZexFR6#1625 - Socks5 Scraper')
 thirdone = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=Socks5")
 with open("proxies.txt", "w") as proxywrite:
    proxywrite.write(thirdone.text)
    print(Fore.RED + "Loading..." + Fore.RESET)
    time.sleep(2)
    for i in thirdone:
     print(Fore.GREEN + thirdone.text + Fore.RESET)
    time.sleep(3)
    print(Fore.GREEN + "Succesfully Scraped Proxies And Put Into Proxies.txt"+ Fore.RESET)
    time.sleep(2)
    input(Fore.CYAN + "Press Enter to go to the main menu" + Fore.CYAN)
    time.sleep(0.3)
    os.system("cls")
    main()
    

def all():
    os.system('title Proxy Tool by ZexFR6#1625 - All Scraper')
    proxyrequest = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=http")
    with open("HttpProxies.txt", "w") as proxywrite:
     proxywrite.write(proxyrequest.text)
     print(Fore.RED + "Loading..." + Fore.RESET)
     time.sleep(3)
     for i in proxyrequest:
      print(Fore.GREEN + proxyrequest.text + Fore.RESET)
      print(Fore.RED + "Loading Socks4 Proxies..." + Fore.RED)
     time.sleep(3)

     sockfour = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=Socks4")
     with open("Socks4Proxies.txt", "w") as proxywrite:
      proxywrite.write(sockfour.text)
      time.sleep(3)
      for i in sockfour:
       print(Fore.GREEN + sockfour.text + Fore.RESET)
       print(Fore.RED + "Loading Socks5 Proxies..." + Fore.RED)
      time.sleep(3)
      

      sockfive = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=Socks5")
      with open("Socks5Proxies.txt", "w") as proxywrite:
        proxywrite.write(sockfive.text)
        time.sleep(3)
        for i in sockfive:
         print(Fore.GREEN + sockfive.text + Fore.RESET)
        time.sleep(3)
        print(Fore.GREEN + "Succesfully Scraped Proxies"+ Fore.RESET)
        time.sleep(2)
        input(Fore.CYAN + "Press Enter to go to the main menu" + Fore.CYAN)
        time.sleep(0.3)
        os.system("cls")
        main()

def menuscrape():
    os.system("cls")
    os.system('title Proxy Tool by ZexFR6#1625 - Scraper')
    print(Fore.GREEN + """ 
  ____                        ____                                 
 |  _ \ _ __ _____  ___   _  / ___|  ___ _ __ __ _ _ __   ___ _ __ 
 | |_) | '__/ _ \ \/ / | | | \___ \ / __| '__/ _` | '_ \ / _ \ '__|
 |  __/| | | (_) >  <| |_| |  ___) | (__| | | (_| | |_) |  __/ |   
 |_|   |_|  \___/_/\_\\__, | |____/ \___|_|  \__,_| .__/ \___|_|   
                      |___/                       |_|              
 """ + Fore.RESET)
    print(Fore.YELLOW + "1. Scrape HTTP Proxies" + Fore.RESET)
    print(Fore.LIGHTRED_EX + "2. Scrape Socks4 Proxies" + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + "3. Scrape Socks5 Proxies" + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + "4. Scrape All Proxies" + Fore.RESET)

    def askChoice():
     option = int(input("What number > "))
     if option == 1:
        os.system("cls")
        http()
     elif option == 2:
        os.system("cls")
        socks4()
     elif option == 3:
        os.system("cls")
        socks5()
     elif option == 4:
         all()
     else:
        print("Invalid Option")
        askChoice()
    
    askChoice()

def main():
    os.system('title Proxy Scraper by ZexFR6#1625 - Menu')
    print(Fore.GREEN + """ 
   _____                            _ _           _______          _     
  / ____|                          (_) |         |__   __|        | |    
 | (___   ___ _ __ ___   __ _ _ __  _| |_ _   _     | | ___   ___ | |___ 
  \___ \ / _ \ '_ ` _ \ / _` | '_ \| | __| | | |    | |/ _ \ / _ \| / __|
  ____) |  __/ | | | | | (_| | | | | | |_| |_| |    | | (_) | (_) | \__ \\
 |_____/ \___|_| |_| |_|\__,_|_| |_|_|\__|\__, |    |_|\___/ \___/|_|___/
                                           __/ |                         
                                          |___/                          
                                 Developed by ZexFR6#1625""" + Fore.RESET)
    
    
    
    
    
    
    print(Fore.LIGHTMAGENTA_EX + "1. Proxy Scraper"+ Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "2. Proxy Checker" + Fore.RESET)

    def askmain():
     option1 = int(input(Fore.LIGHTBLUE_EX + "What number > " + Fore.RESET))
     if option1 == 1:
            menuscrape()
     elif option1 == 2:
            os.system('title Proxy Tool by ZexFR6#1625 - GET ME TO 10 STARS!')
            os.system("cls")
            bob = str(input(Fore.RED + "Have we hit the 10 star goal yet > " + Fore.RESET))
            if bob == "yes":
                print("Dm me on discord - ZexFR6#1625")
                time.sleep(2)
                main()
            elif bob == "no":
                print("SO GET ME THERE!")
                time.sleep(2)
                main()
            else:
                print("What lmao?")
                time.sleep(2)
                main()
  
            
            
     else:
            print("Wrong Number")
            print("Asking Again In 3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            os.system("cls")
            askmain()
    askmain()
       

if __name__ == "__main__":
    main()
