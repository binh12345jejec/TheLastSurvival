import pygame
import sys
BLUE = (0,0,255)
class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width=1064
        self.height =712
        self.options = {}
        self.clicked = False
        self.command = None
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Menu")
       

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        return self.command

    def add_option(self,label,width,height,x,y,command):
        surface = pygame.Surface((width,height))
        surface.fill((255,255,255))
        rect = pygame.Rect(x,y,width,height)
        self.options[label] = {
                                'label':label,
                                'surface':surface,
                                'rect':rect,
                                'command':command
                            }
    def update(self):
        for option in self.options:
            if self.options[option]['rect'].collidepoint((self.mx,self.my)):
                self.options[option]['surface'].set_alpha(255)
                if self.clicked:
                    self.running = False
                    self.command = self.options[option]['command']
            else:
                self.options[option]['surface'].set_alpha(0)
    def events(self):
        self.mx,self.my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.clicked=True
            else:
                self.clicked=False
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_text("Menu",self.font,50,(255,0,0),self.width//2, 50,align="center")
        for option in self.options:
            self.screen.blit(self.options[option]["surface"], self.options[option]["rect"])
            self.draw_text(self.options[option]["label"],self.font,50,(255,0,0),self.options[option]["rect"].x, self.options[option]["rect"].y)
        pygame.display.update()
m= Menu()
m.add_option("PLAY",500,50,m.width//2,300,"play")
m.add_option("SETTINGS",500,50,m.width//2,300,"settings")
m.add_option("EXIT",500,50,m.width//2,350,"exit")
command = m.run()
if command == "play":
    print('play')
elif command == "settings":
    print('settings')    
elif command == "exit":
    print('exit')
else:
    print(command)
