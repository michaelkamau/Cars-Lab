class Car:
    def __init__(self, name='General', model = 'GM', type='saloon'):
        self.name = name
        self.model = model
        self.num_of_doors = 2 if self.name == 'Porshe' or self.name == 'Koenigsegg' else 4
        self.num_of_wheels = 8 if type == 'trailer' else 4
        self.speed = 0

    def is_saloon(self):
        return True if self.num_of_wheels == 4 else False

    def drive(self, new_speed):
        self.speed = new_speed * 1000/3 if self.is_saloon() else new_speed * 77/7
        return self
