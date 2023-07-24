import random
class Bunny(object):
    """Описание кролика"""
    def __init__(self, state, bunny, opportunity_bunny):
        """Инициализирует атрибуты state и tiger"""
        self.state = state
        self.bunny = bunny
        self.opportunity_bunny = opportunity_bunny
    def condition_bunny(self):
        """Среда"""
        self.opportunity_bunny = [0, 0.1, 0.2, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        self.opportunity_bunny = random.choice(self.opportunity_bunny)
        return  self.opportunity_bunny

class Tiger(Bunny):
    """Описание среды"""
    def __init__(self, state, tiger, opportunity_tiger_trace, opportunity_tiger_attack):
        """Инициализирует атрибуты state и tiger"""
        self.state = state
        self.tiger = tiger
        self.opportunity_tiger_trace = opportunity_tiger_trace
        self.opportunity_tiger_attack = opportunity_tiger_attack
        super(Tiger,self).condition_bunny() # передача из род. класса в дочерний
    def condition_tiger(self):
        """Среда"""

        self.tiger = "Поиск добычы"
        print(self.tiger)
        self.state = [1, 2, 3]
        self.state = random.choice(self.state)
        self.opportunity_tiger_trace = [0, 0.1, 0.2, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        self.opportunity_tiger_trace = random.choice(self.opportunity_tiger_trace)
        self.opportunity_tiger_attack = [0, 0.1, 0.2, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        self.opportunity_tiger_attack= random.choice(self.opportunity_tiger_attack)
        if self.opportunity_tiger_attack > self.opportunity_bunny:
            self.tiger = "Успешная атака"
        else:
            self.tiger = "Поиск добычы"
            print("Кролик убежал")
        return self.tiger
my_tiger = Tiger('savana', 'behavior', 'op1', 'op2')
print(my_tiger.condition_tiger())
