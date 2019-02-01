import random
import sys
import pygame

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class SpaceLlamaGame():
    """

    About a llama who isn't afraid to take his protein pills.

    """
    background = Background('img/stars.jpg', [0,0])
    loading_screen = pygame.image.load("img/banner.png")
    space_llama = pygame.image.load("img/space-llama.png")
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    def __init__(self,width=640,height=480):
        """
        Set up the game.
        
        :param width: width of screen
        :param height: height of screen

        """
        self.width = width
        self.height = height
        pygame.mixer.init()
        pygame.mixer.music.load('audio/space-oddity.mp3')
        pygame.mixer.music.play()
        print("Playing")
        pygame.event.wait()


    def run(self):
        """
        Runs the damn game.
        :return: Null
        """
        llama_box = self.space_llama.get_rect()
        speed = [4, 4]
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    sys.exit()

            loading_screen_box = self.loading_screen.get_rect(center=(self.width / 2, self.height / 2))

            llama_box = llama_box.move(speed)
            print(llama_box)
            if llama_box.left < 0 or llama_box.right > self.width:
                speed[0] = -speed[0]
            if llama_box.top < 0 or llama_box.bottom > self.height:
                speed[1] = -speed[1]

            self.screen.blit(self.background.image, self.background.rect)
            self.screen.blit(self.space_llama, llama_box)
            self.screen.blit(self.loading_screen, loading_screen_box)
            pygame.display.flip()

game = SpaceLlamaGame(1280, 720)
game.run()