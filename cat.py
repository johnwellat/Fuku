class Cat:
    species = 'felis catus'

    def __init__(self,name,age,meaning,color,):
        self.name = name
        self.age = age
        self.meaning = meaning
        self.color = color

    def description(self):
        return(f'{self.name} is {self.age} years old cat,its name means {self.meaning}. It has a {self.color} fur.')

    def meow(self,sound):
        return f'{self.name} meows like {sound}.'


haru = Cat('Haru',3,'spring','chocolate color')
yuki = Cat('Yuki',2,'snow','calico & bi-color')
chibi = Cat('Chibi',1,'tiny','himalayan color')


print(haru.description())
print(haru.meow('mew mew'))
print(yuki.description())
print(yuki.meow('moo moo'))
print(chibi.description())
print(chibi.meow('miaow miaow'))
