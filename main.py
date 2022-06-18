from datetime import datetime
import os
import time

zero = [
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B'
]
one = [
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B'
]
two = [
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B'
]
tree = [
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B'
]
four = [
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B'
]
five = [
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B'
]
six = [
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B'
]
seven = [
    '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B'
]
eight = [
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B'
]
nine = [
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
    '\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B'
]
sep_b = [
    '\u2B1B',
    '\u2B1B',
    '\u2B1B',
    '\u2B1B',
    '\u2B1B',
    '\u2B1B',
    '\u2B1B'
]
sep_bnw = [
    '\u2B1B',
    '\u2B1C',
    '\u2B1B',
    '\u2B1B',
    '\u2B1B',
    '\u2B1C',
    '\u2B1B'
]
dct = {
    '0': zero,
    '1': one,
    '2': two,
    '3': tree,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    ':': sep_bnw,
    ';': sep_b
}

counter = 0
while True:
    def lights():
        if counter %2 == 0:
            return datetime.now().strftime("%H:%M:%S")
        elif counter %2 == 1:
            return datetime.now().strftime("%H;%M;%S")
    ct = lights()
    clock = [dct[x] for x in ct if x in dct.keys()]
    print(clock[0][0] + clock[1][0] + clock[2][0] + clock[3][0] + clock[4][0] + clock[5][0] + clock[6][0] + clock[7][0])
    print(clock[0][1] + clock[1][1] + clock[2][1] + clock[3][1] + clock[4][1] + clock[5][1] + clock[6][1] + clock[7][1])
    print(clock[0][2] + clock[1][2] + clock[2][2] + clock[3][2] + clock[4][2] + clock[5][2] + clock[6][2] + clock[7][2])
    print(clock[0][3] + clock[1][3] + clock[2][3] + clock[3][3] + clock[4][3] + clock[5][3] + clock[6][3] + clock[7][3])
    print(clock[0][4] + clock[1][4] + clock[2][4] + clock[3][4] + clock[4][4] + clock[5][4] + clock[6][4] + clock[7][4])
    print(clock[0][5] + clock[1][5] + clock[2][5] + clock[3][5] + clock[4][5] + clock[5][5] + clock[6][5] + clock[7][5])
    print(clock[0][6] + clock[1][6] + clock[2][6] + clock[3][6] + clock[4][6] + clock[5][6] + clock[6][6] + clock[7][6])
    counter += 1
    time.sleep(1)
    os.system('clear')
