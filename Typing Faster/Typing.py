import pygame
import random
import time

pygame.init()

# Player
player_x = 300

# Menu
count = 0
key_check = False
ground = pygame.Rect(0,300,800,100)
font_game = 'Coiny-Regular.ttf'
text_size = 25
text_menu_size = 20
font = pygame.font.Font(font_game,text_size)
font_1 = pygame.font.Font(font_game,text_menu_size)
text_1 = font_1.render('Hàng phím thứ nhất',True,('black'))
text_2 = font_1.render('Hàng phím thứ hai',True,('black'))
text_3 = font_1.render('Hàng phím thứ ba',True,('black'))
text_4 = font_1.render('Tổng hợp phím',True,('black'))
button_1 = pygame.Rect(50,100,250,50)
button_2 = pygame.Rect(50,200,250,50)
button_3 = pygame.Rect(50,300,250,50)
button_4 = pygame.Rect(350,100,250,50)
button1 = pygame.image.load('button.png')
button2 = pygame.image.load('button.png')
button3 = pygame.image.load('button.png')
button4 = pygame.image.load('button.png')
menu_1,menu_2,menu_3,menu_4 = False,False,False,False
bg = pygame.image.load('bgtyping.jpg')
trollbutton = pygame.image.load('trollbutton.png')
trollbutton_rect = pygame.Rect(700,5,50,50)
trollsound = pygame.mixer.Sound('trollsound.mp3')
bgmenu = pygame.image.load('bgmenu.png')
title_size = 50
title_font = pygame.font.Font(font_game,title_size)
title = title_font.render('Typing Faster',True,('white'))
clock = pygame.time.Clock()
start_time = time.time()
lastest_time = 0
end = False
score = 0

# Menu 1
color = (117, 125, 138)
text_title_1_size = 30
text_size_1 = 40
font_title = pygame.font.Font(font_game,text_title_1_size)
title_1 = font_title.render('Hàng phím thứ nhất',True,('black'))
font_key = pygame.font.Font(font_game,text_size_1)
q = font_key.render('Q',True,('black'))
w = font_key.render('W',True,('black'))
e = font_key.render('E',True,('black'))
r = font_key.render('R',True,('black'))
t = font_key.render('T',True,('black'))
y = font_key.render('Y',True,('black'))
u = font_key.render('U',True,('black'))
i = font_key.render('I',True,('black'))
o = font_key.render('o',True,('black'))
p = font_key.render('p',True,('black'))
Q = pygame.image.load('Q.png')
W = pygame.image.load('W.png')
E = pygame.image.load('E.png')
R = pygame.image.load('R.png')
T = pygame.image.load('T.png')
Y = pygame.image.load('Y.png')
U = pygame.image.load('U.png')
I = pygame.image.load('I.png')
O = pygame.image.load('O.png')
P = pygame.image.load('P.png')
key_ran_1 = ['Q','W','E','R','T','Y','U','I','O','P']
key_spawn = []
key_save = []
pos_key_x = [800]
key_pic = ''

# Menu 2
color = (117, 125, 138)
text_title_2_size = 30
text_size_2 = 40
font_title = pygame.font.Font(font_game,text_title_2_size)
title_2 = font_title.render('Hàng phím thứ hai',True,('black'))



font_key = pygame.font.Font(font_game,text_size_2)
a = font_key.render('A',True,('black'))
s = font_key.render('S',True,('black'))
d = font_key.render('D',True,('black'))
f = font_key.render('F',True,('black'))
g = font_key.render('G',True,('black'))
h = font_key.render('H',True,('black'))
j = font_key.render('J',True,('black'))
k = font_key.render('K',True,('black'))
l = font_key.render('L',True,('black'))
dot = font_key.render(';',True,('black'))
key_ran_2 = ['A','S','D','F','G','H','J','K','L',';']
key_spawn = []
key_save = []
pos_key_x = [800]
A = pygame.image.load('A.png')
S = pygame.image.load('S.png')
D = pygame.image.load('D.png')
F = pygame.image.load('F.png')
G = pygame.image.load('G.png')
H = pygame.image.load('H.png')
J = pygame.image.load('J.png')
K = pygame.image.load('K.png')
L = pygame.image.load('L.png')
Semicolon = pygame.image.load('semicolon.png')
key_pic =''

# Menu 3
color = (117, 125, 138)
text_title_3_size = 30
text_size_3 = 40
font_title = pygame.font.Font(font_game,text_title_3_size)
title_3 = font_title.render('Hàng phím thứ ba',True,('black'))
font_key = pygame.font.Font(font_game,text_size_3)
z = font_key.render('Z',True,('black'))
x = font_key.render('X',True,('black'))
c = font_key.render('C',True,('black'))
v = font_key.render('V',True,('black'))
b = font_key.render('B',True,('black'))
n = font_key.render('N',True,('black'))
m = font_key.render('M',True,('black'))
key_ran_3 = ['Z','X','C','V','B','N','M']
key_spawn = []
key_save = []
pos_key_x = [800]
Z = pygame.image.load('Z.png')
X = pygame.image.load('X.png')
C = pygame.image.load('C.png')
V = pygame.image.load('V.png')
B = pygame.image.load('B.png')
N = pygame.image.load('N.png')
M = pygame.image.load('M.png')
key_pic = ''

# Menu 4
color = (117, 125, 138)
text_title_4_size = 30
text_size_4 = 40
font_title = pygame.font.Font(font_game,text_title_4_size)
title_4 = font_title.render('Tổng hợp các phím',True,('black'))
font_key = pygame.font.Font(font_game,text_size_3)
key_ran_4 = key_ran_1 + key_ran_2 + key_ran_3

# Screen
screen_height = 400
screen_width = 750
window = pygame.display.set_mode((screen_width,screen_height))
run = True
start = False
music = pygame.mixer.Sound('bgmusic.mp3')
music_button = pygame.image.load('music_but_off.png')
Music = False
music_button_rect = pygame.Rect(650,0,50,50)
troll = False
troll_size = 40
font_troll = pygame.font.Font(font_game,troll_size)
trolltitle = font_troll.render('You were rolled!',True,('white'))
endtitle = font_troll.render('End Typing!',True,('white'))
againbut = pygame.image.load('againbutton2.png')
againbut_rect = pygame.Rect(5,5,50,50)
pygame.display.set_caption('Typing Faster')

# Loop
while run:

    # X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Start button
    if start == False:
        window.blit(bgmenu,(0,0))
        window.blit(title,(10,10))
        window.blit(button1,button_1)
        window.blit(text_1,(75,115))
        window.blit(button2,button_2)
        window.blit(text_2,(76,215))
        window.blit(button3,button_3)
        window.blit(text_3,(80,315))
        window.blit(button4,button_4)
        window.blit(text_4,(400,115))
        window.blit(music_button,(650,0))
        window.blit(trollbutton,(700,5))
        if Music == True:
            music.play()
        else:
            music.stop()
        x,y = pygame.mouse.get_pos()
        mouse_box = pygame.Rect(x,y,20,20)
        if mouse_box.colliderect(button_1):
            button1 = pygame.image.load('button2.png')
        else:
            button1 = pygame.image.load('button.png')
        if mouse_box.colliderect(button_2):
            button2 = pygame.image.load('button2.png')
        else:
            button2 = pygame.image.load('button.png')
        if mouse_box.colliderect(button_3):
            button3 = pygame.image.load('button2.png')
        else:
            button3 = pygame.image.load('button.png')
        if mouse_box.colliderect(button_4):
            button4 = pygame.image.load('button2.png')
        else:
            button4 = pygame.image.load('button.png')
        
    

    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        mouse_box = pygame.Rect(x,y,20,20)
        if mouse_box.colliderect(button_1):
            menu_1 = True
            start = True
            start_time = time.time()
        if mouse_box.colliderect(button_2):
            menu_2 = True
            start = True
            start_time = time.time()
        if mouse_box.colliderect(button_3):
            menu_3 = True
            start = True
            start_time = time.time()
        if mouse_box.colliderect(button_4):
            menu_4 = True
            start = True
            start_time = time.time()
        if mouse_box.colliderect(music_button_rect):
            if Music == True:
                Music = False
                music_button = pygame.image.load('music_but_off.png')
            else:
                Music = True
                music_button = pygame.image.load('music_but-on.png')
        if mouse_box.colliderect(trollbutton_rect):
            troll = True
        if mouse_box.colliderect(againbut_rect):
            menu_1 = False
            menu_2 = False
            menu_3 = False
            menu_4 = False
            end = False
            start = False
            if len(key_spawn) > 0:
                key_spawn = []
                key_save = []
                pos_key_x = [800]
                score = 0
    
    # Menu 1
    
    re = 0
    if menu_1 == True:
        window.blit(bg,(0,0))
        window.blit(trollbutton,(700,5))
        window.blit(title_1,(225,25))
        window.blit(againbut,againbut_rect)
        pygame.draw.rect(window,color,(30,165,70,70))
        window.blit(music_button,(650,0))
        lastest_time = time.time() - start_time
        if lastest_time >= 30:
            end = True
        time_text = str(int(30 - lastest_time))
        text_surface = font_title.render(time_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(375,100))
        window.blit(text_surface, text_rect)
        if Music == True:
            music.play()
        else:
            music.stop()
        
        if len(key_spawn) < 10:
            key_ran = random.choice(key_ran_1)
            if len(key_spawn) == 0 and len(key_save) == 0:
                count = 0
            if count  > 0:
                while key_ran == key_save[count-1]:
                    key_ran = random.choice(key_ran_1)
            key_save.append(key_ran)
            if len(key_spawn) == 0:
                key_x = pos_key_x[0]
                key_box = pygame.Rect(pos_key_x[0],175,50,50)
            else:
                key_x = pos_key_x[count-1] + 70
                pos_key_x.append(key_x)
                key_box = pygame.Rect(pos_key_x[count],175,50,50)
            count += 1
            if count == 10:
                count = 9
            key_spawn.append(key_box)

        
        for key_box in key_spawn:
            if key_save[re] == 'Q':
                key_pic = Q
            if key_save[re] == 'W':
                key_pic = W
            if key_save[re] == 'E':
                key_pic = E
            if key_save[re] == 'R':
                key_pic = R
            if key_save[re] == 'T':
                key_pic = T
            if key_save[re] == 'Y':
                key_pic = Y
            if key_save[re] == 'U':
                key_pic = U
            if key_save[re] == 'I':
                key_pic = I
            if key_save[re] == 'O':
                key_pic = O
            if key_save[re] == 'P':
                key_pic = P
            window.blit(key_pic,key_box)
            re += 1

        re = 0
        for key_box in key_spawn:
            if pos_key_x[re] > (40 + (50 * re)):
                key_box.x -= 1
                pos_key_x[re] -= 1
                re += 1


        for key_box in key_spawn:
            key_pre = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                key_check = True
            if event.type == pygame.KEYUP:
                key_check = False
        
            if key_pre[pygame.K_q] and not key_check :
                if key_save[0] == 'Q':
                    key_save.remove('Q')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_w] and not key_check:
                if key_save[0] == 'W':
                    key_save.remove('W')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_e] and not key_check:
                if key_save[0] == 'E':
                    key_save.remove('E')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_r] and not key_check:
                if key_save[0] == 'R':
                    key_save.remove('R')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1
     
            if key_pre[pygame.K_t] and not key_check:
                if key_save[0] == 'T':
                    key_save.remove('T')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_y] and not key_check:
                if key_save[0] == 'Y':
                    key_save.remove('Y')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_u] and not key_check:
                if key_save[0] == 'U':
                    key_save.remove('U')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_i] and not key_check:
                if key_save[0] == 'I':
                    key_save.remove('I')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_o] and not key_check:
                if key_save[0] == 'O':
                    key_save.remove('O')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_p] and not key_check:
                if key_save[0] == 'P':
                    key_save.remove('P')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1
            
            if lastest_time == 30:
                end = True
        
    # Menu 2

    re = 0
    if menu_2 == True:
        window.blit(bg,(0,0))
        window.blit(trollbutton,(700,5))
        window.blit(title_2,(225,25))
        window.blit(againbut,againbut_rect)
        pygame.draw.rect(window,color,(30,165,70,70))
        window.blit(music_button,(650,0))
        lastest_time = time.time() - start_time
        if lastest_time >= 30:
            end = True
        time_text = str(int(30 - lastest_time))
        text_surface = font_title.render(time_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(375,100))
        window.blit(text_surface, text_rect)
        if Music == True:
            music.play()
        else:
            music.stop()
        
        if len(key_spawn) < 10:
            key_ran = random.choice(key_ran_2)
            if len(key_spawn) == 0 and len(key_save) == 0:
                count = 0
            if count  > 0:
                while key_ran == key_save[count-1]:
                    key_ran = random.choice(key_ran_2)
            key_save.append(key_ran)
            if len(key_spawn) == 0:
                key_x = pos_key_x[0]
                key_box = pygame.Rect(pos_key_x[0],175,50,50)
            else:
                key_x = pos_key_x[count-1] + 70
                pos_key_x.append(key_x)
                key_box = pygame.Rect(pos_key_x[count],175,50,50)
            count += 1
            if count == 10:
                count = 9
            key_spawn.append(key_box)

        
        for key_box in key_spawn:
            if key_save[re] == 'A':
                key_pic = A
            if key_save[re] == 'S':
                key_pic = S
            if key_save[re] == 'D':
                key_pic = D
            if key_save[re] == 'F':
                key_pic = F
            if key_save[re] == 'G':
                key_pic = G
            if key_save[re] == 'H':
                key_pic = H
            if key_save[re] == 'J':
                key_pic = J
            if key_save[re] == 'K':
                key_pic = K
            if key_save[re] == 'L':
                key_pic = L
            if key_save[re] == ';':
                key_pic = Semicolon
            window.blit(key_pic,key_box)
            re += 1

        re = 0
        for key_box in key_spawn:
            if pos_key_x[re] > (40 + (50 * re)):
                key_box.x -= 1
                pos_key_x[re] -= 1
                re += 1


        for key_box in key_spawn:
            key_pre = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                key_check = True
            if event.type == pygame.KEYUP:
                key_check = False
        
            if key_pre[pygame.K_a] and not key_check :
                if key_save[0] == 'A':
                    key_save.remove('A')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_s] and not key_check:
                if key_save[0] == 'S':
                    key_save.remove('S')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_d] and not key_check:
                if key_save[0] == 'D':
                    key_save.remove('D')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_f] and not key_check:
                if key_save[0] == 'F':
                    key_save.remove('F')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

     
            if key_pre[pygame.K_g] and not key_check:
                if key_save[0] == 'G':
                    key_save.remove('G')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_h] and not key_check:
                if key_save[0] == 'H':
                    key_save.remove('H')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_j] and not key_check:
                if key_save[0] == 'J':
                    key_save.remove('J')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_k] and not key_check:
                if key_save[0] == 'K':
                    key_save.remove('K')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_l] and not key_check:
                if key_save[0] == 'L':
                    key_save.remove('L')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_SEMICOLON] and not key_check:
                if key_save[0] == ';':
                    key_save.remove(';')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            
            
    # Menu 3

    re = 0
    if menu_3 == True:
        window.blit(bg,(0,0))
        window.blit(trollbutton,(700,5))
        window.blit(title_3,(225,25))
        window.blit(againbut,againbut_rect)
        pygame.draw.rect(window,color,(30,165,70,70))
        window.blit(music_button,(650,0))
        lastest_time = time.time() - start_time
        if lastest_time >= 30:
            end = True
        time_text = str(int(30 - lastest_time))
        text_surface = font_title.render(time_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(375,100))
        window.blit(text_surface, text_rect)
        if Music == True:
            music.play()
        else:
            music.stop()
        
        if len(key_spawn) < 10:
            key_ran = random.choice(key_ran_3)
            if len(key_spawn) == 0 and len(key_save) == 0:
                count = 0
            if count  > 0:
                while key_ran == key_save[count-1]:
                    key_ran = random.choice(key_ran_3)
            key_save.append(key_ran)
            if len(key_spawn) == 0:
                key_x = pos_key_x[0]
                key_box = pygame.Rect(pos_key_x[0],175,50,50)
            else:
                key_x = pos_key_x[count-1] + 70
                pos_key_x.append(key_x)
                key_box = pygame.Rect(pos_key_x[count],175,50,50)
            count += 1
            if count == 10:
                count = 9
            key_spawn.append(key_box)

        
        for key_box in key_spawn:
            if key_save[re] == 'Z':
                key_pic = A
            if key_save[re] == 'S':
                key_pic = S
            if key_save[re] == 'D':
                key_pic = D
            if key_save[re] == 'F':
                key_pic = F
            if key_save[re] == 'G':
                key_pic = G
            if key_save[re] == 'H':
                key_pic = H
            if key_save[re] == 'J':
                key_pic = J
            if key_save[re] == 'K':
                key_pic = K
            if key_save[re] == 'L':
                key_pic = L
            if key_save[re] == ';':
                key_pic = Semicolon 
            if key_save[re] == 'X':
                key_pic = X
            if key_save[re] == 'C':
                key_pic = C
            if key_save[re] == 'V':
                key_pic = V
            if key_save[re] == 'B':
                key_pic = B
            if key_save[re] == 'N':
                key_pic = N
            if key_save[re] == 'M':
                key_pic = M
            window.blit(key_pic,key_box)
            re += 1

        re = 0
        for key_box in key_spawn:
            if pos_key_x[re] > (40 + (50 * re)):
                key_box.x -= 1
                pos_key_x[re] -= 1
                re += 1


        for key_box in key_spawn:
            key_pre = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                key_check = True
            if event.type == pygame.KEYUP:
                key_check = False
        
            if key_pre[pygame.K_z] and not key_check :
                if key_save[0] == 'Z':
                    key_save.remove('Z')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_x] and not key_check:
                if key_save[0] == 'X':
                    key_save.remove('X')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_c] and not key_check:
                if key_save[0] == 'C':
                    key_save.remove('C')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_b] and not key_check:
                if key_save[0] == 'B':
                    key_save.remove('B')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

     
            if key_pre[pygame.K_n] and not key_check:
                if key_save[0] == 'N':
                    key_save.remove('N')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_m] and not key_check:
                if key_save[0] == 'M':
                    key_save.remove('M')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            
            if key_pre[pygame.K_v] and not key_check:
                if key_save[0] == 'V':
                    key_save.remove('V')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


    # Menu 4
    
    re = 0
    if menu_4 == True:
        window.blit(bg,(0,0))
        window.blit(trollbutton,(700,5))
        window.blit(title_4,(225,25))
        window.blit(againbut,againbut_rect)
        pygame.draw.rect(window,color,(30,165,70,70))
        window.blit(music_button,(650,0))
        lastest_time = time.time() - start_time
        if lastest_time >= 30:
            end = True
        time_text = str(int(30 - lastest_time))
        text_surface = font_title.render(time_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(375,100))
        window.blit(text_surface, text_rect)
        if Music == True:
            music.play()
        else:
            music.stop()
        
        if len(key_spawn) < 10:
            key_ran = random.choice(key_ran_4)
            if len(key_spawn) == 0 and len(key_save) == 0:
                count = 0
            if count  > 0:
                while key_ran == key_save[count-1]:
                    key_ran = random.choice(key_ran_4)
            key_save.append(key_ran)
            if len(key_spawn) == 0:
                key_x = pos_key_x[0]
                key_box = pygame.Rect(pos_key_x[0],175,50,50)
            else:
                key_x = pos_key_x[count-1] + 70
                pos_key_x.append(key_x)
                key_box = pygame.Rect(pos_key_x[count],175,50,50)
            count += 1
            if count == 10:
                count = 9
            key_spawn.append(key_box)

        
        for key_box in key_spawn:
            if key_save[re] == 'Z':
                key_pic = Z
            if key_save[re] == 'X':
                key_pic = X
            if key_save[re] == 'C':
                key_pic = C
            if key_save[re] == 'V':
                key_pic = V
            if key_save[re] == 'B':
                key_pic = B
            if key_save[re] == 'N':
                key_pic = N
            if key_save[re] == 'M':
                key_pic = M
            if key_save[re] == 'Q':
                key_pic = Q
            if key_save[re] == 'W':
                key_pic = W
            if key_save[re] == 'E':
                key_pic = E
            if key_save[re] == 'R':
                key_pic = R
            if key_save[re] == 'T':
                key_pic = T
            if key_save[re] == 'Y':
                key_pic = Y
            if key_save[re] == 'U':
                key_pic = U
            if key_save[re] == 'I':
                key_pic = I
            if key_save[re] == 'O':
                key_pic = O
            if key_save[re] == 'P':
                key_pic = P
            if key_save[re] == 'A':
                key_pic = A
            if key_save[re] == 'S':
                key_pic = S
            if key_save[re] == 'D':
                key_pic = D
            if key_save[re] == 'F':
                key_pic = F
            if key_save[re] == 'G':
                key_pic = G
            if key_save[re] == 'H':
                key_pic = H
            if key_save[re] == 'J':
                key_pic = J
            if key_save[re] == 'K':
                key_pic = K
            if key_save[re] == 'L':
                key_pic = L
            if key_save[re] == ';':
                key_pic = Semicolon
            window.blit(key_pic,key_box)
            re += 1

        re = 0
        for key_box in key_spawn:
            if pos_key_x[re] > (40 + (50 * re)):
                key_box.x -= 1
                pos_key_x[re] -= 1
                re += 1


        for key_box in key_spawn:
            key_pre = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                key_check = True
            if event.type == pygame.KEYUP:
                key_check = False
        
            if key_pre[pygame.K_z] and not key_check :
                if key_save[0] == 'Z':
                    key_save.remove('Z')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_x] and not key_check:
                if key_save[0] == 'X':
                    key_save.remove('X')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_c] and not key_check:
                if key_save[0] == 'C':
                    key_save.remove('C')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_b] and not key_check:
                if key_save[0] == 'B':
                    key_save.remove('B')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

     
            if key_pre[pygame.K_n] and not key_check:
                if key_save[0] == 'N':
                    key_save.remove('N')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_m] and not key_check:
                if key_save[0] == 'M':
                    key_save.remove('M')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            
            if key_pre[pygame.K_v] and not key_check:
                if key_save[0] == 'V':
                    key_save.remove('V')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_a] and not key_check :
                if key_save[0] == 'A':
                    key_save.remove('A')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_s] and not key_check:
                if key_save[0] == 'S':
                    key_save.remove('S')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_d] and not key_check:
                if key_save[0] == 'D':
                    key_save.remove('D')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_f] and not key_check:
                if key_save[0] == 'F':
                    key_save.remove('F')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

     
            if key_pre[pygame.K_g] and not key_check:
                if key_save[0] == 'G':
                    key_save.remove('G')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_h] and not key_check:
                if key_save[0] == 'H':
                    key_save.remove('H')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_j] and not key_check:
                if key_save[0] == 'J':
                    key_save.remove('J')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_k] and not key_check:
                if key_save[0] == 'K':
                    key_save.remove('K')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_l] and not key_check:
                if key_save[0] == 'L':
                    key_save.remove('L')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_SEMICOLON] and not key_check:
                if key_save[0] == ';':
                    key_save.remove(';')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_q] and not key_check :
                if key_save[0] == 'Q':
                    key_save.remove('Q')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_w] and not key_check:
                if key_save[0] == 'W':
                    key_save.remove('W')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            if key_pre[pygame.K_e] and not key_check:
                if key_save[0] == 'E':
                    key_save.remove('E')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_r] and not key_check:
                if key_save[0] == 'R':
                    key_save.remove('R')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

     
            if key_pre[pygame.K_t] and not key_check:
                if key_save[0] == 'T':
                    key_save.remove('T')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_y] and not key_check:
                if key_save[0] == 'Y':
                    key_save.remove('Y')      
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_u] and not key_check:
                if key_save[0] == 'U':
                    key_save.remove('U')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_i] and not key_check:
                if key_save[0] == 'I':
                    key_save.remove('I')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_o] and not key_check:
                if key_save[0] == 'O':
                    key_save.remove('O')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1


            if key_pre[pygame.K_p] and not key_check:
                if key_save[0] == 'P':
                    key_save.remove('P')
                    key_spawn.remove(key_box)
                    pos_key_x.remove(pos_key_x[0])
                    score += 1

            
    # I dont know that
    
    if troll == True:
        music.stop()
        window.fill('black')
        window.blit(trolltitle,(210,165))
        trollsound.play()

    if end == True:
        window.fill('black')
        window.blit(endtitle,(260,65))
        ur_score = font_title.render("Your Score: " + str(score),True,('white'))
        window.blit(ur_score,(270,165))
        window.blit(againbut,againbut_rect)
        
    pygame.display.update()