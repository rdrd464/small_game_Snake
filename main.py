import tkinter as tk

import pygame
import math
import random
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from pygame import mixer
# First show GUL
root = Tk()
root.title("Snake Game")
root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file='ioo.png'))
root.geometry('500x500')
root.configure(background="green")

class Button1:
    """Create A button ,then blit"""
    def __init__(self,text,pos,font,bg="black",feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial",font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text,bg)
    def change_text(self,text,bg="black"):
        """Change text when chick"""
        self.text = self.font.render(text,1,pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text,(0,0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
    def show(self):
        screen.blit(button.surface,(self.x, self.y))
    def click(self,event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x,y):
                    self.change_text(self.feedback,bg="#cc3300")
                    root3 = Tk()
                    root3.title("Snake Game")
                    root3.tk.call('wm', 'iconphoto', root3._w, tk.PhotoImage(file='ioo.png'))
                    root3.geometry('550x460')
                    root3.configure(background="green")
                    # Create Database or connect
                    con = sqlite3.connect('game.db')
                    # Create cursor
                    c = con.cursor()
                    a = c.execute("SELECT * FROM games").fetchall()[-1]

                    # print(records)
                    quary_label = Label(root3, text="Thank you " +str(a[0] ),
                                        font=("Consolas", 30, "bold"),
                                        relief='solid',borderwidth=0,highlightthicknes=0
                                       , background="green", fg="#8B0000")
                    quary_label.grid(padx=0, pady=30)
                    quary1_label = Label(root3, text=" Score Value is = " + str(a[4]),
                                        font=("Consolas", 30, "bold"),
                                        relief='solid', borderwidth=0, highlightthicknes=0
                                        , background="green", fg="#8B0000")
                    quary1_label.grid(padx=50, pady=50)
                    bt1 = Button(root3,text="Close Game",command=root3.destroy
                                 ,bg="#cc3300"
                             ,relief="groove",font=("Courier",19))
                    bt1.grid(padx=20,pady=60,ipady=1,ipadx=10)
                    # commit Changes
                    con.commit()
                    # Close Connection

                    con.close()
                    root3.mainloop()
                    pygame.quit()


def openGame():
    root2.destroy()
    value = 0.02
    # init pygame
    pygame.init()
    global button
    button = Button1("Finish",(200,430),font=30,bg="navy",feedback="you click")
    global screen
    screen = pygame.display.set_mode((480, 480))
    # Background
    background = pygame.image.load('background.png')
    # Background sound
    mixer.music.load('background.mp3')
    mixer.music.play(-1)
    # Title And Icon
    pygame.display.set_caption("Snake Game")
    icon = pygame.image.load('snakeIcon.png')
    pygame.display.set_icon(icon)
    # snake player
    global snake_player
    snake_player = pygame.image.load('snake (2).png')
    global player_s_X
    player_s_X = 270
    global player_s_Y
    player_s_Y = 340
    global snakeX_Change
    snakeX_Change = 0
    # Apple
    apple1 = pygame.image.load('apple.png')
    strawberry = pygame.image.load('strawberry.png')
    banana = pygame.image.load('banana.png')
    red_berry = pygame.image.load('red-berries.png')
    orange = pygame.image.load('orange.png')
    apple2 = pygame.image.load('apple.png')
    strawberry2 = pygame.image.load('strawberry.png')
    banana2 = pygame.image.load('banana.png')
    red_berry2 = pygame.image.load('red-berries.png')
    orange2 = pygame.image.load('orange.png')

    apple3 = pygame.image.load('apple.png')
    strawberry3 = pygame.image.load('strawberry.png')
    banana3 = pygame.image.load('banana.png')
    red_berry3 = pygame.image.load('red-berries.png')
    orange3 = pygame.image.load('orange.png')

    apple4 = pygame.image.load('apple.png')
    strawberry4 = pygame.image.load('strawberry.png')
    banana4 = pygame.image.load('banana.png')
    red_berry4 = pygame.image.load('red-berries.png')
    orange4 = pygame.image.load('orange.png')

    apple5 = pygame.image.load('apple.png')
    strawberry5 = pygame.image.load('strawberry.png')
    banana5 = pygame.image.load('banana.png')
    red_berry5 = pygame.image.load('red-berries.png')
    orange5 = pygame.image.load('orange.png')
    global image_fr
    image_fr = [apple1, strawberry, banana, red_berry, orange, apple2, strawberry2, banana2, red_berry2, orange2
        , apple3, strawberry3, banana3, red_berry3, orange3,
                apple4, strawberry4, banana4, red_berry4, orange4,
                apple5, strawberry5, banana5, red_berry5, orange5]
    global frX
    frX = []
    global frY
    frY = []
    global frX_change
    frX_change = []
    global frY_change
    frY_change = []
    for num in range(len(image_fr)):
        frX.append(random.randint(0, 440))
        frY.append(random.randint(50, 130))
        frX_change.append(0.02)
        frY_change.append(30)
    # Tongue
    global tongue
    tongue = pygame.image.load('tasty.png')
    tonX = 0
    tonY = 340
    tonX_Change = 0
    tonY_change = 10
    tonState = "ready"

    # Font
    global score_val
    score_val = 0
    global overFont
    overFont = pygame.font.Font('freesansbold.ttf', 32)
    global textX
    textX = 10
    global textY
    textY = 10
    score_val = 0
    global over_font
    over_font = pygame.font.Font('freesansbold.ttf', 55)
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            button.click(event)
        button.show()
        # Movement Snake
        inputKey = pygame.key.get_pressed()
        if inputKey[pygame.K_LEFT]:
            player_s_X -= value
        if inputKey[pygame.K_RIGHT]:
            player_s_X += value
        if inputKey[pygame.K_UP]:
            player_s_Y -= value
        if inputKey[pygame.K_DOWN]:
            player_s_Y += value
        if inputKey[pygame.K_SPACE]:
            if tonState == "ready":

                # Get Current x cordinate of tongue
                tonX = player_s_X
                tonY = player_s_Y
                tongueF(tonX, tonY)

        # Check Boundaries
        player_s_X += snakeX_Change
        if player_s_X <= 0:
            player_s_X = 0
        elif player_s_X >= 440:
            player_s_X = 440
        # fruits Movement
        for num in range(len(image_fr)):
            # Game Over
            if frY[num] > 200:
                for j in range(len(image_fr)):
                    frY[j] = 2000
                game_Over()
                break
            frX[num] += frX_change[num]
            if frX[num] <= 0:
                frX_change[num] = 0.04
                frY[num] += frY_change[num]
            elif frX[num] >= 440:
                frX_change[num] = -0.04
                frY[num] += frY_change[num]

            # Collision
            collision = isCollision(frX[num], frY[num], tonX, tonY)
            if collision:
                dingg = mixer.Sound('ding.mp3')
                dingg.play()
                tonY = 330
                tonState = "ready"
                score_val += 1
                frX[num] = random.randint(0, 440)
                frY[num] = random.randint(50, 130)
            fruits(frX[num], frY[num], num)

        # Tongue Move
        if tonY <= 0:
            tonY = 340
            tonState = "ready"
        if tonState == "fire":
            tongueF(tonX, tonY)
            tonY -= tonY_change

        snake(player_s_X, player_s_Y)
        show_Sc(textX, textY)
        pygame.display.update()



def database():
    root.destroy()
    global root2
    global f_name
    global l_name
    global email
    global password
    global score_val
    global root1
    root1 = Tk()
    root1.title("Snake Game")
    root1.tk.call('wm', 'iconphoto', root1._w, tk.PhotoImage(file='ioo.png'))
    root1.geometry('380x300')
    root1.configure(background="green")
    # Create Database or connect
    con = sqlite3.connect('game.db')
    # Create cursor
    c = con.cursor()
    # Create Tabel
    '''
    c.execute("""CREATE TABLE games(
             first_name text,
             last_name text,
             email text,
             password text,
             score integer
             )""")

       '''

    # Create Text Boxes
    text = Label(root1, text="Information Player ",
                 font=("Consolas", 20, "bold"), relief='solid',
                 borderwidth=0,
                 highlightthicknes=0
                 , background="green", fg="#8B0000")
    text.grid(row=0, column=2, pady=10)
    f_name = Entry(root1, width=40)
    f_name.grid(row=1, column=2, padx=20, pady=10)

    l_name = Entry(root1, width=40)
    l_name.grid(row=2, column=2, pady=10)

    email = Entry(root1, width=40)
    email.grid(row=3, column=2, pady=10)

    password = Entry(root1, width=40)
    password.grid(row=4, column=2, pady=10)

    # create Text Box Labels
    f_name_label = Label(root1, text="First Name:",
                         highlightthicknes=0, borderwidth=0, background="green")
    f_name_label.grid(row=1, column=1, pady=10)

    l_name_label = Label(root1, text="Last Name:",
                         highlightthicknes=0, borderwidth=0,
                         background="green")
    l_name_label.grid(row=2, column=1)

    email_label = Label(root1, text="Email:",
                        highlightthicknes=0,
                        borderwidth=0, background="green")
    email_label.grid(row=3, column=1)

    password_label = Label(root1, text="Password:",
                           highlightthicknes=0, borderwidth=0, background="green")
    password_label.grid(row=4, column=1)

    submitt = Button(root1, text="Submit", command=submit,
                     bg="#cc3300", relief="groove", font=("Courier", 19))
    submitt.grid(row=5, column=2, ipadx=10, ipady=5)
    # commit Changes
    con.commit()
    # Close Connection
    con.close()
    root1.mainloop()

def snake(x,y):
    screen.blit(snake_player,(x,y))
def fruits(x,y,num):
    screen.blit(image_fr[num],(x,y))
def tongueF(x,y):
    global tonState
    screen.blit(tongue,(x +16 ,y-17))
def isCollision(frX,frY,tonX,tonY):
    distant = math.sqrt((math.pow(frX-tonX,2))+(math.pow(frY-tonY,2)))
    if distant < 27:
        return True
    else:
        return False
def show_Sc(x,y):
    sc = overFont.render("Score: "+str(score_val),True,(255,255,255))
    screen.blit(sc,(x,y))
def game_Over():

    con = sqlite3.connect('game.db')
    # Create cursor
    c = con.cursor()
    # Update Table

    over = over_font.render("Game Finish", True, (0, 0, 0))
    screen.blit(over, (90, 150))
    a = c.execute("SELECT * FROM games").fetchall()[-1]
    idd = a[5]
    sore = str(score_val)
    c.execute("""UPDATE games
              SET score = :sore
              WHERE id = :idd  """,
              {
                  'sore': sore,
                  'idd': idd
              })

    # commit Changes
    con.commit()
    # Close Connection
    con.close()

def submit():

    global root2
    # Create Database or connect
    con = sqlite3.connect('game.db')
    # Create cursor
    c = con.cursor()
    # Insert Into Table

    c.execute("INSERT INTO games(first_name,last_name,email,password, score) VALUES(:f_name, :l_name, :email, :password,0)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'email': email.get(),
                  'password': password.get(),


                  })
    # commit Changes
    con.commit()
    # Close Connection
    con.close()
    # Clear
    f_name.delete(0,END)
    l_name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    root1.destroy()
    # GUL
    root2 = Tk()
    root2.title("Snake Game")
    root2.tk.call('wm', 'iconphoto', root2._w, tk.PhotoImage(file='ioo.png'))
    root2.geometry('380x300')
    root2.configure(background="green")
    add1 = Label(root2, text="SNAKE GAME !!", font=("Consolas", 20, "bold"), relief='solid', borderwidth=0,
                highlightthicknes=0 , background="green", fg="#8B0000")
    add1.grid(padx=80,pady=50,ipady=10,ipadx=10)
    bt1 = Button(root2, text="Play", command=openGame, bg="#cc3300", relief="groove", font=("Courier", 19))
    bt1.grid(padx=60, pady=60, ipady=4, ipadx=15)


    root2.mainloop()
add = Label(root,text="SNAKE GAME !!",font=("Consolas",20,"bold")
            , relief='solid',borderwidth=0, highlightthicknes=0
            ,background="green",fg="#8B0000")
add.grid(padx=40,pady=50,ipady=10,ipadx=10)
image = ImageTk.PhotoImage(Image.open("s.png"))
la = Label(root,image=image)
la.grid(padx=100,pady=10)
bt = Button(root,text="Create",command=database,bg="#cc3300"
            ,relief="groove",font=("Courier",19))
bt.grid(padx=110,pady=10,ipady=1,ipadx=10)
root.mainloop()