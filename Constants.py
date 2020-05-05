import pygame
import Cypher
import Utils
pygame.init()
#Width of buttons if pressed or not
WID_PRESSED = 29
WID_NOT = 2
#Colors for use in simulation
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIT = (255, 250, 205)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (70, 130, 180)
PURPLE = (218, 112, 214)
NAVY = (0, 0, 128)
PINK = (255, 192, 203)
TURQUOISE = (64, 224, 208)
PEACH = (218, 165, 32)
YELLOW = (255, 255, 0)
OLIVE = (128, 128, 0)
CADET = (95, 158, 160)
MAROON = (128, 0, 0)
CRIMSON = (220, 20, 60)
INDIGO = (75, 0, 130)
GREY = (169, 169, 169)
LIGHT_GREEN = (124, 252, 0)
BROWN = (139, 69, 19)
COL_LIST = [
    GREY, BROWN, LIGHT_GREEN, BLUE, PURPLE, NAVY, PINK, TURQUOISE, PEACH,
    YELLOW, OLIVE, CADET, MAROON, CRIMSON, INDIGO
]


class Plug():
    def __init__(self, letter):
        self.letter = letter
        self.color = WHITE

    def color_step(self):
        if self.color == INDIGO:
            self.color = WHITE
        elif self.color == WHITE:
            self.color = GREY
        else:
            self.color = COL_LIST[COL_LIST.index(self.color) + 1]

    def partner_locate(self, plug_list):
        partner = None
        for i in plug_list:
            if not i == self:
                if not self.color == WHITE:
                    if i.color == self.color:
                        partner = i.letter
        print(partner)
        if not partner == None:
          return Utils.LettertoMeta(str(partner))
        else:
          return Utils.LettertoMeta(str(self.letter))


#What keys to display on buttons & their key versions in the pygame library
row_1 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']


def plug_list_gen():
    row_1_plugs = []
    for i in row_1:
        row_1_plugs += [Plug(i)]
    row_2_plugs = []
    for i in row_2:
        row_2_plugs += [Plug(i)]
    row_3_plugs = []
    for i in row_3:
        row_3_plugs += [Plug(i)]
    return row_1_plugs, row_2_plugs, row_3_plugs


row_1_meta = [
    pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n,
    pygame.K_m
]
row_2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
row_2_meta = [
    pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h,
    pygame.K_j, pygame.K_k, pygame.K_l
]
row_3 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
row_3_meta = [
    pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y,
    pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p
]
#Screen size for pygame window
size = [800, 640]
#Some images to be used in simulation & a font for it as well
up_raw = pygame.image.load('up_arrow.png')
right_raw = pygame.image.load('Right_Arrow.png')
right = pygame.transform.scale(right_raw, (30, 30))
up = pygame.transform.scale(up_raw, (30, 30))
down = pygame.transform.flip(up, False, True)
left = pygame.transform.flip(right, True, False)
font = pygame.font.SysFont("calibri", 60)
cores_font = pygame.font.SysFont("calibri", 30)
pygame.quit()

#A set of debug vars
LIST_GEN = False
DEBUG = False
SKIP = False

#Rotor encryption lists, using Swiss K encoding algorithm

BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE_META = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
]

BASE_META_NUM = [
    97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
    112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122
]

ROTOR1 = [[0, 15], [1, 4], [2, 25], [3, 20], [4, 14], [5, 7], [6, 23], [7, 18],
          [8, 2], [9, 21], [10, 5], [11, 12], [12, 19], [13, 1], [14, 6],
          [15, 11], [16, 17], [17, 8], [18, 13], [19, 16], [20, 9], [21, 22],
          [22, 0], [23, 24], [24, 3], [25, 10]]

ROTOR2 = [[0, 25], [1, 14], [2, 20], [3, 4], [4, 18], [5, 24], [6, 3], [7, 10],
          [8, 5], [9, 22], [10, 15], [11, 2], [12, 8], [13, 16], [14, 23],
          [15, 7], [16, 12], [17, 21], [18, 1], [19, 11], [20, 6], [21, 13],
          [22, 9], [23, 17], [24, 0], [25, 19]]

ROTOR3 = [[0, 4], [1, 7], [2, 17], [3, 21], [4, 23], [5, 6], [6, 0], [7, 14],
          [8, 1], [9, 16], [10, 20], [11, 18], [12, 8], [13, 12], [14, 25],
          [15, 5], [16, 11], [17, 24], [18, 13], [19, 22], [20, 10], [21, 19],
          [22, 15], [23, 3], [24, 9], [25, 2]]

ROTOR4 = [[0, 8], [1, 12], [2, 4], [3, 19], [4, 2], [5, 6], [6, 5], [7, 17],
          [8, 0], [9, 24], [10, 18], [11, 16], [12, 1], [13, 25], [14, 23],
          [15, 22], [16, 11], [17, 7], [18, 10], [19, 3], [20, 21], [21, 20],
          [22, 15], [23, 14], [24, 9], [25, 13]]

ROTOR5 = [[0, 16], [1, 22], [2, 4], [3, 17], [4, 19], [5, 25], [6, 20], [7, 8],
          [8, 14], [9, 0], [10, 18], [11, 3], [12, 5], [13, 6], [14, 7],
          [15, 9], [16, 10], [17, 15], [18, 24], [19, 23], [20, 2], [21, 21],
          [22, 1], [23, 13], [24, 12], [25, 11]]


def givewires(rotnum):
    rotwires = {1: ROTOR1, 2: ROTOR2, 3: ROTOR3, 4: ROTOR4, 5: ROTOR5}
    return rotwires.get(rotnum, "Invalid rotor")
