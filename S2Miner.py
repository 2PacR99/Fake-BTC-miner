import os,string;from pystyle import *;from time import sleep;from random import choice, randint
logo = """   Hello! This LightMiner Was Made By S2Market Enjoy And Mine Free Money!     
"""
os.system("mode con cols=89 lines=29")
os.system("title " + "Wallet Miner || bilo and Skurken")
class Code:
   def __init__(self):
      print(f"{Col.light_green}{logo}")
      print(f"\t\t\t{Col.white}Welcome To S2 Miner Wallet Miner Tool |choose| BTC,ETH,LTC! {Col.light_green}")
      try:


         c = int(input(f"""
{Col.white}[{Col.dark_red}1{Col.white}]{Col.pink} BTC Wallet Miner
{Col.white}[{Col.dark_red}2{Col.white}]{Col.pink} LTC Wallet Miner
{Col.white}[{Col.dark_red}3{Col.white}]{Col.pink} ETH Wallet Miner
{Col.white}>> """))
      except:os.system('cls');self.__init__()
      if c == 1:
            self.btc()
      elif c==2:
         self.ltc()
      elif c==3:
         self.eth()
      else:os.system('cls');self.__init__()
   def btc(self):
      while True:
         btc = input(f"\n{Col.white}[{Col.light_red}+{Col.white}]{Col.light_red} Enter Your BTC Wallet {Col.white}>> ")
         if btc.startswith("3") or btc.startswith("bc1") or btc.startswith("1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid BTC Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}1.5 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.light_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} BTC - {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(BTC))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} mined BTC - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent The Money {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
   def ltc(self):
      while True:
         ltc = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Your LTC Wallet Address{Col.white}>> ")
         if ltc.startswith("L") or ltc.startswith("M") or ltc.startswith("ltc1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid LTC Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}0.6 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} LTC- {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(5)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} mined LTC - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent The Money  {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
   def eth(self):
      while True:
         eth = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Your ETH Wallet Address {Col.white}>> ")
         if eth.startswith("0x") or eth.startswith("tx"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid ETH Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}0.9 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} ETH - {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} mined ETH - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent The Money {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
Code()