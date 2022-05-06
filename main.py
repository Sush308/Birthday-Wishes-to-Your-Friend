import time as t
from pygame import mixer

mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("happy-birthday-song.mp3")
mixer.music.play()

x = "My Dear Friends"
b = len(x)

def cake():
    print(" " * 23, "i i i i i")
    t.sleep(1)
    print(" " * 23, "i i i i i")
    t.sleep(1)
    print(" " * 21, "__i_i_i_i_i__")
    t.sleep(1)
    print(" " * 20, "|", " " * 11, "|")
    t.sleep(1)
    print(" " * 20, "|", " " * 11, "|")
    t.sleep(1)
    print(" " * 20, "|", " " * 11, "|")
    t.sleep(1)
    print(" " * 16, "-" * 24)
    t.sleep(1)
    print(" " * 16, "|", " " * 20, "|")
    t.sleep(1)

    print(" " * 16, "|", " " * int((20 - b) / 2), x, " " * int((20 - b) / 2 - 1), "|")
    t.sleep(1)
    print(" " * 16, "|", " " * 20, "|")
    t.sleep(1)
    print(" " * 12, "-" * 32)


def menu():
    print()
    for i in range(4):
        if i == 3:
            print(" " * 13, "Happy Happy Birthday To You")
        elif i == 0 or i == 1:
            print(" " * 15, "Happy Birthday To You")
        elif i == 2:
            print(" " * 15, "Happy Birthday", "*", x.upper(), "*", "\n")

        t.sleep(1.8)
        print()


def heart():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("❤️", end=" ")
            else:
                print(" " * 1, end=" ")
        print()

print("\n")
print("#" * 9, "Birthday Wishes For My Friend", "*" + x.upper() + "*", "#" * 9)
t.sleep(1.5)
menu()
cake()
print("" * 14, "Many Many Happy Returns of the Day\n".upper())
t.sleep(2)

x = "Happy, Healthy, Rocking, Fadu Birthday to you my Friend by Sushil Ghanekar!!! "

a = x.split()
for i in a:
    print("\t\t", i.title())
    t.sleep(1)

print(" ")
t.sleep(2)
print(" " * 18, "god bless you".upper())
t.sleep(1)
print(" " * 18, "with beautiful heart".upper())
t.sleep(1)
heart()

