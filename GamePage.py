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

        self.button_input = Button('Input',self.font,button_width,button_height,(WIDTH/2+5,HEIGHT-100),5,self.take_input)
        self.button_done = Button('Done',self.font,button_width,button_height,(WIDTH/2+button_width+7.5,550),5,self.done_input)
        self.button_solve = Button('Solve',self.font,button_width,button_height,(WIDTH/2-button_width-10,HEIGHT-100),5,self.solve)
        self.button_shuffle = Button('Shuffle',self.font,button_width,button_height,(WIDTH/2-button_width-10,HEIGHT-50),5,self.shuffle_click)
        self.button_reset = Button('Reset',self.font,button_width,button_height,(WIDTH/2+5,HEIGHT-50),5,self.reset)
        self.button_next = Button('Next',self.font,button_width,button_height,(WIDTH/2+button_width+7.5,550),5,self.next)
        self.button_previous = Button('Prev',self.font,button_width,button_height,(WIDTH/2-2*button_width-7.5,550),5,self.previous)
        self.button_resume = Button('Resume',self.font,button_width,button_height,(WIDTH/2+2.5,550),5,self.resume)
        self.button_pause = Button('Pause',self.font,button_width,button_height,(WIDTH/2-button_width-2.5,550),5,self.pause)
        self.buttons_list = [self.button_solve,self.button_shuffle,self.button_reset, self.button_input]
        self.result_buttons_list = [self.button_pause,self.button_next,self.button_previous,self.button_resume]

        self.expanded_nodes = 0
        self.search_depth = 0

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
        self.algorithm = A_star_search()
        self.selected_algo = "a*"
        self.input_mode = False
        self.input_grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.selected = 0,0
        self.textC = ""
        self.wrong_input = False
        self.Solvable = True
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

    def done_input(self):
        res = self.node.ValidateInput(self.input_grid)
        if(res == False):
            self.Solvable = True
            self.wrong_input = True
        elif(not self.node.isSolvable(res)):
            self.Solvable = False
            self.wrong_input = False
        else:
            self.wrong_input = False
            self.start_game = True
            self.tiles_grid = res
            self.elapsed_time = 0
            self.input_mode = False
            self.start_show_result = False
            self.show_result_buttons = False
            self.start_timer = True
            self.buttons_list.pop()
            self.button_solve.enable()
            self.button_shuffle.enable()

    def solve(self):
        self.elapsed_time = time.time()
        self.path = self.algorithm.solve(self.tiles_grid)
        self.elapsed_time = time.time()-self.elapsed_time
        self.start_game = False
        self.input_mode = False
        self.current_step = -1
        self.resume()
        self.show_result_buttons = True
        self.expanded_nodes = self.algorithm.number_of_expanded_nodes
        self.search_depth = self.algorithm.depth_of_search_tree
        print("expanded nodes: ", self.algorithm.number_of_expanded_nodes)
        print("path length: ",len(self.path))
        self.button_solve.disable()

    def take_input(self):
        self.elapsed_time = 0
        self.start_game = False
        self.input_mode = True
        self.start_show_result = False
        self.show_result_buttons = False
        self.tiles_grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.buttons_list.append(self.button_done)
        self.button_solve.disable()
        self.button_shuffle.disable()
        self.draw_tiles()

    def next(self):
        if((self.current_step-1)*-1 > len(self.path)):
            return
        elif((self.current_step-1)*-1 == len(self.path)):
            self.button_next.disable()
        elif((self.current_step+1) < -1):
            self.button_previous.enable()
        
        self.tiles_grid = self.node.strTO2dArray(self.path[self.current_step-1])
        self.current_step -= 1
        self.draw_tiles()

    def previous(self):
        if(self.current_step+1 > -1):
            return
        elif(self.current_step+1 == -1):
            self.button_previous.disable()
        elif((self.current_step-1)*-1 < len(self.path)):
            self.button_next.enable()
        
        self.tiles_grid = self.node.strTO2dArray(self.path[self.current_step+1])
        self.current_step += 1
        self.draw_tiles()
    
    def pause(self):
        self.pause_show_result = True
        self.result_buttons_list[0].disable()
        for button in range(1,4):
            self.result_buttons_list[button].enable()

    def resume(self):
        self.start_show_result = True
        self.pause_show_result = False
        self.input_mode = False
        self.result_buttons_list[0].enable()
        for button in range(1,4):
            self.result_buttons_list[button].disable()

    def change_algorithm(self,algo):
        self.algorithm = self.Factory(algo)

    def shuffle_click(self):
        self.win = False
        self.shuffle_counter = 0
        self.start_shuffle = True 
        self.start_show_result = False
        self.show_result_buttons = False
        self.input_mode = False

    def reset(self):
        self.win = False
        self.start_show_result = False
        self.show_result_buttons = False
        self.input_mode = False
        self.Solvable = True
        if len(self.buttons_list) > 4 :
            self.buttons_list.pop()
        self.button_shuffle.enable()
        self.button_solve.enable()
        self.new()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if(self.input_mode):
                    keys = list(pygame.key.get_pressed())
                    index = keys.index(1)
                    if pygame.key.get_pressed()[pygame.K_BACKSPACE] and len(self.textC)>0:
                        self.textC = self.textC[:-1] # removes last letter
                    else:
                        self.textC += event.unicode # adds letter
                    self.input_grid[self.selected[0]][self.selected[1]] = str(self.textC)
                    self.draw_tiles(self.input_grid)

                if(not self.input_mode):   
                    if(event.key == pygame.K_d):
                        print("dfs")
                        self.selected_algo = "dfs"
                        self.change_algorithm("DFS")
                    if(event.key == pygame.K_b):
                        print("bfs")
                        self.selected_algo = "bfs"
                        self.change_algorithm("BFS")
                    if(event.key == pygame.K_a):
                        print("A*")
                        self.selected_algo = "a*"
                        self.change_algorithm("A*")
                    if(event.key == pygame.K_m):
                        self.algorithm.set_heuristic("manhattan")
                        print("manhattan")
                    if(event.key == pygame.K_e):
                        self.algorithm.set_heuristic("euclidean")
                        print("euclidean")
            
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
                            if(self.input_mode):
                                if(self.input_grid[self.selected[0]][self.selected[1]] == ""):
                                    self.input_grid[self.selected[0]][self.selected[1]] = 0
                                self.selected = row, col
                                self.textC = ""
                                self.input_grid[row][col] = ""
                                self.draw_tiles(self.input_grid)
                                break

                            if tile.right() and self.tiles_grid[row][col + 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]

                            if tile.left() and self.tiles_grid[row][col - 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]

                            if tile.up() and self.tiles_grid[row - 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]

                            if tile.down() and self.tiles_grid[row + 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]
                            self.draw_tiles()
    
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

    def draw_tiles(self, grid = []):
        self.tiles = []
        if(grid == []):
            grid = self.tiles_grid
        for row, x in enumerate(grid):
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
        UIElement(10, 150, "TIME:", WHITE).draw(self.screen)
        UIElement(10, 180, "%.3f" % self.elapsed_time, WHITE).draw(self.screen)
        UIElement(10, 220, "BEST:", WHITE).draw(self.screen)
        UIElement(10, 250, "%.3f" % (self.high_score if self.high_score > 0 else 0), WHITE).draw(self.screen)
        UIElement(WIDTH-120, 150, "DFS", GREEN if self.selected_algo == "dfs" else WHITE).draw(self.screen)
        UIElement(WIDTH-120, 180, "BFS", GREEN if self.selected_algo == "bfs" else WHITE).draw(self.screen)
        UIElement(WIDTH-120, 210, "A*", GREEN if self.selected_algo == "a*" else WHITE).draw(self.screen)

        if(self.start_show_result):
            UIElement(10, 600, "No. of steps: %d" % len(self.path), WHITE).draw(self.screen)
            UIElement(10, 630, "No. of expanded nodes: %d" %self.expanded_nodes , WHITE).draw(self.screen)
            UIElement(10, 660, "Search depth: %d" % self.search_depth, WHITE).draw(self.screen)

        if(self.wrong_input):
            UIElement(10, 600, "Wrong board please try again", WHITE).draw(self.screen)
        if(not self.Solvable):
            UIElement(10, 600, "board is not solvable", WHITE).draw(self.screen)
        # if(self.win):
        #     UIElement(10, 600, "YOU WIN 555555555 !!!!!").draw(self.screen)
        pygame.display.flip()

