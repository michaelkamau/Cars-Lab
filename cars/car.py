class Car:
    def __init__(self, name='General', model = 'GM'):
        self.name = name
        self.model = model
        self.num_of_doors = 2 if self.name == 'Porshe' or self.name == 'Koenigsegg' else 4
