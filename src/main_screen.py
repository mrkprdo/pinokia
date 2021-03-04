import pygame
import pygame_menu

class MainScreen:
    def __init__(self):
        pygame.init()
        
    def start(self):
        surface = pygame.display.set_mode((128, 128))

        menu = pygame_menu.Menu(128, 128, 'PiNokia v0.1',
                       theme=self.theming())
        
        menu.add_text_input('Name :', default='John Doe')
        menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
        menu.add_button('Play', None)
        menu.add_button('Quit', pygame_menu.events.EXIT)

        menu.mainloop(surface)

    def set_difficulty(value, difficulty):
        # Do the job here !
        pass

    def start_the_game():
        # Do the job here !
        pass

    def theming(self,selection="dark"):
        theme = pygame_menu.themes.Theme(
                            title_font_size=10,
                            widget_font_size=8,
                            background_color=(40, 41, 35),
                            cursor_color=(255, 255, 255),
                            cursor_selection_color=(80, 80, 80, 120),
                            scrollbar_color=(39, 41, 42),
                            scrollbar_slider_color=(65, 66, 67),
                            selection_color=(255, 255, 255),
                            title_background_color=(47, 48, 51),
                            title_font_color=(215, 215, 215),
                            widget_font_color=(200, 200, 200)
                    )
        return theme if selection == "dark" else pygame_menu.themes.Theme()