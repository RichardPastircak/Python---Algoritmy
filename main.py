import tkinter
from tkinter import *
import time
import random

used_hints = None
field_bottom = None
field_right = None
battleships = None
field = [[False for i in range(10)]for j in range(10)]
timedelay = 0
steps = 0
states = 0


window = Tk()
output_text = tkinter.StringVar()
window.title("Battleships")
canvas = None

#new field - generovanie poli, draw hitns
#rest - cyklus na draw hints

'''
def draw_hints(shape,x ,y):
    if (shape == 0):
        canvas.create_oval(25 * x + 25, 25 * y + 25, 25 * x + 50, 25 * y + 50, fill="black")
    elif (shape == 1):
        canvas.create_rectangle(25 * x + 25, 25 * y + 25, 25 * x + 50, 25 * y + 50, fill="black")
    elif shape == 2:
        canvas.create_arc(25 * x + 37.5, 25 * y + 25, 25 * x + 62.5, 25 * y + 50, start=90, extent=180, fill="black")
    elif shape == 3:
        canvas.create_arc(25 * x + 12.5, 25 * y + 25, 25 * x + 37.5, 25 * y + 50, start=270, extent=180, fill="black")
    elif shape == 4:
        canvas.create_arc(25 * x + 25, 25 * y + 37.5, 25 * x + 50, 25 * y + 62.5, extent=180, fill="black")
    else:
        canvas.create_arc(25 * x + 25, 25 * y + 12.5, 25 * x + 50, 25 * y + 37.5, start=180, extent=180, fill="black")

def add_hints(field_bottom, field_right):
    global used_hints
    hints = random.randint(2,4)
    hints_added = 0
    used = [[0 for x in range(hints)] for y in range(3)]

    while hints_added < hints:
        repeat = False;
        x = random.randint(1,8)
        y = random.randint(1,8)

        #solve 0 cases
        if field_bottom[x] == 0 or field_right[y] == 0:
            continue

        #prevents using same cooradinations
        for i in range(0,hints_added):
            if abs(used[0][i] - x) <= 1 and abs(used[1][i] - y) <= 1:
                repeat = True
                break
        if repeat:
            continue

        #draw hints
        shape = random.randint(0,5)
        draw_hints(shape,x ,y)

        used[0][hints_added] = x
        used[1][hints_added] = y
        used[2][hints_added] = shape
        #print(str(used[0][hints_added])+str(used[1][hints_added])+" "+str(field_bottom[x])+str(field_right[y]))
        hints_added += 1

    used_hints = used
'''

def draw_field():
    tmp = len(field_bottom)+1
    for i in range(1, tmp):
        for j in range(1, tmp):
            canvas.create_rectangle(25+ (i-1) * 25, 25 + (j-1)*25, 25 + i * 25, 25 + j * 25, fill="white")
            if i == tmp-1:
                #canvas.create_rectangle(25 + i * 25, 25 + (j-1) * 25, 25 + (i+1) * 25, 25 + j * 25, fill="white", outline="white")
                canvas.create_text(12.5 + 25 * (i + 1), 12.5 + 25 * j + 1, text=field_right[j - 1], font=("Arial", 13))
        canvas.create_text(12.5 + 25 * i, 12.5 + 25 * (j + 1), text=field_bottom[i - 1], font=("Arial", 13))

def generate_field(fieldtype):
    sixfields = [[[3,0,4,0,1,2],[2,4,1,0,0,3]],[[2,2,1,1,3,1],[0,4,0,3,1,2]],[[0,3,1,2,1,3],[0,3,0,3,1,3]],[[3,0,1,4,0,2],[2,2,2,1,2,1]],[[2,0,0,4,1,3],[3,1,3,0,1,2]]]
    tenfields = [[[3,2,1,5,1,4,1,5,0,3],[6,0,1,2,3,3,2,3,3,2]],[[2,2,4,1,7,0,2,4,1,2],[3,0,7,1,2,3,2,2,3,2]],[[3,2,5,1,5,1,3,2,3,0],[3,2,4,1,6,1,4,1,2,1]],[[2,0,6,0,7,0,4,2,1,3],[2,2,3,3,2,4,2,5,1,1]],[[1,6,2,2,1,1,4,3,3,2],[3,4,3,2,1,2,1,5,2,2]]]
    threefields = [[[2,0,2],[2,1,1]],[[2,1,1],[2,0,2]],[[1,1,2],[2,0,2]],[[2,0,2],[1,1,2]]]
    rfield = None

    if fieldtype == 3:
        while (True):
            tmp = random.randint(0, 3)
            newfield1 = threefields[tmp][0]
            newfield2 = threefields[tmp][1]
            if field_bottom != None:
                for i in range(len(field_bottom)):
                    if field_bottom[i] != newfield1[i] and field_right[i] != newfield2[i]:
                        rfield = threefields[tmp]
                        return rfield

            else:
                rfield = threefields[tmp]
                return rfield

    elif fieldtype == 6:
        while(True):
            tmp = random.randint(0,4)
            newfield = sixfields[tmp][0]
            if field_bottom != None:
                for i in range (len(field_bottom)):
                    if field_bottom[i] !=  newfield[i]:
                        rfield = sixfields[tmp]
                        return rfield

            else:
                rfield = sixfields[tmp]
                return rfield
    else:
        while (True):
            tmp = random.randint(0, 4)
            newfield = tenfields[tmp][0]
            if field_bottom != None:
                for i in range(len(field_bottom)):
                    if field_bottom[i] != newfield[i]:
                        rfield = tenfields[tmp]
                        return rfield

            else:
                rfield = tenfields[tmp]
                return rfield

def new_field(output, fieldtype):
    global field_bottom
    global field_right
    global canvas
    global field
    global battleships
    global steps
    global  states

    steps=0
    states=0

    canvas = Canvas(window, height=300, width=300)

    if field_bottom is not None and fieldtype != len(field_bottom):
        field_bottom = None
        field_right = None

    if fieldtype == 3:
        battleships = [2,1,1]

    elif fieldtype == 6:
        battleships = [3,2,2,1,1,1]
    else:
        battleships = [5,4,3,3,2,2,2,1,1,1,1]

    tmp = generate_field(fieldtype)
    field_bottom = tmp[0]
    field_right = tmp[1]

    # draw the field
    draw_field()
    output.set("")
    for i in range(len(field_bottom)):
        for j in range(len(field_bottom)):
            field[i][j] = False

    #add_hints(field_bottom,field_right)
    canvas.grid(row=1, column=0, columnspan=5)

def reset(output):
    global field
    global steps
    global states

    steps= 0
    states = 0

    tmp = len(field_bottom)+1
    for i in range(1, tmp):
        for j in range(1, tmp):

            canvas.create_rectangle(25+ (i-1) * 25, 25 + (j-1)*25, 25 + i * 25, 25 + j * 25, fill="white")
            if i == tmp-1:
                canvas.create_text(12.5 + 25 * (i + 1), 12.5 + 25 * j + 1, text=field_right[j - 1], font=("Arial", 13))

    tmp = tmp -1
    for i in range (tmp):
        for j in range (tmp):
            field[i][j] = False
    output.set("")
    #for i in range (len(used_hints[0])):
    #    draw_hints(used_hints[2][i],used_hints[0][i],used_hints[1][i])

def draw_rest():
    # Heading
    label = Label(window, text="Battleships", font=('Arial', 40, 'bold'), padx=100)
    label.grid(row=0, column=0, columnspan=5)

    # Button times
    threeButton = Button(window, text="3x3", padx=5, pady=5, command=lambda: new_field(output_text, 3))
    threeButton.grid(row=2, column=1)

    sixButton = Button(window, text="6x6", padx=5, pady=5, command= lambda: new_field(output_text,6))
    sixButton.grid(row=2, column=2)

    tenButton = Button(window, text="10x10", padx=5, pady=5, command= lambda: new_field(output_text,10))
    tenButton.grid(row=2, column=3)

    #resetButton = Button(window, text="Reset", padx=5, pady=5, command= lambda: reset(output_text))
    #resetButton.grid(row=2, column=3)

    empty2 = Label()
    empty2.grid(row=3, column=0, columnspan=5)

    dfsButton = Button(window, text="DFS", padx=5, pady=5, command = lambda: dfs_start(output_text))
    dfsButton.grid(row=4, column=1)

    mrvButton = Button(window, text="MRV", padx=5, pady=5, command= lambda: start_bt_mrv(output_text))
    mrvButton.grid(row=4, column=2)

    lcvButton = Button(window, text="LCV", padx=5, pady=5, command= lambda: start_bt_lcv(output_text))
    lcvButton.grid(row=4, column=3)

    empty = Label()
    empty.grid(row=5, column=0, columnspan=5)

    unsolvableButton = Button(window, text="Unsolvable", padx=5, pady=5)
    unsolvableButton.grid(row=6, column=2)

    empty1 = Label()
    empty1.grid(row=7, column=0, columnspan=5)

    # Output Window
    output = Label(textvariable= output_text, font=("Arial", 15), pady=5)
    output.grid(row=8, column=0, columnspan=5)

def draw_rectangle(x,y,color):
    canvas.create_rectangle(25 + x * 25, 25 + y * 25, 25 + (x + 1) * 25, 25 + (y + 1) * 25, fill=color)
    canvas.grid(row=1, column=0, columnspan=5)


def dfs_solved():
    bot = field_bottom.copy()
    right = field_right.copy()
    ships = battleships.copy()

    length = len(bot)


    for i in range (length):
        for j in range (length):
            if field[i][j]:
                # check for  if values around are correct
                bot[i] -= 1
                right[j] -= 1
                if(bot[i] < 0 or right[j] < 0):
                    return False

                # check for diagonal
                if (i - 1 >= 0 and j - 1 >= 0 and field[i-1][j-1]) or (i - 1 >= 0 and j + 1 < length and field[i-1][j+1]) or (i + 1 < length and j - 1 >= 0 and field[i+1][j-1]) or (i + 1 < length and j + 1 < length and field[i+1][j+1]):
                    return False

                #check for vertical and horizontal ships from one place
                if (i+1 < length and field[i+1][j]) or (i - 1 >= 0 and field[i-1][j]):
                    if(j+1 < length and field[i][j+1]) or (i - 1 >= 0 and field[i][j-1]):
                        return False

                elif (j+1 < length and field[i][j+1]) or (i - 1 >= 0 and field[i][j-1]):
                    if (i+1 < length and field[i+1][j]) or (i - 1 >= 0 and field[i-1][j]):
                        return False



    return True

def dfs(x, y, nodes):
    global field
    global steps
    global states

    length = len(field_bottom)
    max_nodes = 10 if length == 6 else 20 if length == 10 else 4

    #already visted
    if field[x][y]:
        return False

    #new visited node
    field[x][y] = True
    draw_rectangle(x,y,"black")
    steps += 1
    window.update()
    time.sleep(timedelay)


    if nodes >= max_nodes:
        is_solved = dfs_solved()
        if (not is_solved):
            draw_rectangle(x,y,"white")
            field[x][y] = False
            states += 1
            return False
        else:
            return True

    tmpy  = y

    for i in range(x,length):
        for j in range(tmpy,length):
            if dfs(i, j, nodes + 1):
                return True
        tmpy = 0



    #this node is not the right one
    field[x][y] = False
    draw_rectangle(x, y, "white")
    return False

def dfs_start(output):
    global  states
    reset(output_text)

    tmp = len(field_bottom)

    starttime = time.time_ns()
    endtime = 0.0
    alltime = 0.0
    for m in range (tmp):
        for n in range (tmp):
            if dfs(m,n, 1):
                states += 1
                endtime = time.time_ns()
                alltime = round((endtime - starttime) * 0.000000001,3)
                output.set("DFS Successed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")
                return

    endtime = time.time_ns()
    alltime = round((endtime - starttime) * 0.000000001, 3)
    output.set("DFS Failed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")


def bt_solve(ships, bot, right):
    global field
    global steps
    global  states

    returned = True

    if(len(ships) > 0):
        ship = ships.pop(0)
    else: return True

    #print("Currently trying to fit ship " + str(ship) + " HORIZONTALY. Ships to fit: " + str(ships))
    #time.sleep(1)

    #try to fit horizontaly
    length = len(bot)
    for i in range(length):
        len_of_ship = 0
        bottom = bot.copy()
        right1 = right.copy()
        j = -1
        while j < length-1:
            j += 1
            #invalid row
            if right[i] < ship:
                break

            #test for valid column + ship already there - yes its correctly like this
            if bottom[j] > 0 and (not field[j][i]):
                # ship below/up, ship right - just right bcs we are going from left to right
                if ((i+1 < length and field[j][i+1]) or (i-1 >= 0 and field[j][i-1]) or (j+1 < length and field[j+1][i]) or (j-1 >= 0 and field[j-1][i])) or \
                        (i+1 < length and j-1 >= 0 and field[j-1][i+1]) or (i+1 < length and j+1 < length and field[j+1][i+1]) or (i-1 >= 0 and j-1 >= 0 and field[j-1][i-1]) or (i-1 >= 0 and j+1 < length and field[j+1][i-1]):
                    bottom = bot.copy()
                    right1 = right.copy()
                    len_of_ship = 0
                    continue

                len_of_ship +=1
                bottom[j] -=1
                right1[i] -=1
            #no continual ship reset the stuff
            elif len_of_ship > 0:
                bottom = bot.copy()
                right1 = right.copy()
                len_of_ship = 0

            #continual place for ship found
            if len_of_ship == ship:
                for k in range (ship):
                    field[j-k][i] = True
                    draw_rectangle(j-k,i,"black")

                steps += 1
                returned = True
                window.update()
                time.sleep(timedelay)

                #no solution was found in further search
                if not bt_solve(ships, bottom.copy(), right1.copy()):
                    returned = False
                    for k in range(ship):
                        field[j - k][i] = False
                        draw_rectangle(j - k, i, "white")

                    j = j - ship + 1
                    window.update()
                    time.sleep(timedelay)

                    #reset variables
                    bottom = bot.copy()
                    right1 = right.copy()
                    len_of_ship = 0
                else:
                    return True


    #no reason to try to fit ship of lengts one also vertically
    if ship == 1:
        if returned:
            states += 1
        ships.insert(0, ship)
        return False

    # try to fit vertical;y
    for i in range(length):
        len_of_ship = 0
        bottom = bot.copy()
        right1 = right.copy()
        j = -1
        while j < length - 1:
            j += 1
            if bot[i] < ship:
                break

            if right1[j] > 0 and (not field[i][j]):
                #nearby on x/y axes then diagonaly
                if ((i+1 < length and field[i+1][j]) or (i-1 >= 0 and field[i-1][j]) or (j-1 >= 0 and field[i][j-1]) or (j+1 < length and field[i][j+1])) or \
                        (i+1 < length and j-1 >= 0 and field[i+1][j-1]) or (i+1 < length and j+1 < length and field[i+1][j+1]) or (i-1 >= 0 and j-1 >= 0 and field[i-1][j-1]) or (i-1 >= 0 and j+1 < length and field[i-1][j+1]):
                    bottom = bot.copy()
                    right1 = right.copy()
                    len_of_ship = 0
                    continue

                len_of_ship +=1
                bottom[i] -=1
                right1[j] -=1
            elif len_of_ship > 0:
                bottom = bot.copy()
                right1 = right.copy()
                len_of_ship = 0

            if len_of_ship == ship:
                for k in range (ship):
                    field[i][j-k] = True
                    draw_rectangle(i,j-k,"black")

                steps += 1
                returned = True
                window.update()
                time.sleep(timedelay)

                    # no solution was found in further search
                if not bt_solve(ships, bottom.copy(), right1.copy()):
                    returned = False
                    for k in range(ship):
                        field[i][j-k] = False
                        draw_rectangle(i, j-k, "white")

                    j = j - ship + 1
                    window.update()
                    time.sleep(timedelay)

                        # reset variables
                    bottom = bot.copy()
                    right1 = right.copy()
                    len_of_ship = 0
                else: return True

    # no solution found
    if returned:
        states += 1
    ships.insert(0, ship)
    return False

def start_bt_mrv(output):
    global states

    reset(output_text)
    ships = battleships.copy()
    ships.sort(reverse=True)

    timestart = time.time_ns()
    succes = bt_solve(ships, field_bottom.copy(), field_right.copy())
    timeend = time.time_ns()
    alltime = round((timeend - timestart) * 0.000000001,3)

    if succes:
        states += 1
        output.set("BT_MRV Succesed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")
    else:
        output.set("BT_MRV Failed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")

def start_bt_lcv(output):
    global states

    reset(output_text)
    ships = battleships.copy()
    ships.sort()

    timestart = time.time_ns()
    succes = bt_solve(ships, field_bottom.copy(), field_right.copy())
    timeend = time.time_ns()
    alltime = round((timeend - timestart) * 0.000000001, 3)

    if succes:
        states += 1
        output.set("BT_LCV Succesed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")
    else:
        output.set("BT_LCV Failed. Steps: " + str(steps) + " ,States: " + str(states)+", Time: " + str(alltime) + " s.")



new_field(output_text, 4)
draw_rest()


window.mainloop()

