class Animals:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f" Если {self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plants:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammals (Animals):
    pass

class Predators (Animals):
    pass

class Flowers (Plants):
    pass

class Fruits (Plants):
    edible = True
    def __init__(self, name):
        super(). __init__(name)

a1 = Predators ('Волк с Уолл-Стрит')
a2 = Mammals ('Хатико')
p1 = Flowers ('Цветик семицветик')
p2 = Fruits ('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)















