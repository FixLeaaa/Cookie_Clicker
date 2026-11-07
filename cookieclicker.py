import pygame, sys

class Game:
    def __init__(self):
        self.cookies = 0
        self.cookie_per_click = 1

        self.cookie_size = 200
        self.original_cookie_size = 200
        self.animation_timer = 0

        self.cookie_image = pygame.transform.scale(cookie, (self.original_cookie_size, self.original_cookie_size))
        self.cookie = self.cookie_image.get_rect(center=(width / 2, height / 2))
        self.clicked = False

        self.upgradeBtn = pygame.Rect(10, 405, 185, 75)
        self.upgrade1_cost = 5

        self.game_font = pygame.font.Font("fonts/Minecraft.ttf", 20)

    def upgrade(self):
        self.upgrade1_description = self.game_font.render(f"+{self.cookie_per_click} cookie per click", True, "#ffffff")
        self.display_cost = text_font.render(f"Cost:{str(self.upgrade1_cost)}", True, "#ffffff")

        pygame.draw.rect(screen, "#488ebd", self.upgradeBtn, border_radius = 15)
        screen.blit(self.display_cost, (15, 445))
        screen.blit(self.upgrade1_description, (15,410))
    
    def draw_score(self):
        self.display_cookies = self.game_font.render(f"Cookies: {str(self.cookies)}", True, "#a8a8a8")
        screen.blit(self.display_cookies, (5,60))

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.cookies += self.cookie_per_click
                    self.animation_timer = 10
                    self.clicked = False

        if self.upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.upgrade1_cost:
                    upgrade_sound.play()
                    self.cookies -= self.upgrade1_cost
                    self.upgrade1_cost *= 2
                    self.cookie_per_click += 1

        if self.animation_timer > 0:
            self.cookie_size = 180
            self.animation_timer -= 1
        else:
            self.cookie_size = self.original_cookie_size

        self.cookie_image = pygame.transform.scale(
            cookie, (self.cookie_size, self.cookie_size)
        )       

        self.cookie = self.cookie_image.get_rect(
            center=(width / 2, height / 2)
        )

        screen.blit(self.cookie_image, self.cookie)

    def render(self):
        self.click_button()
        self.draw_score()
        self.upgrade()
    
pygame.init()
width = 400
height = 500

screen = pygame.display.set_mode(size=(width,height))
pygame.display.set_caption("Cookie Clicker")
text_font = pygame.font.Font("fonts/Minecraft.ttf", 40)
title = text_font.render("Cookie Clicker", True, "#ea8c8c")
background = pygame.image.load("graphics/background.jpg").convert()
upgrade_sound = pygame.mixer.Sound("audio/level_up.mp3")
cookie = pygame.image.load("graphics/minecraft_cookie.png").convert_alpha()

pygame.mixer.music.load("audio/background_music.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
FPS=60

game = Game()

while True:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(title, (60 ,15))
    game.render()
    pygame.display.update()
    clock.tick(60)