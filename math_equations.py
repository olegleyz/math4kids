import random
from time import time
import datetime
import argparse
import sys
import os

def equation():
    a = random.randint(1,9)
    sign = ' + ' if random.randint(0,1)==1 else ' - '
    b = str(random.randint(1,a if sign ==" - " else 9))
    return str(a)+sign+b+' ='
def main():
    random.seed(time())
    filename = str(datetime.date.today()) + '.txt'
    with open(filename,"w") as f:
        for i in range(30):
            line = ""
            for j in range(3):
                line += "{}{}".format(equation(),"                  ")
            print (line)
            line += "\n"
            f.write(line)
            f.write("\n")

    # if (todo):
    #     os.system("start " + filename)
    # else:
    #     os.system("open " + filename)

if __name__ == '__main__':
    main()
