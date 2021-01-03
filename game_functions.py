import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    """ 响应按键"""
    if event.key == pygame.K_RIGHT:
        """向右移动飞机"""
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        """向左移动飞机"""
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:



def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    bullets.draw_bullet()
    pygame.display.flip()