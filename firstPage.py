class FirstPage:
    def __init__(self, description, name, surname):
        self.description  = description
        self.name = name
        self.surname = surname
        self.email = name + '.' + surname + '@iaau.edu.kg'

    def about (self):
        return self.description

    def author (self):
        return '{} {}'.format(self.name, self.surname)