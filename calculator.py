from graphics import *


def main():

    def calculate(numbers, work):

        if len(numbers) % 2 == 0 and len(numbers) != 0:

            if work[0] == "**":
                r = numbers[0] ** numbers[1]
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)

            elif work[0] == "%":
                r = numbers[0] % numbers[1]
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)
            elif work[0] == "+":
                r = numbers[0] + numbers[1]
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)

            elif work[0] == "-":
                r = numbers[0] - numbers[1]
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)

            elif work[0] == "/":
                r = numbers[0] / numbers[1]
                a = str(r)
                c = a.find(".")
                if a[c+1] == "0":
                    r = int(a[0:c])
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)

            elif work[0] == "X":
                r = numbers[0] * numbers[1]
                numbers.pop(0)
                numbers.pop(0)
                numbers.append(r)
                work.pop(0)

    win = GraphWin("Calculator", 600, 600)

    rect = []
    for y in range(100, 600, 100):

        for x in range(0, 600, 150):

            if x == 0 and y == 500:
                rect.append(Rectangle(Point(x, y), Point(x+300, y+100)))
                continue
            if x == 150 and y == 500:
                continue
            rect.append(Rectangle(Point(x, y), Point(x+150, y+100)))

    for i in range(len(rect)):
        rect[i].draw(win)

    buttons = ["AC", "+/-", "%", "/", "7", "8", "9", "X", "4",
               "5", "6", "-", "1", "2", "3", "+", "0", "**", "="]

    butt = []
    for i in range(len(rect)):
        butt.append(Text(rect[i].getCenter(), buttons[i]))

    for i in range(len(butt)):
        butt[i].draw(win)

    input1 = Entry(Point(300, 50), 20)
    input1.setText("0")
    input1.draw(win)
    mess = ""
    key = "a"
    exception = ""
    work = []
    numbers = []

    while True:
        try:
            cor = win.getMouse()

        except GraphicsError:
            break

        try:
            x = cor.getX()
            y = cor.getY()

            if y > 100 and y < 200:

                if x > 0 and x < 150:
                    input1.setText("0")
                    mess = ""
                    work = []
                    numbers = []
                    exception = ""
                    key = "a"

                elif x > 150 and x < 300:

                    if exception == "istisna":
                        numbers[0] = -numbers[0]
                        input1.setText(numbers[0])
                        exception = ""
                        key += "s"

                    elif key[-1] == "s":
                        numbers[0] = -numbers[0]
                        input1.setText(numbers[0])
                        key += "s"

                    elif mess[0] == "-":
                        mess = mess[1:]
                        input1.setText(mess)
                        key += "d"

                    elif mess[0] != "-":
                        mess = "-" + mess
                        input1.setText(mess)
                        key += "d"

                elif x > 300 and x < 450:
                    work.append(butt[2].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""

                elif x > 450 and x < 600:
                    work.append(butt[3].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""

            elif y > 200 and y < 300:

                if x > 0 and x < 150:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[4].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 150 and x < 300:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[5].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 300 and x < 450:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[6].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 450 and x < 600:
                    work.append(butt[7].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""
            elif y > 300 and y < 400:

                if x > 0 and x < 150:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[8].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 150 and x < 300:
                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[9].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 300 and x < 450:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[10].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 450 and x < 600:
                    work.append(butt[11].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""
            elif y > 400 and y < 500:

                if x > 0 and x < 150:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[12].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 150 and x < 300:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[13].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 300 and x < 450:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if key[-1] == "s":
                            mess = str(numbers[0])
                            numbers.pop(0)
                        mess += butt[14].getText()
                        input1.setText(mess)
                        key += "a"

                elif x > 450 and x < 600:
                    work.append(butt[15].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""
            elif y > 500 and y < 600:

                if x > 0 and x < 300:

                    if exception == "istisna":
                        input1.setText("0")
                        work = []
                        numbers = []
                        exception = ""
                    else:
                        if mess == "" and len(work) == 0:
                            input1.setText("0")
                            work = []
                            numbers = []
                        else:
                            if key[-1] == "s":
                                mess = str(numbers[0])
                                numbers.pop(0)
                            mess += butt[16].getText()
                            input1.setText(mess)
                            key += "a"

                elif x > 300 and x < 450:
                    work.append(butt[17].getText())
                    if mess != "":
                        numbers.append(int(mess))
                        mess = ""
                    calculate(numbers, work)
                    input1.setText(numbers[0])
                    key += "b"
                    exception = ""
                elif x > 450 and x < 600:
                    if exception == "istisna":
                        input1.setText(numbers[0])

                    elif key[-1] == "s":
                        input1.setText(numbers[0])
                    else:
                        numbers.append(int(mess))
                        mess = ""
                        calculate(numbers, work)
                        input1.setText(numbers[0])
                        key += "c"
                        exception = "istisna"

            if "bb" in key:
                key = "a"
                input1.setText("0")
                work = []
                numbers = []
                exception = ""

        except:
            input1.setText("0")
            work = []
            numbers = []
            exception = ""
            key = "a"
            continue

    win.close()


main()
