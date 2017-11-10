import random
import time

title = """
   ___                       _           ___                                     _   
  / _ \___ _ __   __ _ _   _(_)_ __     / __\ __ _ ___  ___ _ __ ___   ___ _ __ | |_ 
 / /_)/ _ \ '_ \ / _` | | | | | '_ \   /__\/// _` / __|/ _ \ '_ ` _ \ / _ \ '_ \| __|
/ ___/  __/ | | | (_| | |_| | | | | | / \/  \ (_| \__ \  __/ | | | | |  __/ | | | |_ 
\/    \___|_| |_|\__, |\__,_|_|_| |_| \_____/\__,_|___/\___|_| |_| |_|\___|_| |_|\__|
                 |___/                                                               

"""

print(title)

def displayIntro():
	print("""You have found yourself in a basement full of the world's top
hackers. You have to access the internet in order to warn your friends about
the possibility of a nearby threat. You see 2 wireless connections you can choose
from. In one network, black hat hackers are awaiting a victim to steal packets
from as soon as the connection is established. The other network, white and
grey hats are waiting and willing to offer you extra security.""")
	print()

def chooseNetwork():
	network = ""
	while network != "1" and network != "2":
		print("\nWhich network will you connect to? (1 or 2)")
		network = input()
	return network

def connectNetwork(chosenNetwork):
	print("You click on the network...")
	time.sleep(1)
	print("You read your computer's logs...")
	time.sleep(1)
	print("You recieve an executable file which automatically...")
	print()
	time.sleep(1)  
	
	whiteHat = random.randint(1,2)

	if chosenNetwork == str(whiteHat):
		print("installs a security suite!")
	else:
		print("runs a script to steal all your private keys!")

playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
	displayIntro()
	networkNumber = chooseNetwork()
	connectNetwork(networkNumber)

	print("\nDo you want to play again? (yes or no)")
	playAgain = input().lower()
