import pygame as pg
import sys
import random

def obstacle_render(obs_list,obst_list):
    if obs_list:
        for i in range (len(obs_list)):
            screen.blit(pipe,pipe.get_rect(topleft=obs_list[i]))
            screen.blit(pipet,pipet.get_rect(topleft=obst_list[i]))
            obst_list[i][0]=obst_list[i][0]-4
            obs_list[i][0]=obst_list[i][0]-4
        if obs_list[0][0]<-150:
            del obs_list[0]
            del obst_list[0]
        return obs_list,obst_list
    else:
        return[],[]
        

pg.init()
screen=pg.display.set_mode((1200,576))
pg.display.set_caption("Hello")
clock=pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 22)
sky=pg.image.load('finalbg.jpg').convert()
pipe=pg.image.load('pipe.png').convert_alpha()
pipe=pg.transform.scale(pipe,(160,500))
pipet=pg.transform.rotate(pipe,180)
pipet=pg.transform.flip(pipet,True,False)
pipet_rect=pipet.get_rect(topleft=(1200,-50))
pipe_rect=pipe.get_rect(topleft=(1200,300))
pipe_rect_copy=pipe.get_rect(topleft=(550,300))
pipet_rect_copy=pipet.get_rect(topleft=(550,-50))
bird=pg.image.load('bird.png').convert_alpha()
bird=pg.transform.scale(bird,(70,50))
bird_rect=bird.get_rect(center=(102,100))
sbt=font.render("START",True,"red")
sbt_rect=sbt.get_rect(center=(600,288))
screen.blit(sbt,sbt_rect)

#defining timer for the obstacles to occur
timer=pg.USEREVENT+1
pg.time.set_timer(timer,2000)

#bird=pg.transform.rotate(bird,-30)
obs_list=[]
obst_list=[]
t=0
a=0
score="0"
s=100
x1=random.randint(-250,0)
x2=random.randint(-300,-50)
text = font.render(score, True, (77,208,225))
text_rect = text.get_rect(center=(600,80))

while True:
    #draw everything and update
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            s=s+t*t*1.5-t*a
            a=25
            t=0
        if event.type==timer:
            x=4*random.randint(300,360)
            y=400+random.randint(-150,100)
            obs_list.append([x,y])
            obst_list.append([x,y-700+random.randint(0,50)])
    # defining thr rectangle postions
    el=pg.draw.circle(screen,"blue",bird_rect.center,20)
    
    #displaying the final position on the surface
    screen.blit(sky,(-100,0))
    bird_rect.centery=s+t*t*1.5-t*a
    screen.blit(bird,bird_rect)
    screen.blit(text,text_rect)

    obs_list,obst_list=obstacle_render(obs_list,obst_list)

    if obs_list and el.right-2==obs_list[0][0]+160:
        score=str(eval(score)+1)
        text = font.render(score, True,(77,208,225))
    if obs_list and obst_list and (el.colliderect(pipe.get_rect(topleft=obs_list[0])) or el.colliderect(pipet.get_rect(topleft=obst_list[0]))):
        pg.quit()
        sys.exit()
    t=t+0.4
    print(el.right)
    pg.display.update()
    clock.tick(60)   #does not let the frame rate to be higher than 60