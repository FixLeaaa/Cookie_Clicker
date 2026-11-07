import pygame, sys, random
from pygame.math import Vector2

class COOKIE:
    def __init__(self):
        self.rect = pygame.Rect(120, 150, 100, 91)
        self.is_clicked = False
    def draw_cookie(self):
        # cookie_rect = pygame.Rect(120, 150, 100, 91) # x, y, w, h
        screen.blit(cookie, self.rect)
    def check_click(self):
        # Check if the left mouse button is pressed AND the mouse is over this sprite
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            # Ensure the action is performed only once per press
            if not self.is_clicked:
                print("Action triggered by subclass method!")
                self.is_clicked = True
                # click animation
                # increase counter
                return True
        else:
            self.is_clicked = False

class MAIN:
    def __init__(self):
        self.cookie = COOKIE()
    def draw_elements(self):
        self.cookie.draw_cookie()
        text_surface = font.render("Cookie Clicker", True, (255,255,255))
        text_rect = text_surface.get_rect(center=(175, 50))
        screen.blit(text_surface, text_rect)

pygame.init()
screen = pygame.display.set_mode((350, 400))
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Cookie Clicker")

cookie = pygame.image.load('graphics/minecraft_cookie_scaled.png')
font = pygame.font.Font("fonts/Minecraft.ttf", 30)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


while True:
    # draw all our elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for 
            cookie.check_click(event)
        if event.type == SCREEN_UPDATE:
            pass
            # #main_game.update()

    screen.fill((204, 238, 253))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FPS)

#     def __init__(self):
#         self.body = pygame.draw.circle(screen, BLUE, (175, 200), 50)  

# mouse_buttons = pygame.mouse.get_pressed()
# counter = 0

# class MAIN:
#     def check_click(self):
#         if mouse_buttons[0]:
#             counter = counter + 1

# cookie = pygame.image.load('graphics/minecraft_cookie.png').convert_alpha()

# BLUE = (0, 0, 255)
# WHITE = (255, 255, 255)

# font = pygame.font.Font("fonts/Minecraft.ttf", 24)
# # Render text
# text_surface = font.render("Score: 100", True, WHITE)
# text_rect = text_surface.get_rect(center=(400, 50))
# #screen.blit(text_surface, text_rect)

    # pygame.draw.circle(screen, BLUE, (175, 200), 50)  
    # text_surface = font.render("Cookie Clicker", True, WHITE)
    # text_rect = text_surface.get_rect(center=(175, 50))
    # screen.blit(text_surface, text_rect)