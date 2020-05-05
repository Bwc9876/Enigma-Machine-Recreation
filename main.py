import pygame
import Utils
import Constants as Cons
from Cypher import Cypher, plug_switch

if Cons.LIST_GEN:
    Utils.listgen("QWERTZUIOASDFGHJKPYXCVBNML")
pygame.init()
rotors = [1, 1, 1]
rotors_cools = [0, 0, 0]
rotor_cores = [0, 0, 0]
rotor_cores_cools = [0, 0, 0]
reflector_core_cool = 0
reflector_core = 0
reflector = 1
plug_allow = True
reflector_cool = 0
rotnum = [3, 2, 1]
rotnumcool = [0, 0, 0]
row_1_plugs, row_2_plugs, row_3_plugs = Cons.plug_list_gen()
screen = pygame.display.set_mode(Cons.size)
plugboard = []
plugshow = False
done = False
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
font = pygame.font.SysFont("calibri", 60)
cores_font = pygame.font.SysFont("calibri", 45)
while not done:
    #Resets some variable to prevent repeating actions due to them being the same

    mouse_x = 0
    mouse_y = 0
    pressed = 0

    #-------------------------------------------------

    #Initializes pygame's clock and tick speed (in this case 10), aswell as handles event logic

    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed_raw = event.key
            if Cons.SKIP:
                if not pressed_raw == 313:
                    rotors = Utils.rotorcheck(rotors)
                pressed = pressed_raw
            else:
                if not pressed_raw == 313:
                    if not Utils.rotnumcheck(rotnum):
                        pressed = 0
                    elif not plugshow:
                        if Utils.plugcheck(row_1_plugs, row_2_plugs,
                                           row_3_plugs):
                            rotors = Utils.rotorcheck(rotors)
                            pressed_raw = plug_switch(pressed_raw, row_1_plugs,
                                                      row_2_plugs, row_3_plugs)
                            pressed = Cypher(rotors, pressed_raw, rotor_cores,
                                             reflector, reflector_core, rotnum)
                            pressed = plug_switch(pressed, row_1_plugs,
                                                  row_2_plugs, row_3_plugs)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
    screen.fill(Cons.BLACK)

    #-------------------------------------------------

    #Renders keys and determines if pressed
    if not plugshow:
        for x in range(0, 7):
            WID, COL = Utils.presscheck(1, pressed, x)
            cent = 200 + x * 70
            pygame.draw.circle(screen, COL, [cent, 550], 30, WID)
            text = font.render(Cons.row_1[x], True, Cons.GREEN)
            screen.blit(text, (cent - 16, 550 - 20))
        for x in range(0, 9):
            WID, COL = Utils.presscheck(2, pressed, x)
            cent = 130 + x * 70
            pygame.draw.circle(screen, COL, [cent, 470], 30, WID)
            text = font.render(Cons.row_2[x], True, Cons.GREEN)
            screen.blit(text, (cent - 16, 470 - 20))
        for x in range(0, 10):
            WID, COL = Utils.presscheck(3, pressed, x)
            cent = 80 + x * 70
            pygame.draw.circle(screen, COL, [cent, 390], 30, WID)
            text = font.render(Cons.row_3[x], True, Cons.GREEN)
            if Cons.row_3[x] == "I":
                screen.blit(text, (cent - 7, 390 - 20))
            else:
                screen.blit(text, (cent - 16, 390 - 20))

#-------------------------------------------------

#Renders Rotors and determines if the user has changed them via the arrows

        for x in range(0, 3):
            pos = x * 100 + 280
            mine = Utils.digitcheck(rotors[x])
            if mine == 2:
                new_pos = pos - 8
            else:
                new_pos = pos
            up_temp = screen.blit(Cons.up, (pos - 5, 100))
            down_temp = screen.blit(Cons.down, (pos - 5, 200))
            if rotors_cools[x] > 10:
                if up_temp.collidepoint(mouse_x, mouse_y) and rotors[x] < 26:
                    rotors[x] += 1
                if down_temp.collidepoint(mouse_x, mouse_y) and rotors[x] > 1:
                    rotors[x] -= 1
            rotors_cools[x] += 1
            text = font.render(str(rotors[x]), True, Cons.GREEN)
            screen.blit(text, (pos, 150))
        for x in range(0, 3):
            if not Utils.rotnumcheck(rotnum):
                COL = Cons.RED
            else:
                COL = Cons.NAVY
            pos = x * 100 + 280
            left_temp = screen.blit(Cons.left, (pos - 30, 250))
            right_temp = screen.blit(Cons.right, (pos + 30, 250))
            if rotnumcool[x] > 10:
                if right_temp.collidepoint(mouse_x, mouse_y) and rotnum[x] < 3:
                    rotnum[x] += 1
                if left_temp.collidepoint(mouse_x, mouse_y) and rotnum[x] > 1:
                    rotnum[x] -= 1
            rotnumcool[x] += 1
            text = font.render(str(rotnum[x]), True, COL)
            screen.blit(text, (pos, 250))
            stattext = font.render(Utils.stat(x), True, Cons.WHITE)
            screen.blit(stattext, (pos, 50))
        for x in range(0, 3):
            pos = x * 100 + 230
            mine = Utils.digitcheck(rotor_cores[x])
            if mine == 2:
                new_pos = pos - 8
            else:
                new_pos = pos
            up_temp = screen.blit(Cons.up, (pos - 5, 120))
            down_temp = screen.blit(Cons.down, (pos - 5, 180))
            if rotor_cores_cools[x] > 10:
                if up_temp.collidepoint(mouse_x,
                                        mouse_y) and rotor_cores[x] < 25:
                    rotor_cores[x] += 1
                if down_temp.collidepoint(mouse_x,
                                          mouse_y) and rotor_cores[x] > 0:
                    rotor_cores[x] -= 1
            rotor_cores_cools[x] += 1
            text = cores_font.render(str(rotor_cores[x]), True, Cons.BLUE)
            screen.blit(text, (new_pos + 2, 150))

        mine = Utils.digitcheck(reflector)
        pos = 100
        if mine == 2:
            new_pos = pos - 8
        else:
            new_pos = pos
        up_temp = screen.blit(Cons.up, (pos - 5, 100))
        down_temp = screen.blit(Cons.down, (pos - 5, 200))
        if reflector_cool > 10:
            if up_temp.collidepoint(mouse_x, mouse_y) and reflector < 26:
                reflector += 1
            if down_temp.collidepoint(mouse_x, mouse_y) and reflector > 1:
                reflector -= 1
        reflector_cool += 1
        text = font.render(str(reflector), True, Cons.PURPLE)
        screen.blit(text, (new_pos, 150))

        pos = 50
        mine = Utils.digitcheck(reflector_core)
        if mine == 2:
            new_pos = pos - 8
        else:
            new_pos = pos
        up_temp = screen.blit(Cons.up, (pos - 5, 120))
        down_temp = screen.blit(Cons.down, (pos - 5, 180))
        if reflector_core_cool > 10:
            if up_temp.collidepoint(mouse_x, mouse_y) and reflector_core < 25:
                reflector_core += 1
            if down_temp.collidepoint(mouse_x, mouse_y) and reflector_core > 0:
                reflector_core -= 1
        reflector_core_cool += 1
        text = cores_font.render(str(reflector_core), True, Cons.BLUE)
        screen.blit(text, (new_pos + 2, 150))
        down_temp = screen.blit(Cons.down, (400, 600))
        if down_temp.collidepoint(mouse_x, mouse_y):
            plugshow = True
    else:
        if Utils.plugcheck(row_1_plugs, row_2_plugs, row_3_plugs):
            down_temp = screen.blit(Cons.up, (400, 50))
        if down_temp.collidepoint(mouse_x, mouse_y):
            plugshow = False
        for x in range(0, 7):
            cent = 200 + x * 70
            circ = pygame.draw.circle(screen, row_1_plugs[x].color,
                                      [cent, 550], 30, 29)
            if circ.collidepoint(mouse_x, mouse_y):
                for i in row_1_plugs:
                    if i.letter == Cons.row_1[x]:
                        i.color_step()
            text = font.render(Cons.row_1[x], True, Cons.GREEN)
            screen.blit(text, (cent - 16, 550 - 20))
        for x in range(0, 9):
            cent = 130 + x * 70
            circ = pygame.draw.circle(screen, row_2_plugs[x].color,
                                      [cent, 470], 30, 29)
            if circ.collidepoint(mouse_x, mouse_y):
                for i in row_2_plugs:
                    if i.letter == Cons.row_2[x]:
                        i.color_step()
            text = font.render(Cons.row_2[x], True, Cons.GREEN)
            screen.blit(text, (cent - 16, 470 - 20))
        for x in range(0, 10):
            cent = 80 + x * 70
            circ = pygame.draw.circle(screen, row_3_plugs[x].color,
                                      [cent, 390], 30, 29)
            if circ.collidepoint(mouse_x, mouse_y):
                for i in row_3_plugs:
                    if i.letter == Cons.row_3[x]:
                        i.color_step()
            text = font.render(Cons.row_3[x], True, Cons.GREEN)
            if Cons.row_3[x] == "I":
                screen.blit(text, (cent - 7, 390 - 20))
            else:
                screen.blit(text, (cent - 16, 390 - 20))

    #-------------------------------------------------

    #Actually shows everything I just did, to the user

    pygame.display.flip()

#-------------------------------------------------

#Quits after the while not done loop (Impossible to reach)

pygame.quit()

#-------------------------------------------------
