import tkinter as tk
import random
import time

#Constants

WIDTH = 640
HEIGHT = 360

PLAYER_SIZE = 30
ENEMY_SIZE = 20
BIG_SIZE = 40

PLAYER_SPEED = 15
ENEMY_SPEED = 3
BIG_SPEED = 1.5

ATTACK_RANGE = 50
ATTACK_DAMAGE = 1

#Variables

alive = True
game_state = "start"

player = None
enemies = None

wave = 1
attack_cooldown = 0

#Window

root = tk.Tk()
root.title("Colosseum")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

#UI

def show_start_screen():
    canvas.delete("all")
    canvas.create_text(WIDTH/2, HEIGHT/2 - 40, text = )