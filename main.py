from classses import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.Clock()
        
        self.group = pygame.sprite.Group()
        Car(self.group)
        
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            self.screen.fill('bisque')
            
            self.group.update(self.dt)
            self.group.draw(self.screen)
            
            pygame.display.flip()
            
            
Game().run()
            