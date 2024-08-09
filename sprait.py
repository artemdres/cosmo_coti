import nastroiki
import sprait
import pygame
import random
import pygame.freetype

pygame.init()

nadpis=pygame.freetype.Font("resurs/srift_rus.ttf", 25)



class Kosmolyt:
    def __init__(self):
        self.kartinka=pygame.image.load("resurs/kosmolyt.png")
        self.kartinka=pygame.transform.scale(self.kartinka,[200, 300])
        sir=self.kartinka.get_width()
        ves=self.kartinka.get_height()
        self.xitboxs=pygame.rect.Rect([0,0],[sir,ves])
        self.hil=3
        self.serdse=pygame.image.load("resurs/serdse.png")
        self.serdse=pygame.transform.scale(self.serdse,[16, 0])
    def resovat(self,okno):
        okno.blit(self.kartinka,self.xitboxs)
    def ypravlenie(self):
        klvivi=pygame.key.get_pressed()
        if klvivi[pygame.K_LEFT]==True:
            self.xitboxs.x=self.xitboxs.x-6
        elif klvivi[pygame.K_RIGHT]==True:
            self.xitboxs.x=self.xitboxs.x+6
        elif klvivi[pygame.K_UP]==True:
             self.xitboxs.y=self.xitboxs.y-6
        elif klvivi[pygame.K_DOWN]==True:
            self.xitboxs.y=self.xitboxs.y+6   



kom=pygame.image.load("resurs/meteorit.png")
kom=pygame.transform.scale(kom,[100,100])

class Kometi:
    def __init__(self):
        sirin=kom.get_width()
        veso=kom.get_height()
        cisl=random.randint(0, nastroiki.VISOTA)
        self.xitboxs=pygame.rect.Rect([nastroiki.SHIRINA,cisl ],[sirin, veso])
        self.xskorost=random.randint(-5, -1)
        self.yskorost=random.randint(-2, 2)
    def resovat(self, okno ):
        okno.blit(kom, self.xitboxs)
    def ypravlenie(self):
        self.xitboxs.x=self.xitboxs.x+self.xskorost    
        self.xitboxs.y=self.xitboxs.y+self.yskorost



kartinka=pygame.image.load("resurs/lazer.png")
kartinka=pygame.transform.scale(kartinka,[100,100])

class Lazer:
    def __init__(self,x,y):
        sirin=kartinka.get_width()
        veso=kartinka.get_height()
        self.xitboxs=pygame.rect.Rect([x,y],[sirin, veso])
    def resovat(self, okno ):
        okno.blit(kartinka, self.xitboxs)
    def ypravlenie(self):    
        self.xitboxs.x=self.xitboxs.x+6



class Knopka:
    def __init__(self,x,y,text, kartinka, razmer1, razmer2):
        self.kartinka=pygame.image.load(kartinka)
        self.kartinka=pygame.transform.scale(self.kartinka,[razmer1,razmer2])
        sirin=self.kartinka.get_width()
        veso=self.kartinka.get_height()
        self.xitboxs=pygame.rect.Rect([x,y],[sirin,veso])
        self.text=text
        kartinka_xitboxs=nadpis.render(text)
        self.katinka_s_textom=kartinka_xitboxs[0]
        self.xitboxs_text=kartinka_xitboxs[1]
        self.xitboxs_text.center=self.xitboxs.center
    def resovat(self, okno):
        okno.blit(self.kartinka, self.xitboxs)
        okno.blit(self.katinka_s_textom, self.xitboxs_text)


        
