from os import wait
import pygame
import random
import time
from sprite import *
from settings import *
from button import Button
from bfs_search import bfs
from dfs_search import dfs
from node import node
from A_star import A_star_search

#class responsible for start page
class gamePage():
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.Font(None,30)

        self.button_solve = Button('Solve',self.font,button_width,button_height,(WIDTH/2-button_width/2,HEIGHT-100),5,self.solve)
        self.button_shuffle = Button('Shuffle',self.font,button_width,button_height,(WIDTH/2-button_width-10,HEIGHT-50),5,self.shuffle_click)
        self.button_reset = Button('Reset',self.font,button_width,button_height,(WIDTH/2+5,HEIGHT-50),5,self.reset)
        self.button_next = Button('Next',self.font,button_width,button_height,(WIDTH/2+button_width+7.5,550),5,self.next)
        self.button_previous = Button('Prev',self.font,button_width,button_height,(WIDTH/2-2*button_width-7.5,550),5,self.previous)
        self.button_resume = Button('Resume',self.font,button_width,button_height,(WIDTH/2+2.5,550),5,self.resume)
        self.button_pause = Button('Pause',self.font,button_width,button_height,(WIDTH/2-button_width-2.5,550),5,self.pause)
        self.buttons_list = [self.button_solve,self.button_shuffle,self.button_reset]
        self.result_buttons_list = [self.button_pause,self.button_next,self.button_previous,self.button_resume]

        self.shuffle_counter = 0
        self.show_time = 0
        self.start_shuffle = False
        self.previous_choice = ""
        self.start_game = False
        self.start_timer = False
        self.elapsed_time = 0
        self.current = False
        self.win = False
        self.start_show_result = False
        self.pause_show_result = False
        self.show_result_buttons = False
        self.path = [[[]]]
        self.current_step = -1
        self.high_score = float(self.get_high_scores()[0])
        self.algorithm = bfs()
        self.node = node()

    def Factory(self, input ="DFS"):   
        
        """Factory Method"""  
        localizers = {   
            "DFS": dfs,
            "BFS": bfs,
            "A*" : A_star_search,
        }   
        return localizers[input]()

    def get_high_scores(self):
        with open("asserts/high_score.txt", "r") as file:
            scores = file.read().splitlines()
        return scores

    def save_score(self):
        with open("asserts/high_score.txt", "w") as file:
            file.write(str("%.3f\n" % self.high_score))

    def checkUpdate(self):
        return self.current
        
    def solve(self):
        self.elapsed_time = time.time()
        self.path = self.algorithm.solve(self.tiles_grid)
        self.elapsed_time = time.time()-self.elapsed_time
        self.start_game = False
        self.resume()
        self.show_result_buttons = True
        print("expanded nodes: ", self.algorithm.number_of_expanded_nodes)
        print("path length: ",len(self.path))
        self.button_solve.disable()

    def take_input(self):
        pass

    def next(self):
        pass

    def previous(self):
        pass

    def pause(self):
        self.pause_show_result = True
        self.result_buttons_list[0].disable()
        for button in range(1,4):
            self.result_buttons_list[button].enable()

    def resume(self):
        self.start_show_result = True
        self.pause_show_result = False
        self.result_buttons_list[0].enable()
        for button in range(1,4):
            self.result_buttons_list[button].disable()

    def change_algorithm(self,algo):
        self.algorithm = self.Factory(algo)

    def shuffle_click(self):
        self.win = False
        self.shuffle_counter = 0
        self.start_shuffle = True 

    def reset(self):
        self.win = False
        self.button_solve.enable()
        self.new()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    print("a7aaaaaaaa")
                
                if(event.key == pygame.K_d):
                    print("dfs")
                    self.change_algorithm("DFS")
                if(event.key == pygame.K_b):
                    print("bfs")
                    self.change_algorithm("BFS")
                if(event.key == pygame.K_a):
                    print("A*")
                    self.change_algorithm("A*")
                if(event.key == pygame.K_m):
                    self.algorithm.set_heuristic("manhattan")
                if(event.key == pygame.K_e):
                    self.algorithm.set_heuristic("euclidean")
            
            for button in self.buttons_list:
                button.check_click()

            if(self.start_show_result):
                for button in self.result_buttons_list:
                    button.check_click()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if tile.click(mouse_x, mouse_y):
                            if tile.right() and self.tiles_grid[row][col + 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]

                            if tile.left() and self.tiles_grid[row][col - 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]

                            if tile.up() and self.tiles_grid[row - 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]

                            if tile.down() and self.tiles_grid[row + 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]
                            self.draw_tiles()
            


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
    
    #write title
    def create_text(self):
        color = (100,200,255)
        self.rect_title = pygame.Rect((0,50,WIDTH,70))
        font = pygame.font.Font("asserts/Arcade.ttf", 60)
        text_title = font.render("8 PUZZLE GAME", True, color)
        text_rect = text_title.get_rect(center=self.rect_title.center)
        self.screen.blit(text_title,text_rect)

    def create_game(self):
        grid = [[x + y * GAME_SIZE for x in range(0, GAME_SIZE)] for y in range(GAME_SIZE)]
        grid[0][0] = 0
        return grid
    
    def shuffle(self):
        possible_moves = []
        self.start_show_result = False
        self.button_solve.enable()
        for row, tiles in enumerate(self.tiles):
            for col, tile in enumerate(tiles):
                if tile.text == "empty":
                    if tile.right():
                        possible_moves.append("right")
                    if tile.left():
                        possible_moves.append("left")
                    if tile.up():
                        possible_moves.append("up")
                    if tile.down():
                        possible_moves.append("down")
                    break
            if len(possible_moves) > 0:
                break

        if self.previous_choice == "right":
            possible_moves.remove("left") if "left" in possible_moves else possible_moves
        elif self.previous_choice == "left":
            possible_moves.remove("right") if "right" in possible_moves else possible_moves
        elif self.previous_choice == "up":
            possible_moves.remove("down") if "down" in possible_moves else possible_moves
        elif self.previous_choice == "down":
            possible_moves.remove("up") if "up" in possible_moves else possible_moves

        choice = random.choice(possible_moves)
        self.previous_choice = choice
        if choice == "right":
            self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], \
                                                                       self.tiles_grid[row][col]
        elif choice == "left":
            self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], \
                                                                       self.tiles_grid[row][col]
        elif choice == "up":
            self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], \
                                                                       self.tiles_grid[row][col]
        elif choice == "down":
            self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], \
                                                                       self.tiles_grid[row][col]
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.create_game()
        self.elapsed_time = 0
        self.start_timer = False
        self.start_game = False
        self.draw_tiles()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if self.start_game:
            if self.tiles_grid == self.tiles_grid_completed:
                self.win = True
                self.start_game = False
                if self.high_score > 0:
                    self.high_score = self.elapsed_time if self.elapsed_time < self.high_score else self.high_score
                else:
                    self.high_score = self.elapsed_time
                self.save_score()

            if self.start_timer:
                self.timer = time.time()
                self.start_timer = False
            self.elapsed_time = time.time() - self.timer

        if self.start_show_result and not self.pause_show_result:
            if(len(self.path) >= self.current_step*-1 and (time.time()-self.show_time) >= 0.5):
                self.tiles_grid = self.node.strTO2dArray(self.path[self.current_step])
                self.current_step -= 1
                self.draw_tiles()
                self.show_time = time.time()

        if self.start_shuffle:
            self.shuffle()
            self.draw_tiles()
            self.shuffle_counter += 1
            if self.shuffle_counter > 120:
                self.start_shuffle = False
                self.start_game = True
                self.start_timer = True

        self.all_sprites.update()

    def draw_grid(self):
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (col+WIDTH/2-(GAME_SIZE * TILESIZE)/2, 150), (col+WIDTH/2-(GAME_SIZE * TILESIZE)/2, GAME_SIZE * TILESIZE+150), 4)
        for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (WIDTH/2-(GAME_SIZE * TILESIZE)/2, row+150), (GAME_SIZE * TILESIZE+ WIDTH/2-(GAME_SIZE * TILESIZE)/2, row+150), 4)

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "empty"))

    def draw(self):
        self.screen.fill(BGCOLOUR)
        for button in self.buttons_list:
            button.draw(self.screen)
        
        if(self.show_result_buttons):
            for button in self.result_buttons_list:
                button.draw(self.screen)
        
        self.create_text()
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        UIElement(10, 150, "TIME:").draw(self.screen)
        UIElement(10, 180, "%.3f" % self.elapsed_time).draw(self.screen)
        UIElement(10, 220, "BEST:").draw(self.screen)
        UIElement(10, 250, "%.3f" % (self.high_score if self.high_score > 0 else 0)).draw(self.screen)
        if(self.start_show_result):
            UIElement(10, 600, "No. of steps: %d" % len(self.path)).draw(self.screen)
            UIElement(10, 630, "No. of expanded nodes: %d" % self.algorithm.number_of_expanded_nodes).draw(self.screen)
            UIElement(10, 660, "Search depth: %d" % self.algorithm.depth_of_search_tree).draw(self.screen)
            UIElement(10, 690, "YOU WIN 555555555 !!!!!").draw(self.screen)

        # UIElement(10, 550, "Press A for A*, D for dfs, B for bfs").draw(self.screen)
        # if(self.win):
        #     UIElement(10, 600, "YOU WIN 555555555 !!!!!").draw(self.screen)
        pygame.display.flip()

