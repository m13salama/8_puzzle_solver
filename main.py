import pygame
from sprite import *
from settings import *
from StartPage import startPage
from GamePage import gamePage

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def Factory(input ="Start"):   
  
   """Factory Method"""  
   localizers = {   
      "Start": startPage,
      "Game": gamePage,
   }   
   page = localizers[input](screen)  

def main():    
    pygame.display.set_caption(title)

    game_page = gamePage(screen)
    start_page = startPage(screen)
    start_page.set_next_page(game_page)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        if(start_page.checkUpdate()):
            start_page.events()
            start_page.draw()
        
        if(game_page.checkUpdate()):
            game_page.new()
            while(1):
                game_page.events()
                game_page.update()
                game_page.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()

# game = Game()
# while True:
#     game.new()
#     game.run()