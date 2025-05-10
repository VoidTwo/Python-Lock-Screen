# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from typing import TYPE_CHECKING

# 3rd party imports
from pygame import (
    constants as pyg_constants,
    display as pyg_display,
    event as pyg_event)
from pygame.mouse import set_visible as pyg_mouse_set_visible
from pygame.time import Clock as pyg_Clock

# Type checking
if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface


def game_loop() -> None:
    game_running: bool = True
    game_clock: pyg_Clock = pyg_Clock()

    unlock_keys: frozenset[int] = frozenset((
        pyg_constants.K_LCTRL, pyg_constants.K_LALT, pyg_constants.K_RALT, pyg_constants.K_RCTRL))
    unlock_keys_length: int = len(unlock_keys)
    pressed_unlock_keys: int = 0

    while game_running:
        event: Event

        for event in pyg_event.get():
            if event.type == pyg_constants.KEYDOWN:
                if event.key in unlock_keys:
                    pressed_unlock_keys += 1
            elif event.type == pyg_constants.KEYUP:
                if event.key in unlock_keys:
                    pressed_unlock_keys -= 1

        if pressed_unlock_keys == unlock_keys_length:
            game_running = False
        else:
            game_clock.tick(60)  # Significantly reduce CPU usage

    pyg_event.clear()
    return


def main() -> None:
    pyg_display.init()

    screen: Surface = pyg_display.set_mode((0, 0), flags=pyg_constants.SHOWN | pyg_constants.FULLSCREEN, depth=1)
    pyg_display.set_caption('Python Lock Screen')
    pyg_display.set_allow_screensaver(False)  # Prevent OS screen saver from activating

    screen.fill((0, 0, 0))  # Black screen
    screen.set_clip((0, 0, 0, 0))  # Set modifiable pixels

    pyg_event.set_blocked(None)  # Blocks ALL event types
    pyg_event.set_allowed((pyg_constants.KEYDOWN, pyg_constants.KEYUP))  # Enable desired event types
    pyg_mouse_set_visible(False)  # Hide cursor

    pyg_event.set_grab(True)
    game_loop()
    pyg_event.set_grab(False)
    return


if __name__ == '__main__':
    main()
