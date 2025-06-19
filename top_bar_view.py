import pygame
import math

TOP_BAR_HEIGHT=50
LIVES=3
WIDTH, HEIGHT=800,600


def draw_top_bar(win,elapsed_time,targets_pressed,misses):
    pygame.font.init()
    LABEL_FONT=pygame.font.SysFont("comicsans",24)
    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BAR_HEIGHT))
    time_label=LABEL_FONT.render(f"Time:{format_time(elapsed_time)}",1,"black")
    
    speed =round(targets_pressed/elapsed_time,1)
    speed_label=LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")
    hits_label=LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")
    lives_label=LABEL_FONT.render(f"Lives: {LIVES-misses}", 1, "black")
    
    win.blit(time_label,(5,5))
    win.blit(speed_label,(200,5))
    win.blit(hits_label,(430,5))
    win.blit(lives_label,(630,5))   
    
def format_time(secs):
    milli=math.floor(int(secs*1000 % 1000)/100)
    seconds=int(round(secs % 60, 1))
    minutes=int(secs // 60)   
    return f"{minutes:02d}:{seconds:02d}.{milli}" 