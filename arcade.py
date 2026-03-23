import tkinter as tk
from tkinter import font
import random
import time


WIDTH = 640
HEIGHT = 360

PLAYER_SIZE = 30
ENEMY_SIZE = 20
TEXT_SIZE = 50
BIG_SIZE = 40

PLAYER_SPEED = 15
ENEMY_SPEED = 3
BIG_SPEED = 1.5

#declare variable

alive = True
game_state = "start"

player = None
enemies = []

wave = 1
attack_cooldown = 0


#build window

root = tk.Tk()
root.title("Colosseum")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


<<<<<<< HEAD
#start screen

def show_start_screen():
    canvas.delete("all")
    canvas.create_text(WIDTH//2, HEIGHT//2 - 50, text="DODGER", fill="white", font=("Arial",60,"bold"))
    canvas.create_text(WIDTH//2,HEIGHT//2+50, text= "Press SPACE to Start", fill="white",font=("Arial",30))
=======
player_img = tk.PhotoImage(file="hero.png.png")
enemy_img = tk.PhotoImage(file="skeleton-small.png.png")
big_enemy_img = tk.PhotoImage(file="skeleton-big.png.png")

bg_img = tk.PhotoImage(file="bg.png")
start_img = tk.PhotoImage(file="Start1.png")
dead_img = tk.PhotoImage(file="Sprite-0001.png")

#UI

wave_text = None
hp_bar = None
hp_bg = None

def show_start_screen():
    canvas.delete("all")
    #canvas.create_text(WIDTH//2, HEIGHT//2 - 40, text = "COLOSSEUM", fill = "white", font = ("Arial", 40, "bold"))
    #canvas.create_text(WIDTH/2, HEIGHT/2 + 40, text = "Attack with Left Shift", fill = "white", font = ("Arial", 20))
    canvas.create_image(0, 0, anchor="nw", image = start_img)
>>>>>>> ddfd54d9b1a85b281a453f2a92815dd670efb896

#game over screen

def show_game_over_screen():
    canvas.delete("all")
    canvas.create_text(WIDTH//2,HEIGHT//2-50,text="YOU DIED",fill="#5C0606",font=("Arial",60,"bold"))
    canvas.create_text(WIDTH//2,HEIGHT//2+50,text="Press SPACE to Restart",fill="white",font=("Arial",30))

#game start(kind og)

def start_game(event=None):
    global alive, score, enemies, bigones, bars, warnings
    global player, score_text, game_state, next_horizontal_time, next_vertical_time, vertical_bars, vertical_warnings

    game_state = "running"
    alive = True
    score = 0
    enemies = []
    bigones = []
    bars = []
    warnings = []
    vertical_warnings = []
    vertical_bars = []
    
    now = time.time() * 1000
    next_horizontal_time = now + random.randint(1000,10000)
    next_vertical_time = now + random.randint(1000,10000)

    canvas.delete("all")

    player = create_heart(WIDTH//2, HEIGHT//2, size=25, color="#00FF37")
    score_text = canvas.create_text(70, 30, text="0", fill="white", font=("Arial",24))
    run_game()


#movemenet function
def move_left(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if x1>0:
        canvas.move(player, -20, 0)
def move_right(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if x2 < WIDTH:
        canvas.move(player, 20, 0)
def move_up(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if y1>0:
        canvas.move(player, 0, -20)
def move_down(event):
    x1,y1,x2,y2 = canvas.bbox(player)
    if y2 < HEIGHT:
        canvas.move(player, 0, 20)

#binding buttons
root.bind("a",move_left)
root.bind("d",move_right)
root.bind("w",move_up)
root.bind("s",move_down)
root.bind("<space>", start_game)
#bad guys



def spawn_enemy():
    x = random.randint(0, WIDTH-ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x+ENEMY_SIZE, ENEMY_SIZE, fill = "#FF0000")
    enemies.append(enemy)

def spawn_bigone():
    x = random.randint(0, WIDTH - BIGONE_SIZE)
    enemy = canvas.create_rectangle(x, 0, x + BIGONE_SIZE, BIGONE_SIZE, fill="#8B0000")
    bigones.append(enemy)
    
def trigger_horizontal_event():
    x = random.randint(0, WIDTH - BAR_WIDTH)
    flash_warning(x)

<<<<<<< HEAD
def flash_warning(x, flashes = 6):
    warning = canvas.create_rectangle(x, 0, x + BAR_WIDTH, 20, fill="yellow")
    warnings.append(warning)
=======
    attack_cooldown = 5
>>>>>>> ddfd54d9b1a85b281a453f2a92815dd670efb896

    def animate(count):
        if count == 0:
            if warning in warnings:
                canvas.delete(warning)
                warnings.remove(warning)
            spawn_bar(x)
            return
        current = canvas.itemcget(warning, "fill")
        new = "" if current == "yellow" else "yellow"
        canvas.itemconfig(warning, fill = new)

<<<<<<< HEAD
        root.after(100, lambda: animate(count-1))
    animate(flashes)
=======
    #Attack visual
    circle = canvas.create_oval(
        px - ATTACK_RANGE, py - ATTACK_RANGE,
        px + ATTACK_RANGE, py + ATTACK_RANGE,
        outline="yellow", width=5
    )
    root.after(100, lambda: canvas.delete(circle))
>>>>>>> ddfd54d9b1a85b281a453f2a92815dd670efb896

def spawn_bar(x):
    bar = canvas.create_rectangle(x, 0, x + BAR_WIDTH, 40, fill="#AA0000")
    bars.append(bar)

def trigger_vertical_event():
    count = random.randint(2,3)
    positions = []
    
    while len(positions) < count:
        x = random.randint(0, WIDTH - 40)

        if all(abs(x-p) > 150 for p in positions):
            positions.append(x)
    for x in positions:
        flash_vertical_warning(x)
def flash_vertical_warning(x, flashes=6):
    warning = canvas.create_rectangle(x, 0, x + 20, 40, fill="cyan")
    vertical_warnings.append(warning)
    def animate(count):
        if count == 0:
            if warning in vertical_warnings:
                canvas.delete(warning)
                vertical_warnings.remove(warning)
            spawn_vertical_bar(x)
            return
        current = canvas.itemcget(warning,"fill")
        new = "" if current == "cyan" else "cyan"
        canvas.itemconfig(warning, fill=new)

        root.after(100, lambda: animate(count-1))
    animate(flashes)
def spawn_vertical_bar(x):
    bar = canvas.create_rectangle(x, 0, x + 40, HEIGHT, fill = "#00A2FF")
    vertical_bars.append(bar)

    root.after(1000, lambda: remove_vertical_bar(bar))
def remove_vertical_bar(bar):
    if bar in vertical_bars:
        canvas.delete(bar)
        vertical_bars.remove(bar)

#run game
def run_game():
    global alive, score, game_state, next_horizontal_time, next_vertical_time
    if game_state != "running":
        return
    if not alive:
        game_state = "game over"
        show_game_over_screen()
        return
        
    now = time.time() * 1000
    if now >= next_horizontal_time:
        trigger_horizontal_event()
        next_horizontal_time = now + random.randint(1000,10000)
    if now >= next_vertical_time:
        trigger_vertical_event()
        next_vertical_time = now + random.randint(1000,10000)
    if random.randint(1,5)==1:
        spawn_enemy()
    if random.randint(1,120)==1:
        spawn_bigone()

    for enemy in enemies[:]:
        canvas.move(enemy, 0, 10)
        ex1,ey1,ex2,ey2 = canvas.bbox(enemy)

        if ey2 > HEIGHT:
            score += 1
            canvas.itemconfig(score_text,text=f"{score}")
            canvas.delete(enemy)
            enemies.remove(enemy)
            continue
        if canvas.bbox(enemy) and canvas.bbox(player):
            px1,py1,px2,py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False
    
    for enemy in bigones[:]:
        canvas.move(enemy, 0, 7)
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy)

        if ey2 > HEIGHT:
            score += 5
            canvas.itemconfig(score_text, text=f"{score}")
            canvas.delete(enemy)
            bigones.remove(enemy)
            continue

        if canvas.bbox(enemy) and canvas.bbox(player):
            px1,py1,px2,py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False

    for bar in bars[:]:
        canvas.move(bar, 0, BAR_SPEED)
        bx1, by1, bx2, by2 = canvas.bbox(bar)
        if by2 > HEIGHT:
            canvas.delete(bar)
            bars.remove(bar)
            continue

        px1, py1, px2, py2 = canvas.bbox(player)
        if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
            alive = False
    
    for bar in vertical_bars[:]:
        bx1, by1, bx2, by2 = canvas.bbox(bar)
        px1, py1, px2, py2 = canvas.bbox(player)
        if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
            alive = False

        

    root.after(40, run_game)


#main loop
show_start_screen()
root.mainloop()