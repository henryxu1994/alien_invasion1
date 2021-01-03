import pygame

from ship import Ship

from settings import Settings

import game_functions as gf

from pygame.sprite import Group


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)

    bullets = Group()


    #开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


"""
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #screen.fill(bg_color)
            screen.fill(ai_settings.bg_color)
            """


            #让最近绘制的屏幕可见


run_game()



