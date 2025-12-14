#1 parent
class Camera:
    def __init__(self, megapixel):
        self.megapixel = megapixel

    def take_photo(self):
        print(f'Say CHEESE on camera:{self.megapixel}')

#2 parent
class GPS:
    def __init__(self, map_vers):
        self.map_vers= map_vers

    def build_route(self, place):
        print(f'Route has been rebuilt to: {place}, maps:{self.map_vers}')

#3 parent
class Player:
    def __init__(self, volume):
        self.volume = volume

    def play (self, song):
        print(f'Playing: {song}, Volume: {self.volume}')

#1 child
class Smartphone (Camera, GPS, Player):
    def __init__(self, model, megapixel, map_vers, volume):
        self.model = model

        Camera.__init__(self, megapixel)
        GPS.__init__(self, map_vers)
        Player.__init__(self, volume)

    def info(self):
        print(f'Smartphone: {self.model}')
        print(f'Camera: {self.megapixel} MP')
        print(f'GPS: {self.map_vers} version')
        print(f'Volume: {self.volume}')

Phone= Smartphone('Galaxy S24', 50, '01.2024', 15)
Phone.info()
Phone.take_photo()
Phone.build_route('Uralsk/')
Phone.play('Imagine Dragons - Believer')




