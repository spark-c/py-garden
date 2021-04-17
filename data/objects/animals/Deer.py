# deer animal

from data.objects.animals.Animal import Animal
import os

class Deer(Animal):
    
    sprite_path_template = 'deer_gender.png'
    speed_mod = 2

    def __init__(self, gender='female'):
        self.gender = gender
        self.sprite_path = os.path.join(\
            Animal.sprites_path,\
            Deer.sprite_path_template.replace('gender', self.gender))
        
        super().__init__(self.sprite_path) # passes to the Animal.__init__()
