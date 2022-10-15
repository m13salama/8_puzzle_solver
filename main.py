import pygame
import random
import time
from sprite import *
from settings import *
from button import Button

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#class responsible for start page
class startPage():
    def __init__(self):
        self.screen = screen
        screen.fill(BGCOLOUR)
        self.font = pygame.font.Font(None,30)
        button_next = Button('Play',self.font,button_width,button_height,(WIDTH/2-button_width/2,HEIGHT-300),5,self.change_state)
        self.buttons = [button_next]
    def change_state(self):
        global page
        # page = Factory("Main")
        print("a7aaaaaaa")
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                print("main")
                global page
                # page = Factory("Main")
                print("a7aaaaaaaa")
        self.buttons[0].check_click()

    def draw(self):
        self.buttons[0].draw(screen)
        self.create_text()
        self.show_us()
        self.show_rules()


    def show_us(self):
        font_powered = pygame.font.Font("FerroRosso.ttf", 20)
        font_names = pygame.font.Font("arial_narrow_7.ttf", 15)
        names = "1-mohamed salama\n\
2-mohamed aiad\n\
3-ahmed abdallah\n\
4-michael samir\n"
        text_powered = font_powered.render("Powered by:", True, (0,0,0))
        self.screen.blit(text_powered,(WIDTH/1.3,HEIGHT/1.15-20,WIDTH,50))
        self.blit_text(self.screen, names, (WIDTH/1.3,HEIGHT/1.15), font_names, (0,0,0))

    def show_rules(self):
        font_rules = pygame.font.Font("FerroRosso.ttf", 40)
        font_text = pygame.font.Font("arial_narrow_7.ttf", 25)
        names = "Hi dude this is our 8 puzzle game enjoy it\n\
first press space or the \'play\' button\n\
The 8 puzzle consists of eight numbered, movable tiles set in a 3x3 frame.\n\
One cell of the frame is always empty thus making it possible to move an adjacent numbered tile into the empty cell"
        text_rules = font_rules.render("Rules:", True, (0,0,0))
        self.screen.blit(text_rules,(10,HEIGHT/4-50,WIDTH,50))
        self.blit_text(self.screen, names, (10,HEIGHT/4), font_text, (255,255,255))

    
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
        font = pygame.font.Font("Arcade.ttf", 60)
        text_title = font.render("8 PUZZLE GAME", True, color)
        text_rect = text_title.get_rect(center=self.rect_title.center)
        self.screen.blit(text_title,text_rect)


# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption(title)
#         self.clock = pygame.time.Clock()
#         self.shuffle_time = 0
#         self.start_shuffle = False
#         self.previous_choice = ""
#         self.start_game = False
#         self.start_timer = False
#         self.elapsed_time = 0
#         self.high_score = float(self.get_high_scores()[0])

#     def get_high_scores(self):
#         with open("high_score.txt", "r") as file:
#             scores = file.read().splitlines()
#         return scores

#     def save_score(self):
#         with open("high_score.txt", "w") as file:
#             file.write(str("%.3f\n" % self.high_score))

#     def create_game(self):
#         grid = [[x + y * GAME_SIZE for x in range(1, GAME_SIZE + 1)] for y in range(GAME_SIZE)]
#         grid[-1][-1] = 0
#         return grid

#     def shuffle(self):
#         possible_moves = []
#         for row, tiles in enumerate(self.tiles):
#             for col, tile in enumerate(tiles):
#                 if tile.text == "empty":
#                     if tile.right():
#                         possible_moves.append("right")
#                     if tile.left():
#                         possible_moves.append("left")
#                     if tile.up():
#                         possible_moves.append("up")
#                     if tile.down():
#                         possible_moves.append("down")
#                     break
#             if len(possible_moves) > 0:
#                 break

#         if self.previous_choice == "right":
#             possible_moves.remove("left") if "left" in possible_moves else possible_moves
#         elif self.previous_choice == "left":
#             possible_moves.remove("right") if "right" in possible_moves else possible_moves
#         elif self.previous_choice == "up":
#             possible_moves.remove("down") if "down" in possible_moves else possible_moves
#         elif self.previous_choice == "down":
#             possible_moves.remove("up") if "up" in possible_moves else possible_moves

#         choice = random.choice(possible_moves)
#         self.previous_choice = choice
#         if choice == "right":
#             self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], \
#                                                                        self.tiles_grid[row][col]
#         elif choice == "left":
#             self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], \
#                                                                        self.tiles_grid[row][col]
#         elif choice == "up":
#             self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], \
#                                                                        self.tiles_grid[row][col]
#         elif choice == "down":
#             self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], \
#                                                                        self.tiles_grid[row][col]

#     def draw_tiles(self):
#         self.tiles = []
#         for row, x in enumerate(self.tiles_grid):
#             self.tiles.append([])
#             for col, tile in enumerate(x):
#                 if tile != 0:
#                     self.tiles[row].append(Tile(self, col, row, str(tile)))
#                 else:
#                     self.tiles[row].append(Tile(self, col, row, "empty"))

#     def new(self):
#         self.all_sprites = pygame.sprite.Group()
#         self.tiles_grid = self.create_game()
#         self.tiles_grid_completed = self.create_game()
#         self.elapsed_time = 0
#         self.start_timer = False
#         self.start_game = False
#         self.buttons_list = []
#         self.buttons_list.append(Button(500, 100, 200, 50, "Shuffle", WHITE, BLACK))
#         self.buttons_list.append(Button(500, 170, 200, 50, "Reset", WHITE, BLACK))
#         self.draw_tiles()

#     def run(self):
#         self.playing = True
#         while self.playing:
#             self.clock.tick(FPS)
#             self.events()
#             self.update()
#             self.draw()

#     def update(self):
#         if self.start_game:
#             if self.tiles_grid == self.tiles_grid_completed:
#                 self.start_game = False
#                 if self.high_score > 0:
#                     self.high_score = self.elapsed_time if self.elapsed_time < self.high_score else self.high_score
#                 else:
#                     self.high_score = self.elapsed_time
#                 self.save_score()

#             if self.start_timer:
#                 self.timer = time.time()
#                 self.start_timer = False
#             self.elapsed_time = time.time() - self.timer

#         if self.start_shuffle:
#             self.shuffle()
#             self.draw_tiles()
#             self.shuffle_time += 1
#             if self.shuffle_time > 120:
#                 self.start_shuffle = False
#                 self.start_game = True
#                 self.start_timer = True

#         self.all_sprites.update()

#     def draw_grid(self):
#         for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
#             pygame.draw.line(self.screen, LIGHTGREY, (row, 0), (row, GAME_SIZE * TILESIZE))
#         for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
#             pygame.draw.line(self.screen, LIGHTGREY, (0, col), (GAME_SIZE * TILESIZE, col))

#     def draw(self):
#         self.screen.fill(BGCOLOUR)
#         self.all_sprites.draw(self.screen)
#         self.draw_grid()
#         for button in self.buttons_list:
#             button.draw(self.screen)
#         UIElement(550, 35, "%.3f" % self.elapsed_time).draw(self.screen)
#         UIElement(430, 300, "High Score - %.3f" % (self.high_score if self.high_score > 0 else 0)).draw(self.screen)
#         pygame.display.flip()

#     def events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit(0)

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 for row, tiles in enumerate(self.tiles):
#                     for col, tile in enumerate(tiles):
#                         if tile.click(mouse_x, mouse_y):
#                             if tile.right() and self.tiles_grid[row][col + 1] == 0:
#                                 self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]

#                             if tile.left() and self.tiles_grid[row][col - 1] == 0:
#                                 self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]

#                             if tile.up() and self.tiles_grid[row - 1][col] == 0:
#                                 self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]

#                             if tile.down() and self.tiles_grid[row + 1][col] == 0:
#                                 self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]

#                             self.draw_tiles()

#                 for button in self.buttons_list:
#                     if button.click(mouse_x, mouse_y):
#                         if button.text == "Shuffle":
#                             self.shuffle_time = 0
#                             self.start_shuffle = True
#                         if button.text == "Reset":
#                             self.new()





def Factory(page ="Start"):   
  
   """Factory Method"""  
   localizers = {   
      "Start": startPage,
   }   
  
   return localizers[page]()  

def main():
    global page
    page = Factory("Start")
    
    pygame.display.set_caption(title)
    run = True
    clock = pygame.time.Clock()
    fps = 60.0
    START_PAGE = True
    global MAIN_PAGE

    while run:
        clock.tick(fps)
        if(START_PAGE):
            for event in pygame.event.get():
                page.handle_event(event)
            page.draw()


        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()

# game = Game()
# while True:
#     game.new()
#     game.run()