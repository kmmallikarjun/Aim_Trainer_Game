import pygame
import random
import time
import target_model
from end_screen_view import end_screen
from top_bar_view import draw_top_bar

pygame.init()
pygame.mixer.music.load("start_game.mp3")
WIDTH, HEIGHT=800,600

Win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT=400
TARGET_EVENT=pygame.USEREVENT
TARGET_PADDING=30
BG_COLOR="BLACK"
LIVES=3
TOP_BAR_HEIGHT=50
LABEL_FONT=pygame.font.SysFont("comicsans",24)
BUTTON_FONT = pygame.font.SysFont("comicsans", 40)


def draw(win,targets):
    try:
        win.fill(BG_COLOR)
        for target in targets:
            target.draw(win)
    except Exception as e:
        print(e)
    


def main():
    run = True
    targets=[]
    clock=pygame.time.Clock()
    target_pressed=0
    clicks=0
    misses=0
    start_time=time.time()
    
    pygame.mixer.music.play(-1)
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)
    while run:
        clock.tick(60)
        click=False
        mouse_pos=pygame.mouse.get_pos()
        elapsed_time=time.time()-start_time
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                exit()
                break
            if event.type==TARGET_EVENT:
                x=random.randint(TARGET_PADDING,WIDTH-TARGET_PADDING)
                y=random.randint(TARGET_PADDING + TOP_BAR_HEIGHT,HEIGHT-TARGET_PADDING)
                target=target_model.Target(x,y)
                targets.append(target)

            if event.type==pygame.MOUSEBUTTONDOWN:
                click=True
                clicks+=1   


        for target in targets:
            target.update()

            if (target.size<=0):
                targets.remove(target)
                misses+=1

            if click and target.collide(*mouse_pos):  # splash operator *mouse_pos=mouse_pos[0],mouse_pos[1]
                targets.remove(target)
                target_pressed+=1
                
        if misses>=LIVES:
           end_screen(Win,elapsed_time,target_pressed,clicks,restart_callback=main)

        draw(Win,targets)
        draw_top_bar(Win,elapsed_time,target_pressed,misses)
        pygame.display.update()

    



if(__name__=="__main__"):
    main()