import pygame
import frogger

def main():
    pygame.font.init()
    game = frogger.Frogger()
    game.main_loop()

if __name__ == "__main__":
    main()