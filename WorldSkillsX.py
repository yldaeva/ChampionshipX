
import pygame
import sys
from pygame.locals import *
pygame.init()
icon=pygame.image.load('TLgreen.png')
bg = pygame.image.load('Schema.PNG')
car = pygame.image.load('BCbottom.PNG')
men=pygame.image.load('Pedestrain.PNG')
vagon=pygame.image.load('VagonBlock.PNG')
heavy=pygame.image.load('HeavyBlock2.PNG')
dorogv=pygame.image.load('Zvertical.PNG')
dorogg=pygame.image.load('Zhorizontal.PNG')

width=700
height=700
window=pygame.display.set_mode((width,height))
screen=pygame.Surface((width, height))
color = (255,255,255)
color_dark = (100,100,100)
color_light = (170,170,170)
smallfont = pygame.font.SysFont('Corbel',15)
text = smallfont.render('Menu' , True , color)
pygame.display.set_caption('World Skills X')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
#pygame.display.Surface.fill(img=Image.open('d:\\Schema.JPG'))
start_a=True

cube=pygame.Surface((30,30)) #обьект
#начальное состояние
x1 = 50
y1 = 50
x_cube=0
y_cube=0

while start_a==True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            start_a=False
           
        if i.type==pygame.KEYDOWN and i.key==pygame.K_UP:
            y_cube-=5
            x_cube=0
        if i.type==pygame.KEYDOWN and i.key==pygame.K_RIGHT:
            x_cube+=5
            y_cube=0
        if i.type==pygame.KEYDOWN and i.key==pygame.K_LEFT:
            x_cube-=5
            y_cube=0
        if i.type==pygame.KEYDOWN and i.key==pygame.K_DOWN:
           y_cube+=5
           x_cube=0
    if x1 >= width:
        x_cube-=5
        y_cube=0
        
    if x1 < 0:
        x_cube+=5
        y_cube=0
    if y1 >= height:
       y_cube-=5
       x_cube=0
    if y1 < 0:
       y_cube+=5
       x_cube=0
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/width <= mouse[0] <= width/width+100 and height/height <= mouse[1] <= height/height+40:
                pygame.quit()
    mouse = pygame.mouse.get_pos()
    x1 += x_cube
    y1 += y_cube
    window.blit(screen,(0,0))
    screen.blit(bg,(0,0))
    
    screen.blit(heavy,(500,600))
    screen.blit(heavy,(340,630))
    screen.blit(heavy,(90,180))
    screen.blit(vagon,(90,80))
    screen.blit(vagon,(360,40))
    screen.blit(vagon,(500,400))
    screen.blit(dorogv,(420,600))
    screen.blit(dorogv,(420,630))
    
    screen.blit(car,(x1,y1))
    
    if width/width <= mouse[0] <= width/width+100 and height/height <= mouse[1] <= height/height+40:
        pygame.draw.rect(screen,color_light,[width/width,height/height,100,40])
        screen.blit(men,(200,15))
        screen.blit(men,(360,170))
        screen.blit(men,(600,200))
        screen.blit(men,(200,580))
        screen.blit(men,(420,560))
        screen.blit(men,(280,250))
          
    else:
        pygame.draw.rect(screen,color_dark,[width/width,height/height,100,40])
      
    screen.blit(text , (width/width+50,height/height))


    pygame.display.update()
    clock.tick(20)
pygame.quit()


 

