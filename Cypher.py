import Constants as Cons
import Utils


def plug_switch(pressed, row_1_plugs, row_2_plugs, row_3_plugs):
    plug_list = Utils.plug_list_master_gen(row_1_plugs, row_2_plugs, row_3_plugs)
    plug = Utils.find_plug(Utils.MetatoLetter(pressed), plug_list)
    return plug.partner_locate(plug_list)


class Rotor():
    def __init__(self, rotorno, rotorpos, core_in):
        self.num = rotorno
        self.pos = rotorpos
        self.core = core_in
        self.wires = Cons.givewires(self.num)

    def RotorPass(self, pressed, direction):
        if direction:
            i = ((pressed + self.pos) + self.core) % 26
            return self.wires[i][1]
        else:
            out = 0
            for i in range(0, 26):
                if pressed == self.wires[i][1]:
                    out = (self.wires[i][0] - self.pos) - self.core
                    while out < 0:
                        out += 26
                    output = out % 26
                    return output

    def ReflCalc(self, pressed, forward):
        if forward:
            i = (pressed + self.pos + self.core) % 26
            return self.wires[i][1]
        else:
            i = ((pressed - self.pos) - self.core) % 26
            return self.wires[i][0]


def Cycle(Rotor_1, Rotor_2, Rotor_3, Refl_Rotor, pressed):
    num = Rotor_1.RotorPass(pressed, True)
    num2 = Rotor_2.RotorPass(num, True)
    num3 = Rotor_3.RotorPass(num2, True)
    num4 = Refl_Rotor.ReflCalc(num3, True)
    num8 = Refl_Rotor.ReflCalc(num4, False)
    num5 = Rotor_3.RotorPass(num8, False)
    num6 = Rotor_2.RotorPass(num5, False)
    num7 = Rotor_1.RotorPass(num6, False)
    if Cons.DEBUG:
        print(pressed)
        print(num)
        print(num2)
        print(num3)
        print(num4)
        print(num8)
        print(num5)
        print(num6)

    return num7


def Cypher(rotors, pressed, Cores, Refl, Refl_Core, rotnum):

    if not pressed == 313:
        ROTOR_OBJ_1 = Rotor(rotnum[2], rotors[2], Cores[2])
        ROTOR_OBJ_2 = Rotor(rotnum[1], rotors[1], Cores[1])
        ROTOR_OBJ_3 = Rotor(rotnum[0], rotors[0], Cores[0])
        REFL_ROTOR = Rotor(4, Refl, Refl_Core)
        out = Cycle(ROTOR_OBJ_1, ROTOR_OBJ_2, ROTOR_OBJ_3, REFL_ROTOR,
                    Cons.BASE_META_NUM.index(pressed))
        return Cons.BASE_META[out]
    else:
        return 313
