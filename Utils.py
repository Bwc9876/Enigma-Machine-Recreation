import Constants as Cons


def rotorcheck(rotors_in):
    rotors = rotors_in
    rotors[2] += 1
    if rotors[2] == 27:
        rotors[2] = 1
        rotors[1] += 1
        if rotors[1] == 27:
            rotors[1] = 1
            rotors[0] += 1
            if rotors[0] == 27:
                rotors[0] = 1
                rotors[1] = 1
                rotors[2] = 1
    return rotors


def presscheck(rownum, pressed, x):
    if rownum == 2:
        if pressed == Cons.row_2_meta[x]:
            WID = 29
            COL = Cons.LIT
        else:
            WID = 2
            COL = Cons.WHITE
    elif rownum == 1:
        if pressed == Cons.row_1_meta[x]:
            WID = 29
            COL = Cons.LIT
        else:
            WID = 2
            COL = Cons.WHITE
    elif rownum == 3:
        if pressed == Cons.row_3_meta[x]:
            WID = 29
            COL = Cons.LIT
        else:
            WID = 2
            COL = Cons.WHITE
    return WID, COL


def listgen(toencode):
    iter = 0
    print("rotorNUM = [", sep=' ', end='', flush=True)
    for i in toencode:
        print(f" [{iter}, {Cons.BASE.index(i)}],", sep=' ', end='', flush=True)
        iter += 1
    print("]", sep=' ', end='', flush=True)


def MetatoLetter(meta):
    pos = Cons.BASE_META_NUM.index(meta)
    return Cons.BASE[pos]


def LettertoMeta(letter):
    pos = Cons.BASE.index(letter)
    return Cons.BASE_META[pos]


def LetterListToMetaList(li):
    print("newlist = [", sep=' ', end='', flush=True)
    for i in li:
        print(f" pygame.K_{i.lower()},", sep=' ', end='', flush=True)
    print("]", sep=' ', end='', flush=True)


def dylist(list):
    for i in list:
        print(f" {i},", sep=' ', end='', flush=True)


def rotnumcheck(rotnums):
    return len(set(rotnums)) == len(rotnums)


def listcompat(in_list):
    out_list = []
    for i in in_list:
        out_list += [i - 1]
    return out_list


def digitcheck(i):
    return int(str(i).__len__())


def CycleCheck(i):
    if i > 25:
        return i - 26
    else:
        return i


def stat(num):
    if num == 0:
        return "III"
    elif num == 1:
        return "II"
    else:
        return "I"


def plugcheck(row_1_plugs, row_2_plugs, row_3_plugs):
    master = []
    testy = []
    colors = []
    for i in Cons.COL_LIST:
        colors += [0]
    for i in row_1_plugs:
        master += [i]
    for i in row_2_plugs:
        master += [i]
    for i in row_3_plugs:
        master += [i]
    for i in master:
        if not i.color == Cons.WHITE:
            colors[Cons.COL_LIST.index(i.color)] += 1
    iy = True
    for i in colors:
        if Cons.DEBUG:
            print(i)
        if i > 2:
            iy = False
        else:
            pass
    return iy


def plug_list_master_gen(row_1, row_2, row_3):
    master = []
    for i in row_1:
        master += [i]
    for i in row_2:
        master += [i]
    for i in row_3:
        master += [i]
    return master


def find_plug(letter, plug_list):
    out = 0
    for i in plug_list:
        if i.letter == letter:
            out = i
    return out
