# variable that pulls current time
# outputs when bosses are going to spawn (current time + 35)
# hotkeys for bosses e.g. 'cb1 = carrierbomb channel 1', 'cm4 = crane machinery channel 4'
# prints out a list with all the timers of the bosses & sorted from earliest to latest

# EXTRA: a non irritating sound that alarms when a boss is nearly going to spawn (1 min before expected time)


from ast import NotIn
from collections import UserString
from email.utils import localtime
from datetime import datetime, timedelta
from threading import Timer
from tracemalloc import stop
from unicodedata import name

_output = ""
new_row = ""

# dict with keys and pair values
bossList = {
            "eg1":"xx:xx", "eg2":"xx:xx", "eg3":"xx:xx", "eg4":"xx:xx", "eg5":"xx:xx", 
            "gs1":"xx:xx", "gs2":"xx:xx", "gs3":"xx:xx", "gs4":"xx:xx", "gs5":"xx:xx", 
            "cm1":"xx:xx", "cm2":"xx:xx", "cm3":"xx:xx", "cm4":"xx:xx", "cm5":"xx:xx",
            "sy1":"xx:xx", "sy2":"xx:xx", "sy3":"xx:xx", "sy4":"xx:xx", "sy5":"xx:xx", 
            "gm1":"xx:xx", "gm2":"xx:xx", "gm3":"xx:xx", "gm4":"xx:xx", "gm5":"xx:xx", 
            "cb1":"xx:xx", "cb2":"xx:xx", "cb3":"xx:xx", "cb4":"xx:xx", "cb5":"xx:xx", 
}


def channelName_headers():
    global _output

    # creates the header of the channels
    spacing = f"{'':^5}"
    fill = ("                   |                |               |               |               |              |")
    fill2 = ("___________________|________________|_______________|_______________|_______________|______________|")
    ch1_header = f"{'           |   Channel 1  '}"
    ch2_header = f"{'  |   Channel 2  ':^0}"
    ch3_header = f"{' |   Channel 3  ':^3}"
    ch4_header = f"{' |   Channel 4  ':^3}"
    ch5_header = f"{' |   Channel 5  |':^3}"
    _output += f"{spacing}\t{ch1_header}{ch2_header}{ch3_header}{ch4_header}{ch5_header}\n{fill2}\n{fill}"


def bossName_rows():

    while True:

        global _output
        global new_row
        userInput = input("")
        time = datetime.now() + timedelta(minutes = 30)
        timer = (format(time, '%H:%M'))

        # inputs key value of bossList
        if userInput in bossList:
            bossList[userInput] = timer         
        elif userInput == "show":
            print(_output, new_row)
        elif userInput == "stop":
            return
        elif userInput not in bossList:
            print("Invalid input")

        # creates the rows of the boss names
        fill = ("___________________|________________|_______________|_______________|_______________|______________|\n")
        fill2 = ("                   |                |               |               |               |              |")
        eg = (f"\nElderguard         |     {bossList['eg1']}      |     {bossList['eg2']}     |     {bossList['eg3']}     |     {bossList['eg4']}     |     {bossList['eg5']}    |")
        gs = (f"\nGarbagespider      |     {bossList['gs1']}      |     {bossList['gs2']}     |     {bossList['gs3']}     |     {bossList['gs4']}     |     {bossList['gs5']}    |")
        cm = (f"\nCrane machinery    |     {bossList['cm1']}      |     {bossList['cm2']}     |     {bossList['cm3']}     |     {bossList['cm4']}     |     {bossList['cm5']}    |")
        sy = (f"\nSyliaca            |     {bossList['sy1']}      |     {bossList['sy2']}     |     {bossList['sy3']}     |     {bossList['sy4']}     |     {bossList['sy5']}    |")
        gm = (f"\nGreemong           |     {bossList['gm1']}      |     {bossList['gm2']}     |     {bossList['gm3']}     |     {bossList['gm4']}     |     {bossList['gm5']}    |")
        cb = (f"\nCarrierbomb        |     {bossList['cb1']}      |     {bossList['cb2']}     |     {bossList['cb3']}     |     {bossList['cb4']}     |     {bossList['cb5']}    |")
        
        # prints the rows
        new_row = f"{eg}\n{fill}{fill2}{gs}\n{fill}{fill2}{cm}\n{fill}{fill2}{sy}\n{fill}{fill2}{gm}\n{fill}{fill2}{cb}\n"


def main():
    print("Usage: Boss name + number. e.g. sy1 = Syliaca channel 1.\nType 'show' to view the table.\n")
    print("--------------------------------\nBoss names\n\n[EG] Elderguard\n[GS] Garbagespider\n[CM] Crane Machinery \n[SY] Syliaca \n[CB] Carrierbomb\n--------------------------------\n")
    channelName_headers()
    bossName_rows()


main()