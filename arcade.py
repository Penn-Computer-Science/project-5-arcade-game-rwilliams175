import tkinter as tk
import random
import time

#Constants

WIDTH = 640
HEIGHT = 360

PLAYER_SPEED = 12
ENEMY_SPEED = 3
BIG_SPEED = 1.5

ATTACK_RANGE = 50
ATTACK_DAMAGE = 1

MAX_HP = 100


#Variables

alive = True
game_state = "start"

player = None
enemies = []

wave = 1
attack_cooldown = 0
player_hp = MAX_HP




#Window

root = tk.Tk()
root.title("Colosseum")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

#IMGS

player_img = tk.PhotoImage(file="player.png")
enemy_img = tk.PhotoImage(file="enemy.png")
big_enemy_img = tk.PhotoImage(file="big_enemy.png")

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
    #canvas.create_text(WIDTH/2, HEIGHT/2 + 40, text = "Press Space to Start", fill = "white", font = ("Arial", 20))
    canvas.create_image(0, 0, anchor="nw", image = start_img)

def show_game_over():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image = dead_img)


#Start game 

def start_game(event=None):
    global alive, enemies, player, wave, game_state, player_hp
    global wave_text, hp_bar, hp_bg

    if game_state == "running":
        return

    alive = True
    game_state = "running"
    wave = 1
    enemies = []
    player_hp = MAX_HP

    canvas.delete("all")

    # background
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    # player
    player = canvas.create_image(WIDTH//2, HEIGHT//2, image=player_img)

    # UI
    wave_text = canvas.create_text(80, 20, text=f"Wave: {wave}",
                                   fill="white", font=("Arial", 16))

    hp_bg = canvas.create_rectangle(10, 40, 210, 60, fill="gray")
    hp_bar = canvas.create_rectangle(10, 40, 210, 60, fill="green")

    spawn_wave()
    run_game()
#Movement

def move_left(event):
    if game_state != "running": return
    canvas.move(player, -PLAYER_SPEED, 0)

def move_right(event):
    if game_state != "running": return
    canvas.move(player, PLAYER_SPEED, 0)

def move_up(event):
    if game_state != "running": return
    canvas.move(player, 0, -PLAYER_SPEED)

def move_down(event):
    if game_state != "running": return
    canvas.move(player, 0, PLAYER_SPEED)


#Attacks 

def attack(event=None):
    global attack_cooldown

    if game_state != "running": return
    if attack_cooldown > 0:
        return

    attack_cooldown = 10

    px1, py1, px2, py2 = canvas.bbox(player)
    px = (px1 + px2) / 2
    py = (py1 + py2) / 2

    #Attack visual
    circle = canvas.create_oval(
        px - ATTACK_RANGE, py - ATTACK_RANGE,
        px + ATTACK_RANGE, py + ATTACK_RANGE,
        outline="yellow", width=2
    )
    root.after(100, lambda: canvas.delete(circle))

    for enemy in enemies[:]:
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy["id"])
        ex = (ex1 + ex2) / 2
        ey = (ey1 + ey2) / 2

        dist = ((px - ex)**2 + (py - ey)**2)**0.5

        if dist < ATTACK_RANGE:
            enemy["hp"] -= ATTACK_DAMAGE

            if enemy["hp"] <= 0:
                canvas.delete(enemy["id"])
                enemies.remove(enemy)

#Enemies

def spawn_enemy(type="small"):
    if type == "small":
        speed = ENEMY_SPEED
        hp = 1
        sprite = enemy_img
    else:
        speed = BIG_SPEED
        hp = 5
        sprite = big_enemy_img

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    enemy_id = canvas.create_image(x, y, image=sprite)

    enemies.append({
        "id": enemy_id,
        "speed": speed,
        "hp": hp,
        "sprite": sprite
    })

#Wave

def spawn_wave():
    global wave

    for _ in range(wave * 3):
        spawn_enemy("small")

    for _ in range(max(0, wave // 3)):
        spawn_enemy("big")

    canvas.itemconfig(wave_text, text=f"Wave: {wave}")
#Enemy Movement

def move_enemies():
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy["id"])
        px1, py1, px2, py2 = canvas.bbox(player)

        ex = (ex1 + ex2) / 2
        ey = (ey1 + ey2) / 2
        px = (px1 + px2) / 2
        py = (py1 + py2) / 2

        dx = px - ex
        dy = py - ey

        dist = max((dx**2 + dy**2)**0.5, 0.001)

        canvas.move(
            enemy["id"],
            (dx / dist) * enemy["speed"],
            (dy / dist) * enemy["speed"]
        )

#Collision

def check_collisions():
    global player_hp, alive

    for enemy in enemies:
        if canvas.bbox(enemy["id"]) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy["id"])
            px1, py1, px2, py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                player_hp -= 1

    if player_hp <= 0:
        alive = False

#HP Bar

def update_hp_bar():
    ratio = player_hp / MAX_HP
    canvas.coords(hp_bar, 10, 40, 10 + 200 * ratio, 60)

#Game loop

def run_game():
    global alive, game_state, wave, attack_cooldown

    if game_state != "running":
        return

    if not alive:
        game_state = "game over"
        show_game_over()
        return

    move_enemies()
    check_collisions()
    update_hp_bar()

    if attack_cooldown > 0:
        attack_cooldown -= 1

    if len(enemies) == 0:
        wave += 1
        spawn_wave()

    root.after(40, run_game)

#Binds

root.bind("a", move_left)
root.bind("d", move_right)
root.bind("w", move_up)
root.bind("s", move_down)
root.bind("<space>", start_game)
root.bind("<Shift_L>", attack)

#Actually Start

show_start_screen()
root.mainloop()