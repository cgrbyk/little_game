import os
import time
import keyboard
import random

arena_size = 12
fps = 3.0
arena = []
last_event = ''
current_block_y = 0
current_block_x = 0

def init() -> None:
    global arena
    for i in range(arena_size):
        tmp = []
        for j in range(arena_size):
            tmp.append(' . ')
        arena.append(tmp)
    keyboard.on_press(on_press)

def on_press(event):
    global last_event
    last_event = event.name
    move_block()

def generate_block() -> None:
    global arena
    global arena_size
    global current_block_x
    global current_block_y
    random.seed(time.time())
    position = random.randint(0, arena_size -1)
    arena[0][position] = ' H '
    current_block_x = position
    current_block_y = 0


def draw_arena() -> None:
    global arena
    global arena_size
    os.system('clear')
    for i in range(arena_size):
        for j in range(arena_size):
            if j == 0:
                print('|', end='')
            print(arena[i][j], end='')
            if j == arena_size - 1:
                print('|', end='')
        print(os.linesep)

def fall() -> None:
    global arena
    global arena_size
    global current_block_x
    global current_block_y
    if current_block_y < arena_size - 1 and arena[current_block_y + 1][current_block_x] != ' H ':
        arena[current_block_y][current_block_x] = ' . '
        arena[current_block_y + 1][current_block_x] = ' H '
        current_block_y += 1
    else:
        current_block_y = 0
        generate_block()

def move_block() -> None:
    global last_event
    global arena
    global arena_size
    global current_block_x
    global current_block_y
    if last_event == 'left' and current_block_x > 0 and arena[current_block_y][current_block_x - 1] != ' H ':
        arena[current_block_y][current_block_x] = ' . '
        arena[current_block_y][current_block_x - 1] = ' H '
        current_block_x -= 1
        last_event = ''
    if last_event == 'right' and current_block_x < arena_size and arena[current_block_y][current_block_x + 1] != ' H ':
        arena[current_block_y][current_block_x] = ' . '
        arena[current_block_y][current_block_x + 1] = ' H '
        current_block_x += 1
        last_event = ''
    draw_arena()

def game() -> None:
    global last_event
    global arena_size
    generate_block()
    while True:
        draw_arena()
        fall()

        time.sleep(1.0/fps)
        if last_event == 'space':
            break
    print('Thanks for playing')

if __name__ == '__main__':
    init()
    game()