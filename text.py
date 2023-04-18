'''
Title: text sprites
'''
from sprites import Sprite
from pygame import font

class Text(Sprite): # inherits from the sprite class
    def __init__(self, window, content, size = 20, family = 'segoeprint'):
        Sprite.__init__(self, window)
        self.content = content # text in the sprite
        self.family = family # font family of the text
        self.size = size # size of the text
        self.colour = (150, 150, 150) # sets the colour of the text
        self.italic = False # italics
        self.bold = False # bold
        self.brightness = 0
        self.renderText()

    ##-- Modifiers
    def renderText(self): # renders the text sprite
        self.font = font.SysFont(self.family, self.size, italic = self.italic)
        self.sprite = self.font.render(self.content, 1, self.colour)
        self.sprite.set_alpha(self.brightness)

    def setText(self, content): # changes the text 
        self.content = content
        self.renderText()

    def setSize(self, size): # changes the size of the text
        self.size = size
        self.renderText()

    def modAlpha(self, num):
        self.brightness += num
        if self.brightness < 0:
            self.brightness = 0
        if self.brightness > 255:
            self.brightness = 255
        self.renderText()

    ##-- Accessors
    def getText(self): # gets the text of the sprite
        return self.content

    def getDimentions(self):
        return [self.sprite.get_rect().width, self.sprite.get_rect().height]
    
if __name__ == "__main__":
    from pygame import init, font, K_UP, K_DOWN
    from window import Window

    init()
    window = Window()
    typelist = font.get_fonts()
    text = []
    for i, cont in enumerate(typelist):
        # content = Text(window, cont, family = cont)
        content = Text(window, cont)
        content.setPOS(0, i * 24)
        text.append(content)

    print(typelist[38])
    while True:
        window.getEvents()
        if window.getKeysPressed()[K_UP] == 1:
            for txt in text:
                txt.setPOS(txt.getPOS()[0], txt.getPOS()[1] + 10)
        if window.getKeysPressed()[K_DOWN] == 1:
            for txt in text:
                txt.setPOS(txt.getPOS()[0], txt.getPOS()[1] - 10)

        window.clearScreen()
        for txt in text:
            window.blitSprite(txt)
        window.updateScreen()