from entities.entity_base import Entity
from entities.image import Image

class Player(Entity):
    def __init__(self, center, sprite_path, hitbox = None, width = None, height = None, layer = 1):
        super().__init__(layer = layer)
        self.life = 3
        self.sprite = Image(path = sprite_path, center = center, width = width, height = height)

        self.angle = -90

        if hitbox == None:
            hitbox = self.sprite.image.get_rect()