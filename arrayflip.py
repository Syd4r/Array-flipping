numamount = 1
actualnumber = 1
width = int(input("Width:"))
length = int(input("Length:"))
area = length * width
for i in range(area + 1):
    globals()["word" + str(i)] = i
def actualprint1():
    global numamount
    global width
    global length
    numamount = 1
    for i in range (length):
        for i in range (width-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount += 1
        print(globals()["word" + str(numamount)])
        numamount += 1
def actualprint2():
    global numamount
    global width
    global length
    numamount = area - (width - 1)
    for i in range (width):
        for i in range (length-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount -= width
        print(globals()["word" + str(numamount)])
        numamount += (area - (width - 1))
def actualprint3():
    global numamount
    global width
    global length
    numamount = width
    for i in range (width):
        for i in range (length-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount += width
        print(globals()["word" + str(numamount)])
        numamount -= (area - (width - 1))
def actualprint4():
    global numamount
    global width
    global length
    numamount = area - width + 1
    for i in range (length):
        for i in range (width-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount += 1
        print(globals()["word" + str(numamount)])
        numamount -= (2 * width) - 1
def actualprint5():
    global numamount
    global width
    global length
    numamount = width
    for i in range (length):
        for i in range (width-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount -= 1
        print(globals()["word" + str(numamount)])
        numamount += (2 * width) - 1
def actualprint6():
    global numamount
    global width
    global length
    numamount = area
    for i in range (length):
        for i in range (width-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount -= 1
        print(globals()["word" + str(numamount)])
        numamount -= 1
def actualprint7():
    global numamount
    global width
    global length
    numamount = area
    for i in range (width):
        for i in range (length-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount -= width
        print(globals()["word" + str(numamount)])
        numamount += area - (width + 1)
def actualprint8():
    global numamount
    global width
    global length
    numamount = 1
    for i in range (width):
        for i in range (length-1):
            if globals()["word" + str(numamount)] < 10:
                print(globals()["word" + str(numamount)], end = '   ')
            elif globals()["word" + str(numamount)] < 100:
                print(globals()["word" + str(numamount)], end = '  ')
            else:
                print(globals()["word" + str(numamount)], end = ' ')
            numamount += width
        print(globals()["word" + str(numamount)])
        numamount -= area - (width + 1)
actualprint1()
while True:
    action = input("Rotate? R, L, X, Y: ")
    while True:
        if action == ("O"):
            actualprint1()
            action = input("Rotate? R, L, X, Y: ")
        if action == ("R"):
            actualprint2()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("XY")
            elif action == ("L"):
                action = ("O")
            elif action == ("X"):
                action = ("YL")
            elif action == ("Y"):
                action = ("XL")
        if action == ("L"):
            actualprint3()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("O")
            elif action == ("L"):
                action = ("XY")
            elif action == ("X"):
                action = ("XL")
            elif action == ("Y"):
                action = ("YL")
        if action == ("X"):
            actualprint5()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("XL")
            elif action == ("L"):
                action = ("YL")
            elif action == ("X"):
                action = ("O")
            elif action == ("Y"):
                action = ("XY")
        if action == ("Y"):
            actualprint4()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("YL")
            elif action == ("L"):
                action = ("XL")
            elif action == ("X"):
                action = ("XY")
            elif action == ("Y"):
                action = ("O")
        if action == ("XY"):
            actualprint6()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("L")
            elif action == ("L"):
                action = ("R")
            elif action == ("X"):
                action = ("Y")
            elif action == ("Y"):
                action = ("X")
        if action == ("YL"):
            actualprint8()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("Y")
            elif action == ("L"):
                action = ("X")
            elif action == ("X"):
                action = ("R")
            elif action == ("Y"):
                action = ("L")
        if action == ("XL"):
            actualprint7()
            action = input("R, L, X, Y: ")
            if action == ("R"):
                action = ("X")
            elif action == ("L"):
                action = ("Y")
            elif action == ("X"):
                action = ("L")
            elif action == ("Y"):
                action = ("R")