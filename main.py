import pygame
import sys
import time
from random import randint

pygame.init()
class Sprito(tuple):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("1.jpg")
        self.CL=None
        self.x= int(0)
        self.y= int(0)
    def UpdateLocation(self,a,b):
        self.CL=[a,b]
        self.x=a
        self.y=b
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def UpdateImage(self):
        self.image=pygame.image.load("1 copy.jpg")


def main():      
    # logo=pygame.image.load("Michelangelo.jpg")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((1200,600))
    screen_width=1200
    screen_height=600

    image = pygame.image.load("1.jpg")
    bgd_image = pygame.image.load("Back.jpg")
    bgd2_image = pygame.image.load("Back copy.jpg")
    x_pos=600
    y_pos=300

    sprites =[]

    spritecopy =[]

    locations = set()

    s =Sprito()
    s.UpdateLocation(x_pos,y_pos)
    sprites.append(s)

    screen.blit(sprites[0].image, (x_pos,y_pos))

    a =Sprito()
    a.UpdateImage()
    a_x=randint(0,1200)
    a_y=randint(0,600)
    while(a_x==x_pos):
        a_x=randint(0,1200)
    while(a_y==y_pos):
        a_y=randint(0,600)

    a.UpdateLocation(a_x,a_y)
    step_x=0
    step_y=0

    screen.blit(a.image, (a.getX(),a.getY()))

    pygame.display.flip()
    running= True
    event_key="N"
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                # keys=[pygame.key.get_pressed()]
                if(event.key==pygame.K_LEFT):
                    event_key="left"
                    step_x=-24
                    step_y=0
                if(event.key==pygame.K_RIGHT):
                    event_key="right"
                    step_x=24
                    step_y=0
                if(event.key==pygame.K_UP):
                    event_key="up"
                    step_x=0
                    step_y=-28
                if(event.key==pygame.K_DOWN):
                    event_key="down"
                    step_x=0
                    step_y=28
        x_pos+=step_x
        if(x_pos==0):
            x_pos=0
            running=False
        if(x_pos>=screen_width-30):
            x_pos=screen_width-30
            running=False

        y_pos+=step_y

        if(y_pos<=0):
            y_pos=0
            running=False
        if(y_pos>=screen_height-30):
            y_pos=screen_height-30
            running=False

        time.sleep(0.15)
        sprites[0].UpdateLocation(x_pos,y_pos)
        screen.blit(bgd_image,(0,0))
        screen.blit(bgd2_image,(600,0))
        Add = False
        while a.getX()-x_pos>=-24 and a.getX()-x_pos<24 and a.getY()-y_pos>=-28 and a.getY()-y_pos<28:
            x=randint(30,270)
            y=randint(30,570)
            a.UpdateLocation(x,y)
            Add = True
        if Add:
            Sn= Sprito()
            diff_x=28
            diff_y=28
            if(event_key=="left"):
                Sn.UpdateLocation(sprites[len(sprites)-1].getX()+diff_x,y_pos)
            elif(event_key=="right"):
                Sn.UpdateLocation(sprites[len(sprites)-1].getX()-diff_x,y_pos)
            elif(event_key=="up"):
                Sn.UpdateLocation(x_pos,sprites[len(sprites)-1].getY()+diff_y)
            else:
                Sn.UpdateLocation(x_pos,sprites[len(sprites)-1].getY()-diff_y)
            sprites.append(Sn)
            # print("len")
            # print(len(sprites))
            # print()
            # for i in range(len(sprites)):
            #     print(sprites[i].getX())
            #     print(sprites[i].getY())
        
        for x in sprites:
            f= Sprito()
            # print(x.getX())
            # print(x.getY())
            f.UpdateLocation(x.getX(),x.getY())
            spritecopy.append(f)
        locations.clear()
        for i in range(0,len(sprites)):
            screen.blit(sprites[i].image,(sprites[i].getX(),sprites[i].getY()))
            temp = str(sprites[i].getX())
            temp+= str(sprites[i].getY())
            if(temp not in locations):
                locations.add(temp)
            else:
                running=False
                # print("here")
                break
            if(i!=0):
                sprites[i].UpdateLocation(spritecopy[i-1].getX(),spritecopy[i-1].getY())

        print(locations)
        print()
        screen.blit(a.image, (a.getX(),a.getY()))
        pygame.display.flip()
        spritecopy.clear()
        Add = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()