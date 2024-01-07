"""Simón"""
import sys
import random
import pygame
pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

ventana = pygame.display.set_mode((400, 450))
pygame.display.set_caption("SIMÓN")
reloj = pygame.time.Clock()

#imagenes de la botonera con cada boton encendido
imagen = pygame.image.load('simon.png')
a = pygame.image.load('a.png')
r = pygame.image.load('r.png')
v = pygame.image.load('v.png')
az = pygame.image.load('az.png')
vio = pygame.image.load('vio.png')
tono1 = pygame.mixer.Sound("sound1.wav")
tono2 = pygame.mixer.Sound("sound2.wav")
tono3 = pygame.mixer.Sound("sound3.wav")
tono4 = pygame.mixer.Sound("sound4.wav")




def cual_boton():

    x,y = pygame.mouse.get_pos()
    color = imagen.get_at((x,y))
    if color[0] == 179 and color[1]==0 and color[2]==0:
        return 1
    if color[1] == 179 and color[0]==179:
        return 2
    if color[1] == 179 and color[0]==0:
        return 4
    if color[2] == 179:
        return 3
    if color[0] == 179 and  color[2] == 155:
        return 5


def bien_o_mal(boton):

    return cual_boton() == boton



def encender(boton):

    if boton == 1:
        ventana.blit(r,(0,0,0,0))
        tono1.play()            
    if boton == 2:
        ventana.blit(a,(0,0,0,0))
        tono2.play()    
    if boton == 4:
        ventana.blit(v,(0,0,0,0))
        tono4.play()
    if boton == 3:
        ventana.blit(az,(0,0,0,0))
        tono3.play()
    if boton == 5:
        ventana.blit(vio,(0,0,0,0))
    pygame.display.update()

def mostrar(secuencia):

    for boton in secuencia:
        pygame.time.delay(500)
        encender(boton)
        pygame.time.delay(500)
        ventana.blit(imagen,(0,0,0,0))
        tono1.stop()
        tono2.stop()
        tono3.stop()
        tono4.stop()
        pygame.display.update()


def perdiste():

    for i in range(40):
        encender(i%5)  
        pygame.time.delay(50)
        tono1.stop()
        tono2.stop()
        tono3.stop()
        tono4.stop()


        ventana.blit(imagen,(0,0,0,0))
    ventana.blit(imagen,(0,0,0,0))
    pygame.display.update()


ventana.blit(imagen,(0,0,0,0))
pygame.display.update()


def juego():
    
    secuencia =[]
    while True:
        fuente = pygame.font.Font(None, 36)
        texto = f"{len(secuencia)}"
        texto_superficie = fuente.render(texto, True, BLANCO)
        pygame.draw.rect(ventana,(NEGRO),(180,400,220,430))
        ventana.blit(texto_superficie,(200,420))

        rand = random.randint(1,4)
        secuencia.append(rand) 
        mostrar(secuencia)      
        i = 0
        pygame.event.clear()

        for boton in secuencia:
            no_se_apriete_boton = True
            while no_se_apriete_boton: #espera a que se apriete algun boton

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button in (1,2,3) :
                        if cual_boton() == 5:
                            encender(5)
                        elif bien_o_mal(boton):
                            encender(cual_boton())
                        else:
                            perdiste()
                            return False

                    if event.type == pygame.MOUSEBUTTONUP and event.button in (1,2,3):
                        ventana.blit(imagen,(0,0,0,0)) #apagar
                        tono1.stop()
                        tono2.stop()
                        tono3.stop()
                        tono4.stop()

                        pygame.display.update()
                        if cual_boton() == 5:
                            return True
                        no_se_apriete_boton = False  #ya se apreto tecla, no se espera una siguiente
                        i += 1
                        break

def entradas():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                     
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (1,2,3):
                if cual_boton() == 5:
                    encender(5)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button in (1,2,3):
                ventana.blit(imagen,(0,0,0,0))                    
                pygame.display.update()
                if cual_boton() == 5:
                    return "reset"



while True:
    if entradas()=="reset":
        while juego():
            pass
