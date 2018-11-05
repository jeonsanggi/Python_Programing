#슈팅게임 만들기
#pip install pygame 필요

import pygame
import random
from time import sleep

#게임에 사용되는 전역변수
BLACK = (0, 0, 0)     #게임 화면 배경색
RED = (255, 0,0)    #놓친 적의 수 글씨 색
WHITE = (255, 255, 255) #적 처치 수 글씨 색
pad_width = 480     #게임 화면 가로
pad_height = 640    #게임 화면 세로
fighter_width = 36  #전투기 크기 가로
fighter_height = 38 #전투기 크기 세로
enemy_width = 26    #적 크기 가로
enemy_height = 20   #적 크기 세로

#처치한 적 수
def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Kills : '+ str(count), True, WHITE)
    gamepad.blit(text, (0,0))

#적이 화면 아래로 통과한 개수
def drawPassed(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Passed : '+ str(count), True, RED)
    gamepad.blit(text, (360,0))

#화면에 글씨 보이게 하기
def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2, pad_height/2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

#적과 충돌했을때
def crash():
    global gamepad
    dispMessage('Crashed')

#게임 오버 메시지
def gameover():
    global gamepad
    dispMessage('Game Over')

#게임에 등장하는 객체 드로잉
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

#게임 실행 메인 함수
def runGame():
    global gamepad, clock, fighter, enemy, bullet

    isShot = False
    shotcount = 0
    enemypassed = 0

    #무기 좌표 리스트
    bullet_xy = []

    #전투기 초기 위치 (x, y) 설정
    x = pad_width*0.45
    y = pad_height*0.9
    x_change = 0    #전투기를 좌우 이동시키기 위한 변수


    #적 초기 위치 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3

    doneFlag = True    #게임 종료를 위해 게임 화면을 닫을 때 False로 설정
    while doneFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #이벤트가 마우스로 게임을 닫을때
                doneFlag = False

            if event.type == pygame.KEYDOWN:    #키보드가 눌러졌을 때 발생
                if event.key == pygame.K_LEFT:
                    x_change-=5
                elif event.key == pygame.K_RIGHT:
                    x_change +=5

                #왼쪽 컨트롤 키를 누르면 무기 발사/한번에 2발
                elif event.key == pygame.K_LCTRL:
                    if len(bullet_xy) < 2:
                        bullet_x = x + fighter_width/2
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x, bullet_y]) #bullet의 x,y 좌표 추가

            if event.type == pygame.KEYUP:      #누르고 있던 키보드를 땟을 때 발생
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #게임 화면을 검은색으로 채우고 화면을 업데이트 함
        gamepad.fill(BLACK)

        #전투기의 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width

        #게이머 전투기와 적과 충돌했는지 체크
        if y < enemy_y + enemy_height:
            if (enemy_x > x and enemy_x < x + fighter_width) or (enemy_x + enemy_width > x and enemy_x +enemy_width < fighter_width):
                crash()

        drawObject(fighter, x, y)

        #무기 발사 화면에 그리기
        if len(bullet_xy)!=0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -=10
                bullet_xy[i][1] = bxy[1]

                #적을 격추했을 경우
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x and bxy[0] < enemy_x + enemy_width:
                        bullet_xy.remove(bxy)
                        isShot = True
                        shotcount += 1

                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        drawScore(shotcount)
        # 적을 아래로 움직임
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemypassed += 1

        if enemypassed == 3:
            gameover()

        drawPassed(enemypassed)

        #적이 무기에 맞았는지 확인하고 맞았으면 스피드업
        if isShot:
            enemy_speed += 1
            if enemy_speed >= 10:
                enemy_speed = 10

            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemy_y = 0
            isShot = False

        drawObject(enemy, enemy_x, enemy_y)


        pygame.display.update()
        clock.tick(60)  #게임 화면의 초당 프레임 수 = 60으로 설정 (사람의 눈에 자연스럽게 보이게 되는 초당 프레임 수는 약 30)



    pygame.quit()

#게임 초기화 함수
def initGame():
    global gamepad, clock, fighter, enemy, bullet

    pygame.init()   #pygmae 라이브러리 초기화 (pygame을 활용하려면 게임 구현 초기에 항상 호출해야 함)
    gamepad = pygame.display.set_mode((pad_width ,pad_height))  #게임 화면 크기 설정
    pygame.display.set_caption('MyGalago')  #Title바에 MyGalago 표시
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock() #초당 프레임 수를 설정하는 Clock 객체를 생성

initGame()
runGame()
