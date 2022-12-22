# Future imports
from __future__ import annotations

# Standard imports
from typing import TYPE_CHECKING

# 3rd party imports
from pygame import (
    display as pyg_display,
    event as pyg_event)
from pygame.constants import (
    FULLSCREEN as PYG_FULLSCREEN,
    K_LALT as PYG_K_LALT,
    K_LCTRL as PYG_K_LCTRL,
    K_RALT as PYG_K_RALT,
    K_RCTRL as PYG_K_RCTRL,
    KEYDOWN as PYG_KEYDOWN,
    KEYUP as PYG_KEYUP,
    SHOWN as PYG_SHOWN)
from pygame.mouse import set_visible as pyg_mouse_set_visible
from pygame.time import Clock as pyg_Clock

# Type checking
if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface


def game_loop() -> None:
    game_running: bool = True
    game_clock: pyg_Clock = pyg_Clock()

    unlock_keys: frozenset[int] = frozenset((PYG_K_LCTRL, PYG_K_LALT, PYG_K_RALT, PYG_K_RCTRL))
    unlock_keys_length: int = len(unlock_keys)
    pressed_unlock_keys: int = 0

    while game_running:
        event: Event

        for event in pyg_event.get():
            if event.type == PYG_KEYDOWN:
                if event.key in unlock_keys:
                    pressed_unlock_keys += 1
            elif event.type == PYG_KEYUP:
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

    screen: Surface = pyg_display.set_mode((0, 0), flags=PYG_SHOWN | PYG_FULLSCREEN, depth=1)
    pyg_display.set_caption('Python Lock Screen')
    pyg_display.set_allow_screensaver(False)  # Prevent OS screen saver from activating

    screen.fill((0, 0, 0))  # Black screen
    screen.set_clip((0, 0, 0, 0))  # Set modifiable pixels

    pyg_event.set_blocked(None)  # Blocks ALL event types
    pyg_event.set_allowed((PYG_KEYDOWN, PYG_KEYUP))  # Enable desired event types
    pyg_mouse_set_visible(False)  # Hide cursor

    pyg_event.set_grab(True)
    game_loop()
    pyg_event.set_grab(False)
    return


if __name__ == '__main__':
    main()
