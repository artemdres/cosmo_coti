import nastroiki
import sprait
import pygame
import random
import pygame.freetype

pygame.init()
fon_menu=pygame.image.load("resurs/menu.jpg")
fon_menu=pygame.transform.scale(fon_menu,[nastroiki.SHIRINA, nastroiki.VISOTA])
okno=pygame.display.set_mode([nastroiki.SHIRINA, nastroiki.VISOTA])
fon=pygame.image.load("resurs/kosmos.jpg")
fon=pygame.transform.scale(fon,[nastroiki.SHIRINA, nastroiki.VISOTA])
serdse=pygame.image.load("resurs/serdse.png")
serdse=pygame.transform.scale(serdse,[50, 50])
korbl=sprait.Kosmolyt()
knopka=sprait.Knopka(700, 400, "заново", "PNG/UI/buttonBlue.png",300,100)
knopka_nastroek=sprait.Knopka(700, 600 , "настройки","PNG/UI/buttonBlue.png",300,100 )
knopka2=sprait.Knopka(700, 800, "выйти", "PNG/UI/buttonBlue.png",300,100)

konopka_on=sprait.Knopka(600,600,"", "resurs/on.png",200,200)
konopka_off=sprait.Knopka(600,600,"", "resurs/off.png",200,200)
text=pygame.freetype.Font("resurs/srift_rus.ttf", 40)






menu_ili_game=1




musik_laz=pygame.mixer.Sound("resurs/lazer_mus.wav")
musik=pygame.mixer.Sound("resurs/musik.wav")
musik.play(-1)
podbit_met=0
time_psto=0
time_vistre=0
off_on=1
time_meteor=pygame.USEREVENT
pygame.time.set_timer(time_meteor, 700)
seve_met=[]
seve_lazer=[]
q=0
while 0==q:
    time_psto=pygame.time.get_ticks()
    sobitia=pygame.event.get()
    for sob in sobitia:
        if sob.type==pygame.QUIT:
            q=q+1
        elif sob.type==time_meteor:
            meteori=sprait.Kometi()
            seve_met.append(meteori)
        if sob.type==pygame.KEYDOWN:
            if sob.key==pygame.K_SPACE and time_psto-time_vistre>500:
                musik_laz.play()
                lazer=sprait.Lazer(korbl.xitboxs.centerx, korbl.xitboxs.centery-50   )
                seve_lazer.append(lazer)
                time_vistre=pygame.time.get_ticks()
    
        if sob.type==pygame.MOUSEBUTTONDOWN and menu_ili_game==0:
            
            if knopka.xitboxs.collidepoint(sob.pos)==True:
                menu_ili_game=1
                korbl.hil=3
                korbl.xitboxs.x=0
                korbl.xitboxs.y=0
                seve_met=[]
                seve_lazer=[]
            if knopka_nastroek.xitboxs.collidepoint(sob.pos)==True:
                menu_ili_game=2
            if knopka2.xitboxs.collidepoint(sob.pos)==True:
                q=q+1
        if sob.type==pygame.MOUSEBUTTONDOWN and menu_ili_game==2:
            if konopka_on.xitboxs.collidepoint(sob.pos)==True and off_on==0:
                off_on=1
                musik.stop()
            elif konopka_off.xitboxs.collidepoint(sob.pos)==True and off_on==1:
                off_on=0
                musik.play(-1)
                



    if menu_ili_game==1:
        
        korbl.ypravlenie()
        
        for stolknoveni_metiri in seve_met:
            for stolknovenie_laz_in_met in seve_lazer:
                if stolknovenie_laz_in_met.xitboxs.colliderect(stolknoveni_metiri.xitboxs)==True:
                    seve_met.remove(stolknoveni_metiri)
                    seve_lazer.remove(stolknovenie_laz_in_met)
                    podbit_met=podbit_met+1
                    break








        for stolknoveni_metiri in seve_met:
            if korbl.xitboxs.colliderect(stolknoveni_metiri.xitboxs)==True:
                korbl.hil=korbl.hil-1

                seve_met.remove(stolknoveni_metiri)
        if korbl.hil<0:
            menu_ili_game=0
            

        for met in seve_met:
            met.ypravlenie()
        for laz in seve_lazer:
            laz.ypravlenie()
                
        okno.blit(fon,[0,0])


        if korbl.hil==3:
            okno.blit(serdse,[1450,0])
            okno.blit(serdse,[1500,0])
            okno.blit(serdse,[1550,0])
        elif korbl.hil==2:
            okno.blit(serdse,[1500,0])
            okno.blit(serdse,[1550,0])
        elif korbl.hil==1:
            okno.blit(serdse,[1550,0])

        


        korbl.resovat(okno)
        for met in seve_met:
            met.resovat(okno)
        for laz in seve_lazer:
            laz.resovat(okno)
        text.render_to(okno,[10,10], str(podbit_met))
    elif menu_ili_game==0:
        okno.blit(fon_menu,[0,0])
        knopka.resovat(okno)




        knopka_nastroek.resovat(okno)

        
        knopka2.resovat(okno)
    elif menu_ili_game==2:
        
        okno.blit(fon_menu,[0,0])
        if off_on==0:
            konopka_on.resovat(okno)
        elif off_on==1:
            konopka_off.resovat(okno)
        
        

    
        


    pygame.display.update()