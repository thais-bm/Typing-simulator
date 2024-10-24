from resource.color import *
from entities.entity_base import Entity

import pygame
import resource.fonts as fonts
import resource.color as colors

class KeyListener(Entity):
    '''
    Do action(s) when a key(s) is(are) pressed

    Attributes
    ----------
    keys:
        A list of keys that when pressed will make the action(s) play out
    actions:
        A list of actions that will happen if one of the registered keys is pressed
    '''
    def __init__(self, keys = [], actions = [], layer = 0):
        super().__init__(layer)
        self.keys = keys
        self.actions = actions
        self.pressed_keys = {}
        # Add colors to each key latter
        self.key_colors = {}
        
        self.key_size = (40, 40)
        self.container_rect = pygame.Rect(100, 100, 500, 200)
        self.keyboard = self.keyboard_layout() 
            
                    
    def input_key(self, key_char, pressed):
        # Update the pressed state of a key
        self.pressed_keys[key_char] = pressed
        
        # debug: key_char
        print(key_char)
        
    def event(self, event):
        if event.type == pygame.KEYDOWN:
            # Mods check to see if caps lock is on
            mods = pygame.key.get_mods() 
            key_char = pygame.key.name(event.key)
            
            if (mods and pygame.KMOD_CAPS) and key_char.isalpha():
                key_char = key_char.upper()
            
            else:
                key_char = key_char.lower()

            # Update pressed key
            self.input_key(key_char, True)

            if key_char in self.keys:
                for action in self.actions:
                    action()

        # The key is not being pressed
        elif event.type == pygame.KEYUP:
            key_char = pygame.key.name(event.key).lower()
            self.input_key(key_char, False)
            
    def keyboard_layout(self):
        layout = []
        inicial_x = 450
        inicial_y = 580
        
        letters = [
                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
                ]
        
        for i, row in enumerate(letters):
            for j, key in enumerate(row):
                # Each i is a row of lists, gives it a stairs look
                # i == 1 is the second list
                if i == 1:  
                    x = inicial_x + (j * (self.key_size[0] + 10)) + (self.key_size[0] // 2)
                elif i == 2:  
                    x = inicial_x+ 30 + (j * (self.key_size[0] + 10)) + (self.key_size[0] // 4)
                else:
                    x = inicial_x + j * (self.key_size[0] + 10)
                
                y = inicial_y + i * (self.key_size[1] + 10)
                layout.append((key, x, y))
                
        return layout
    
    def draw(self, screen):
        font = pygame.font.SysFont(fonts.SEGA, 30)
        
        for key, x, y in self.keyboard:
            key_x = self.container_rect.x + x
            key_y = self.container_rect.y + y
        
            color = colors.WHITE
            if self.pressed_keys.get(key.lower(), False): 
                color = colors.GREEN
            if self.pressed_keys.get(key.upper(), False):
                color = colors.GREEN
            
            # The * symbol unpacks the values
            
            pygame.draw.rect(screen, color, (key_x, key_y, *self.key_size))
            pygame.draw.rect(screen, colors.BLACK, (key_x, key_y, *self.key_size), 2) 
            
            
            label = font.render(key, True, colors.BLACK)
            
            label_rect = label.get_rect(center =(key_x + self.key_size[0] // 2, key_y + self.key_size[1] // 2))
            screen.blit(label, label_rect)
            
          
             