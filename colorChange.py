from pybosonlib import boson

bosonCtrl = boson.BosonControl()


def main():
    #Current color setup
    print "Current color:", bosonCtrl.getColorLut()
    state = input("Options: 1=WHITEHOT, 2=BLACKHOT, 3=RAINBOW, 4=RAINBOW_HC, 5=IRONBOW, 6=LAVA, 7=ARCTIC, 8=GLOBOW, 9=GRADEDFIRE, 10=HOTTEST ")
    if state == 1:
        bosonCtrl.setColorLut('WHITEHOT')
    elif state == 2:
        bosonCtrl.setColorLut('BLACKHOT')
    elif state == 3:
        bosonCtrl.setColorLut('RAINBOW')
    elif state == 4:
        bosonCtrl.setColorLut('RAINBOW_HC')
    elif state == 5:
        bosonCtrl.setColorLut('IRONBOW')
    elif state == 6:
        bosonCtrl.setColorLut('LAVA')
    elif state == 7:
        bosonCtrl.setColorLut('ARCTIC')
    elif state == 8:
        bosonCtrl.setColorLut('GLOBOW')
    elif state == 9:
        bosonCtrl.setColorLut('GRADEDFIRE')
    elif state == 10:
        bosonCtrl.setColorLut('HOTTEST')

main()