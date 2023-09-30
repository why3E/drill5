from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_line():
    global frame,x1,x2,y1,y2


    for i in range(0, 100+1, 4):
        frame = frame % 8

        t = i / 100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(frame * 100 , 0 , 100 , 100, x , y)
        hand.clip_draw(0 , 0 , 50 , 50 , x2 , y2)
        update_canvas()
        frame +=1
        delay(0.1)
    


running = True
frame =0

x1,y1 = random.randint(50, 900),random.randint(50, 800)
x2,y2 = random.randint(50, 900),random.randint(50, 800)

while running:
    clear_canvas()

    draw_line()
    delay(1.0)
    handle_events()


close_canvas()




