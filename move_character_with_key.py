from pico2d import *

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('ThePilot1.png')

def handle_events():
    global moving, dirX, dirY, state, idle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False

        elif event.type == SDL_KEYDOWN: #   누름
            idle = False

            if event.key == SDLK_RIGHT:
                dirX += 1
                state = 1

            elif event.key == SDLK_LEFT:
                dirX -= 1
                state = 2

            elif event.key == SDLK_UP:
                dirY += 1
                state = 3

            elif event.key == SDLK_DOWN:
                dirY -= 1
                state = 4

            elif event.key == SDLK_ESCAPE:  #   ESC
                moving = False

        elif event.type == SDL_KEYUP:  #   뗌
            idle = True

            if event.key == SDLK_RIGHT:
                dirX -= 1

            elif event.key == SDLK_LEFT:
                dirX += 1

            elif event.key == SDLK_UP:
                dirY -= 1

            elif event.key == SDLK_DOWN:
                dirY += 1

moving = True
x = 800 // 2
y = 90

idle = True
dirX, dirY = 0, 0
state = 4
frame = 0

def idleDown():
    global x, y, frame
    
    character.clip_draw(frame * 25, 828, 25, 24, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    #x += dir * 5
    delay(0.2)

def moveRight():
    global x, y, frame

    #character.clip_draw(frame * 25, )

def moveLeft():
    pass

def moveUp():
    pass

def moveDown():
    pass

while moving:
    clear_canvas()
    bg.draw(400, 100)

    if idle:  #   아이들 상태
        if state == 1:
            pass

        elif state == 2:
            pass

        elif state == 3:
            pass
        
        elif state == 4:
            idleDown()

    elif state == 1:    #   우
        pass

    elif state == 2:    #   좌
        pass

    elif state == 3:    #   상
        pass

    elif state == 4:    #   하
        pass

close_canvas()