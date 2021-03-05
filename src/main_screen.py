import os
import sys
import pygame
import pygame_menu
from pygame_menu.widgets.widget import SurfaceWidget

from datetime import datetime

class MainScreen:
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M")
        self.h = 0
        pygame.init()

    def start(self):
        self.surface = pygame.display.set_mode((128, 128))
        self.surface_widgets = SurfaceWidget(
            surface=self.surface
        )
        self.main = pygame_menu.Menu(128, 128, f'PiNokia         {self.time}',
                       theme=self.theming(),
                       mouse_visible=False,
                       )
        
        # menu.add_text_input('Name :', default='John Doe')
        # menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
        # menu.add_button('Play', None)
        # menu.add_button('Quit', pygame_menu.events.EXIT)\
        media_path = os.path.join(os.path.dirname(__file__), "..", "media")
        wallpaper = os.path.join(media_path, "pinokia.jpg")
        battery = os.path.join(media_path, "battery.png")
        
        self.main.add_image(wallpaper, scale=(0.4, 0.4))
        self.main.add_image(battery, scale=(1, 1),align=pygame_menu.locals.ALIGN_TOP)

        self.main.add_button('Menu',action=None,align=pygame_menu.locals.ALIGN_CENTER)

        self.main.mainloop(self.surface,bgfun=self.update,fps_limit=60)

    def update(self):
        self.time = datetime.now().strftime("%H:%M")
        menu_bar = self.main.get_menubar()
        menu_bar.set_title(f'PiNokia          {self.time}')

    def set_difficulty(value, difficulty):
        # Do the job here !
        pass

    def start_the_game():
        # Do the job here !
        pass

    def theming(self,selection="dark"):
        theme = pygame_menu.themes.Theme(
                            title_font_size=8,
                            widget_font_size=10,
                            background_color=(40, 41, 35),
                            cursor_color=(255, 255, 255),
                            cursor_selection_color=(80, 80, 80, 120),
                            scrollbar_color=(39, 41, 42),
                            scrollbar_slider_color=(65, 66, 67),
                            selection_color=(255, 255, 255),
                            title_background_color=(40, 41, 35),
                            title_font_color=(215, 215, 215),
                            widget_font_color=(200, 200, 200)
                    )
        return theme if selection == "dark" else pygame_menu.themes.Theme()