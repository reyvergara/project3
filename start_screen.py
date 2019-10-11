import pygame.font


class Start:

    def __init__(self, screen, title, txt_size, y_offset):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Color of title text
        self.title_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, txt_size)

        # self.title_display(title)
        self.title_image = self.font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = (self.screen_rect.x, self.screen_rect.y-y_offset)

    def title_display(self, title, y_offset):
        self.title_image = self.font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = (self.screen_rect.x, self.screen_rect.y-y_offset)
        self.screen.blit(self.title_image)
