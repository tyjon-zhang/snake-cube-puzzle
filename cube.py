
direction = ["x+","x-","y+","y-","z+","z-"]
dire = dict() # match direction with axis change
dire["x+"] = [0,1]
dire["x-"] = [0,-1]
dire["y+"] = [1,1]
dire["y-"] = [1,-1]
dire["z+"] = [2,1]
dire["z-"] = [2,-1]

d = dict() # direction twist of former direction
d['x'] = ["y+","y-","z+","z-"]
d['y'] = ["x+","x-","z+","z-"]
d['z'] = ["x+","x-","y+","y-"]


def printcube(lst):
    space = 0 # space before ■
    vert = 0 # determine the direction of the line
    for i in lst:
        if vert == 0:
            print(2 *space *" ", end ="")
            print(i * "■ ")
            space += i - 1
            vert = 1
            continue
        if vert == 1:
            if i > 2:
                print("/n".join([2*space*" "+"■"]*(i-2)))
            vert = 0

def put(pos, t, cnt):
    if cnt == 1: # first one, dir change
        t += 1
        if len(pos) == 1:
            dd = direction
        elif pos[-1][0] - pos[-2][0] != 0:
            dd = d['x']
        elif pos[-1][1] - pos[-2][1] != 0:
            dd = d['y']
        else:
            dd = d['z']
    else:
        if pos[-1][0] - pos[-2][0] == 1: # x+
            dd = ['x+']
        if pos[-1][0] - pos[-2][0] == -1:
            dd = ['x-']
        if pos[-1][1] - pos[-2][1] == 1:
            dd = ['y+']
        if pos[-1][1] - pos[-2][1] == -1:
            dd = ['y-']
        if pos[-1][2] - pos[-2][2] == 1:
            dd = ['z+']
        if pos[-1][2] - pos[-2][2] == -1:
            dd = ['z-']
    if cnt == arr_cut[t]:
        n_cnt = 1
    else:
        n_cnt = cnt + 1

    for ddd in dd:
        ele = dire[ddd]
        new_pos = pos[-1][:]
        new_pos[ele[0]] += ele[1]
        if new_pos[ele[0]] in [1,2,3] and (new_pos not in pos):
            nnew_pos = pos[:]
            nnew_pos.append(new_pos[:])
            if t == tot-1 and n_cnt == 1:
                return nnew_pos
            else:
                a = put(nnew_pos[:], t, n_cnt)
                if a:
                    return a
                else:
                    continue
        else:
            continue
    return 0

arr = list(map(int,input("please, reshape it into a line, enter the num between each rectangle(separate with space):").split()))
arr_cut = [i - 1 for i in arr]
if sum(arr_cut) != 26:
    print("Wrong Arrey! Not a 3x3x3 cube!")
tot = len(arr)
for i in arr:
    if i < 2:
        print("Wrong Array! There should be no line shorter than 2!")
        quit()
    if i > 3:
        print("Wrong Array! There should be no line larger than 3!")
        quit()
printcube(arr)

ll = put([[1,1,1]], -1, 1)
for i in range(len(ll)):
    dii = ""
    if i != 0:
        if ll[i][0] - ll[i-1][0] == 1: # x+
            dii = 'right ->️'
        if ll[i][0] - ll[i-1][0] == -1: # x-
            dii = 'left <-️'
        if ll[i][1] - ll[i-1][1] == 1: # y+
            dii = 'up ^'
        if ll[i][1] - ll[i-1][1] == -1: # y-
            dii = 'down v'
        if ll[i][2] - ll[i-1][2] == 1: # z+
            dii = 'front(to yourself)'
        if ll[i][2] - ll[i-1][2] == -1: # z-
            dii = 'back (away from yourself️'
    print(ll[i],dii)
