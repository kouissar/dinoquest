import json
import random  
import time
import sys


from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Dino Quest', font='starwars'),
       'yellow', 'on_blue', attrs=['bold'])
print("BY RAFIK KOUISSAR @MAY,2019")
time.sleep( 2 )
    

# animation = "|/-\\"
# idx = 0
# x=false
# while x=false:
#     print(animation[idx % len(animation)]+ "\r",
#     idx += 1
#     time.sleep(0.1)

# for i in range(100):
#     time.sleep(0.1)
#     sys.stdout.write("\r" + animation[i % len(animation)])
#     sys.stdout.flush()
# print("End!")

file1 = open("brac.txt","r+")  
print(file1.read())
print
print("\t\t\tLOADING........")
time.sleep( 5 )
with open('all_dinos.json') as json_file:
    data = json.load(json_file)
    
score = 0
y=10

for x in range(y):
    index= random.randint(1,1000)
    dino_a=data['dinosaurs'][index]
    #print(dino_a.upper())
    dino_q = dino_a[0:6]
    a=input("what dinosaurs starts with " + dino_q.upper() + "------?\n")
    if a.lower() == dino_a.lower():
        score += 1
        cprint(figlet_format('correct', font='starwars'),
       'yellow', 'on_green', attrs=['bold'])
        print("Total Points: ", score)
    else:
        cprint(figlet_format('wrong', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
        print("WRONG, the answer is: " + dino_a.upper())

file1 = open("trex.txt","r+")  
print(file1.read())
print("###############################################")
print("Great effort! Your Score is: " + str(score) + " out of: " + str(y))
print("###############################################")

d= input("let's try something else. Hit enter to continue...")


with open('dino.json') as json_file:  
    data = json.load(json_file)

choice = input("give a number from 0 to 4 to reveal your mystery dinosaur. [0,1,2,3 or 4]")
print("Your mystery Dino is: " + data[int(choice)]['name'])
choice2=input("want to learn more about " + data[int(choice)]['name'] + "?")
print('Diet: ' + data[int(choice)]['diet'])
print('Era: ' + data[int(choice)]['era'])
print('Regions: ' + data[int(choice)]['regions'])
print('FeetTall: ' + data[int(choice)]['feetTall'])
