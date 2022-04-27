import pygame

class StartButton:
    def __init__(self, picture, x, y, radius, color1, color2, deltax, deltay, dinamic):
        # initialization with their picture, coordinates, color, and the dinamic coordinates for moving ,
        # animation
        self.picture = picture
        self.x = x
        self.y = y
        self.radius = radius
        self.pressed = False
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.deltax = deltax
        self.deltay = deltay
        self.dinamic = dinamic + deltay

    def draw(self, win):
        # drawing the button icon, and its "shadow"
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        if self.pressed:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.deltay))
        else:
            win.blit(self.picture, (self.x - self.deltax, self.y - self.dinamic))
        self.clicked()

    def clicked(self):
        # checking if mouse is clicked in the buttons area
        m = pygame.mouse.get_pos()[0]
        n = pygame.mouse.get_pos()[1]
        if m >= self.x - self.radius and m <= self.x + self.radius and n >= self.y - self.radius and \
                n <= self.y + self.radius:
            self.color = self.color2
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    # print("pressed")
                    self.pressed = False
        else:
            self.color = self.color1



'''
def chess():
    print("chess")
'''
