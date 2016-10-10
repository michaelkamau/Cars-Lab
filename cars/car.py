class Car:
    def __init__(self, name='General', model = 'GM', type='saloon'):
        self.name = name
        self.model = model
        self.num_of_doors = 2 if self.name == 'Porshe' or self.name == 'Koenigsegg' else 4
        self.num_of_wheels = 8 if type == 'trailer' else 4
