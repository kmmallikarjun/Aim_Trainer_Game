import pygame
import math

WIDTH, HEIGHT=800,600
BG_COLOR="BLACK"


# end game screen
def end_screen(win,elapsed_time,targets_pressed,clicks,restart_callback=None):
    pygame.font.init()
    LABEL_FONT=pygame.font.SysFont("comicsans",24)
    BUTTON_FONT = pygame.font.SysFont("comicsans", 40)

    win.fill(BG_COLOR)
    pygame.mixer.music.stop()
    time_label=LABEL_FONT.render(f"Time: {format_time(elapsed_time)}",1,"white")
    
    speed =round(targets_pressed/elapsed_time,1)
    speed_label=LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")
    hits_label=LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")
    try:
        accuracy=round((targets_pressed/clicks)*100,1)
    except ZeroDivisionError:
        accuracy=0
    
    accuracy_label=LABEL_FONT.render(f"Accuracy:{accuracy}%",1,"white")
 
    win.blit(time_label,(get_middle(time_label),50))
    win.blit(speed_label,(get_middle(speed_label),150))
    win.blit(hits_label,(get_middle(hits_label),250))
    win.blit(accuracy_label,(get_middle(time_label),350)) 
    
    #Button SetUp
    button_text= BUTTON_FONT.render("Play Again?",1,"black")
    button_width, button_height=300,60
    button_rect=pygame.Rect((WIDTH//2 - button_width//2,500),(button_width,button_height))
    pygame.draw.rect(win,"white",button_rect,border_radius=10)
    win.blit(button_text,(button_rect.centerx-button_text.get_width()//2,
                          button_rect.centery-button_text.get_height()//2))
    
    pygame.display.update()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if event.type == pygame.KEYDOWN :
            if(event.type==pygame.MOUSEBUTTONDOWN):
                if(button_rect.collidepoint(pygame.mouse.get_pos())):
                  if restart_callback:  
                    restart_callback() 
                  return
              
              
def format_time(secs):
    milli=math.floor(int(secs*1000 % 1000)/100)
    seconds=int(round(secs % 60, 1))
    minutes=int(secs // 60)   
    return f"{minutes:02d}:{seconds:02d}.{milli}" 


def get_middle(surface):
    return WIDTH/2 -surface.get_width()/2