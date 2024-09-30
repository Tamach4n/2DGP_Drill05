from pico2d import *

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('ThePilot1.png')

def checkState():
    global dirX, dirY

    if dirX == 0 & dirY == 0:
        return True
    
    else:
        return False
    
def checkCollision():
    global x, y

    r = 50

    if (x - r >= 0) and (x + r <= 800) and (y - r >= 0) and (y + r <= 600):
        return True
    
    else:
        return False

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
                if not checkState():  break

                dirX += 1
                state = 1

            elif event.key == SDLK_LEFT:
                if not checkState():  break
                
                dirX -= 1
                state = 2

            elif event.key == SDLK_UP:
                if not checkState():  break
                
                dirY += 1
                state = 3

            elif event.key == SDLK_DOWN:
                if not checkState():  break
                
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
y = 600 // 2

idle = True
dirX, dirY = 0, 0
state = 4
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
    return frame

#   IDLE 상태 애니메이션 함수들
def idleRight():
    global frame
    
    drawCharacter(frame * 25, 803, 25, 24)
    frame = updateFrames(frame, 4, 0.2)

def idleLeft():
    global frame
    
    drawCharacterF(frame * 25, 803, 25, 24)
    frame = updateFrames(frame, 4, 0.2)

def idleUp():
    global frame
    
    drawCharacterF(frame * 25, 778, 25, 24)
    frame = updateFrames(frame, 6, 0.2)

def idleDown():
    global frame
    
    drawCharacter(frame * 25, 828, 25, 24)
    frame = updateFrames(frame, 6, 0.2)

#   이동 애니메이션 함수들
def moveRight():
    global x, frame

    drawCharacter(frame * 25, 679, 25, 24)
    frame = updateFrames(frame, 12, 0.2)

    if checkCollision():
        x += dirX * 20

def moveLeft():
    global frame, x

    drawCharacterF(frame * 25, 679, 25, 24)
    frame = updateFrames(frame, 12, 0.2)

    if checkCollision():
        x += dirX * 20

def moveUp():
    global frame, y
    
    drawCharacter(frame * 25, 653, 25, 24)
    frame = updateFrames(frame, 12, 0.2)

    if checkState():
        y += dirY * 20

def moveDown():
    global frame, y
    
    drawCharacterF(frame * 25, 703, 25, 24)
    frame = updateFrames(frame, 12, 0.2)

    if checkState():
        y += dirY * 20

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