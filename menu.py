#!/usr/bin/python3

import pygame
import os
import sys
import json

from classes import Button

pygame.init()

WIDTH, HEIGHT = 400, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
FONT_SIZE_MENU = 50
FONT_SIZE_OPTIONS = 16
FONT_SIZE_BACK = 20

# Carcateristicas del display principal
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACESHIP SHOOTER")

# Imagenes
BACKGROUND_BIG = pygame.image.load(os.path.join('Assets', 'wallpaper.jpg'))
BACKGROUND_MAIN = pygame.transform.scale(BACKGROUND_BIG, (WIDTH, HEIGHT))

BUTTON_BIG = pygame.image.load(os.path.join("Assets", "button_rect.png"))
BUTTON_RECT = pygame.transform.scale(BUTTON_BIG, (BUTTON_WIDTH, BUTTON_HEIGHT))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 198, 51)
GRAY = (150, 150, 150)
BLUE = (30, 144,255)

# sonidos del juego
pygame.mixer.music.load('Sounds/dragonball.mpga')#musica del juego
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

# FUNCIONES -------------------------------------------------------------------


# Funcion para mover el fondo del juego
def scrolling_backgroud():

    run = True
    y_position = 0

    while run:
        WINDOW.fill(BLACK)
        WINDOW.blit(BACKGROUND_MAIN, (0, y_position))
        WINDOW.blit(BACKGROUND_MAIN, (0, HEIGHT + y_position))

        if y_position == -HEIGHT:
            WINDOW.blit(BACKGROUND_MAIN, (0, HEIGHT + y_position))
            y_position = 0

        y_position -= 1


# Funcion para cambiar el tamano de la tipgrafia
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join('Assets', 'font.ttf'), size)


# Render multiples lineas
def multiline_render(render_text):
    position = 50
    pygame.draw.rect(WINDOW, BLACK, pygame.Rect(0, 0, 0, 0))
    for x in range(len(render_text)):
        rendered = get_font(30).render(render_text[x], 100, (WHITE))
        WINDOW.blit(rendered, (20, position))
        position += 40


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill(BLACK)

        PLAY_TEXT = get_font(FONT_SIZE_OPTIONS).render("OPCIONES", True,
                                                       "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(WIDTH/2, HEIGHT/4))
        WINDOW.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(None, (WIDTH/2, HEIGHT - 100), "VOLVER",
                           get_font(FONT_SIZE_BACK), WHITE, YELLOW)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_mode(SCREEN)        

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill(BLACK)

        OPTIONS_TEXT = get_font(FONT_SIZE_OPTIONS).render("OPCIONES",
                                                          True, BLUE)

        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        WINDOW.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(BUTTON_RECT, (WIDTH/2, HEIGHT - 100), "VOLVER",
                              get_font(FONT_SIZE_OPTIONS), WHITE, YELLOW)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WINDOW)

        OPTIONS_sonidoA = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/2), "Activar sonido",
                                get_font(FONT_SIZE_OPTIONS), WHITE, YELLOW)
        OPTIONS_sonidoA.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_sonidoA.update(WINDOW)
     
        OPTIONS_sonidoD = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/3), "Desactivar sonido",
                                get_font(FONT_SIZE_OPTIONS), WHITE, YELLOW)
        OPTIONS_sonidoD.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_sonidoD.update(WINDOW)

        OPTIONS_fs = Button(BUTTON_RECT, (WIDTH/2, HEIGHT-200), "Pantalla completa",
                            get_font(FONT_SIZE_OPTIONS), WHITE, YELLOW)
        OPTIONS_fs.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_fs.update(WINDOW)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_sonidoA.checkForInput(OPTIONS_MOUSE_POS):
                    #sound_on = True
                    #if sound_on:
                    pygame.mixer.music.play(loops=-1)
                if OPTIONS_sonidoD.checkForInput(OPTIONS_MOUSE_POS):
                    #sound_on = False
                    #if sound_on:
                    pygame.mixer.music.stop()
                if OPTIONS_fs.checkForInput(OPTIONS_MOUSE_POS):
                    #sound_on = False
                    #if sound_on:
                    pygame.display.set_mode(SCREEN, pygame.SCALED | pygame.FULLSCREEN)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_mode(SCREEN)

        pygame.display.update()


# Funcion para mostar uan breve explicacion acerca del juego
def about():
    WINDOW.blit(BACKGROUND_MAIN, (0, 0))
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        with open(os.path.join('Assets', 'about.json')) as show:
            multiline_render(json.load(show))

        PLAY_BACK = Button(None, (WIDTH/2, HEIGHT-100), "VOLVER",
                           get_font(FONT_SIZE_BACK), WHITE, YELLOW)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_mode(SCREEN)

        pygame.display.update()


def main_menu():
    while True:
        WINDOW.blit(BACKGROUND_MAIN, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT_1 = get_font(FONT_SIZE_MENU).render("SPACESHIP",
                                                      True, YELLOW)

        MENU_TEXT_2 = get_font(FONT_SIZE_MENU - 10).render("SHOOTER",
                                                           True, YELLOW)

        MENU_RECT_1 = MENU_TEXT_1.get_rect(center=(WIDTH/2, HEIGHT/8))
        MENU_RECT_2 = MENU_TEXT_2.get_rect(center=(WIDTH/2, HEIGHT/5))

        PLAY_BUTTON = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/3), "JUGAR",
                             get_font(FONT_SIZE_OPTIONS), WHITE, GRAY)

        OPTIONS_BUTTON = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/3 + 100),
                                "OPCIONES", get_font(FONT_SIZE_OPTIONS),
                                WHITE, GRAY)

        ABOUT_BUTTON = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/3 + 200), "ACERCA",
                              get_font(FONT_SIZE_OPTIONS), WHITE, GRAY)

        QUIT_BUTTON = Button(BUTTON_RECT, (WIDTH/2, HEIGHT/3 + 300), "SALIR",
                             get_font(FONT_SIZE_OPTIONS), WHITE, GRAY)

        WINDOW.blit(MENU_TEXT_1, MENU_RECT_1)
        WINDOW.blit(MENU_TEXT_2, MENU_RECT_2)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, ABOUT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # play()
                    scrolling_backgroud()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_mode(SCREEN)

        pygame.display.update()


main_menu()
