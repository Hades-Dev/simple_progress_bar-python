#---------Code With Love By Mr_Hades 18/06/2020--------------------

import os
import time
import random


def progress_bar(color_id):
    font_color ={
        "Bk": "0",
        "B": "1",
        "G": "2",
        "A": "3",
        "R": "4",
        "P": "5",
        "Y": "6",
        "W": "7",
        "GR": "8",
        "LB": "9",
        "LG": "A",
        "LA": "B",
        "LR": "C",
        "LP": "D",
        "LY": "E",
        "LW": "F",
    }
    sg="##############################################################################"
    os.system('color '+font_color[color_id])
    p=0
    sg_index=1
    end_msg='''
                  _____________________________________
                  |                                   |
                  |         Done Successfully         |
                  |___________________________________|
                  
    '''

    for x in range(30):
        r_number = int(random.randrange(5,10))
        if p<100:
            os.system('cls')
            print("\n"+sg[1:+sg_index]+ " (Loading... ", p, " %)")
        elif p>100:
            os.system('cls')
            edit_val=p-100
            print("\n"+sg[1:+sg_index]+ " (Loading... ", p-edit_val, " %)")
            print(end_msg)
            break
        p+=r_number
        sg_index+=3
        time.sleep(0.50)


progress_bar("LG") #you can replace with ava color shortcut


#---------Code With Love By Mr_Hades 18/06/2020--------------------







