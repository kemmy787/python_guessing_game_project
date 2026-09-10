"""Tests for graphical map rendering."""

import pygame

from game.resource import ResourceNode
from window import BOARD_SIZE, RESOURCE_COLORS, draw_resource


def test_draw_resource_renders_type_marker_and_amount():
        pygame.font.init()
        screen = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 18)
        resource = ResourceNode((0, 0), "gold", amount=25)

        draw_resource(screen, resource, screen.get_rect(), font)

        assert screen.get_at((BOARD_SIZE // 2, BOARD_SIZE // 2 - 12))[:3] == (
                RESOURCE_COLORS["gold"]
        )