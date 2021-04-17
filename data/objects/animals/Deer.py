# deer animal

from data.objects.animals import Animal.Animal
import os

class Deer(Animal):
    
    sprite_path_template = 'deer_gender.png'
    speed_mod = 2

    def __init__(self, width=16, height=16, gender='female'):
        self.gender = gender
        self.sprite_path = os.path.join(\
            Animal.sprites_path,\
            sprite_path_template.replace('gender', self.gender))
        
        super().__init__(width, height, self.sprite_path) # passes to the Animal.__init__()
