# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def simulate(weeks, psuccess, users):
    # for every user and every week
    # Track the number of prototypes found and create a distribution
    # [1,20][2,30] kinda thing
    sumPr = {}
    prot = 0
    for i in range(users):
        for j in range(weeks):
            br = random.random();#<0.11 is prototype dropped from boss run
            #print(br)
            if(br < .11):
                prot+=1

    return(sumPr)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(simulate(12,0.1,10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
