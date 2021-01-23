import pygame

from ship import Ship

from settings import Settings

import game_functions as gf

from alien import Alien

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
    alien = Alien(ai_settings, screen)


    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        #删除已消失
        gf.update_bullet(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


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



