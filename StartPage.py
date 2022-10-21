from turtle import width
import pygame
from sprite import *
from settings import *
from button import Button

#class responsible for start page
class startPage():
    def __init__(self,screen):
        self.screen = screen
        self.screen.fill(BGCOLOUR)
        self.font = pygame.font.Font(None,30)
        button_next = Button('Play',self.font,button_width,button_height,(WIDTH/2-button_width/2,HEIGHT-150),5,self.change_state)
        self.buttons = [button_next]
        self.current = True

    def checkUpdate(self):
        return self.current

    def set_next_page(self, page):
        self.page = page

    def change_state(self):
        self.page.current = True
        self.current = False
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    self.page.current = True
                    self.current = False
            
            self.buttons[0].check_click()

    def draw(self):
        self.buttons[0].draw(self.screen)
        self.create_text()
        self.show_us()
        self.show_rules()


    def show_us(self):
        font_powered = pygame.font.Font("asserts/FerroRosso.ttf", 30)
        font_names = pygame.font.Font("asserts/arial_narrow_7.ttf", 20)
        names = "1-mohamed salama\n\
2-mohamed aiad\n\
3-ahmed abdallah\n\
4-michael samir\n"
        text_powered = font_powered.render("Powered by:", True, (0,0,0))
        self.screen.blit(text_powered,(WIDTH/1.4,HEIGHT/1.1-30,WIDTH,50))
        self.blit_text(self.screen, names, (WIDTH/1.4,HEIGHT/1.1), font_names, (0,0,0))

    def show_rules(self):
        font_rules = pygame.font.Font("asserts/FerroRosso.ttf", 40)
        font_text = pygame.font.Font("asserts/arial_narrow_7.ttf", 25)

        text = "Hi dude this is our 8 puzzle game enjoy it\n\
first press space or the \'play\' button\n\
The 8 puzzle consists of eight numbered, movable tiles set in a 3x3 frame.\n\
One cell of the frame is always empty thus making it possible to move an adjacent numbered tile into the empty cell\n\
The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.\n\
The n-puzzle is a classical problem for modelling algorithms involving heuristics."

        # show example image
        puzzle_image = pygame.image.load("asserts/8-puzzle.png")
        puzzle_image = pygame.transform.scale(puzzle_image, (puzzle_image.get_width()*0.9, puzzle_image.get_height()*0.9))
        imagerect = puzzle_image.get_rect()
        puzzle_image.convert()
        self.screen.blit(puzzle_image, (WIDTH/2-puzzle_image.get_width()/2,HEIGHT-puzzle_image.get_height()-175))


        text_rules = font_rules.render("Rules:", True, (0,0,0))
        self.screen.blit(text_rules,(10,HEIGHT/4-50,WIDTH,50))
        self.blit_text(self.screen, text, (10,HEIGHT/4), font_text, (255,255,255))

    
    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
    
    #write welcome message
    def create_text(self):
        color = (100,200,255)
        self.rect_title = pygame.Rect((0,50,WIDTH,70))
        font = pygame.font.Font("asserts/Arcade.ttf", 60)
        text_title = font.render("8 PUZZLE GAME", True, color)
        text_rect = text_title.get_rect(center=self.rect_title.center)
        self.screen.blit(text_title,text_rect)