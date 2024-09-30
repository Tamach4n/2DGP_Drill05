from pico2d import *

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('ThePilot1.png')

def handle_events():
    global moving, dirX, dirY, state, idle, frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False

        #   누름
        elif event.type == SDL_KEYDOWN: 
            idle = False

            if event.key == SDLK_RIGHT:
                dirX += 1
                dirY = 0
                state = 1

            elif event.key == SDLK_LEFT:
                dirX -= 1
                dirY = 0
                state = 2

            elif event.key == SDLK_UP:
                dirX = 0
                dirY += 1
                state = 3

            elif event.key == SDLK_DOWN:
                dirX = 0
                dirY -= 1
                state = 4

            elif event.key == SDLK_ESCAPE:  #   ESC
                moving = False

        #   뗌
        elif event.type == SDL_KEYUP: 
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
state = 3
frame = 0

#   캐릭터 드로우 & 상태 업데이트 함수들
def drawCharacter(left, down, width, height):
    global x, y

    character.clip_draw(left, down, width, height, x, y, 200, 200)
    update_canvas()
    handle_events()

def drawCharacterF(left, down, width, height):    # 반전해서 그리는 함수
    global x, y

    character.clip_composite_draw(left, down, width, height, 0, 'h', x, y, 200, 200)
    update_canvas()
    handle_events()

def updateFrames(frame, frames, dTime):
    frame = (frame + 1) % frames
    delay(dTime)

#   IDLE 상태 애니메이션 함수들
def idleRight():
    global frame
    
    drawCharacter(frame * 25, 803, 25, 24)
    updateFrames(frame, 4, 0.2)

def idleLeft():
    global frame
    
    drawCharacterF(frame * 25, 803, 25, 24)
    updateFrames(frame, 4, 0.2)

def idleUp():
    global frame
    
    drawCharacterF(frame * 25, 778, 25, 24)
    updateFrames(frame, 6, 0.2)

def idleDown():
    global frame
    
    drawCharacter(frame * 25, 828, 25, 24)
    updateFrames(frame, 6, 0.2)
    #x += dir * 5

#   이동 애니메이션 함수들
def moveRight():
    global x, y, frame

    #character.clip_draw(frame * 25, )

def moveLeft():
    global frame
    pass

def moveUp():
    global frame
    pass

def moveDown():
    global frame
    
    drawCharacterF(frame * 25, 703, 25, 24)
    updateFrames(frame, 12, 0.2)

#   거의 MAIN 함수
while moving:
    clear_canvas()
    bg.draw(400, 100)

    if idle:  #   아이들 상태
        if state == 1:
            idleRight()

        elif state == 2:
            idleLeft()

        elif state == 3:
            idleUp()
        
        elif state == 4:
            idleDown()

    elif state == 1:    #   우
        moveRight()

    elif state == 2:    #   좌
        moveLeft()

    elif state == 3:    #   상
        moveUp()

    elif state == 4:    #   하
        moveDown()

close_canvas()