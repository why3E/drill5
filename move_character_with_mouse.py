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


running = True
frame =0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100 , 100 , 100 , 100, 700 , 600)
    character.clip_draw(frame * 100 ,0 , 100 , 100, 500 , 600)
    hand.clip_draw(0 , 0 , 50 , 50 ,640 , 512)

    frame +=1
    frame %=8
    
    delay(0.2)
    update_canvas()

close_canvas()




