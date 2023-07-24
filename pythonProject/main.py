import random
class Tiger(object):
    """Описание среды"""
    def __init__(self, state, tiger, opportunity_tiger):
        """Инициализирует атрибуты state и tiger"""
        self.state = state
        self.tiger = tiger
        self.opportunity_tiger = opportunity_tiger
    def condition(self):
        """Среда"""
        self.tiger = "Поиск добычи"
        print(self.tiger)
        self.state = [1, 2, 3]
        self.state = random.choice(self.state)
        self.opportunity_tiger = [0, 0.1, 0.2, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        self.opportunity_tiger = random.choice(self.opportunity_tiger)
        if self.state == 1:
            print('Добыча есть,',self.state)
            self.tiger = "Выследить добычу"
            print(self.tiger)
            if self.opportunity_tiger > 0.5:
                print("Вероятность = ",self.opportunity_tiger)
                self.tiger = "Атака добычи"
            else:
                print("Вероятность = ", self.opportunity_tiger)
                self.tiger = "Поиск добычи"
        elif self.state == 2:
            print('Есть враг,', self.state)
            self.tiger = "Убежать от врага"
        else:
            print('Добычи нет,', self.state)
            self.tiger = "Поиск добычи"
        return self.tiger
my_tiger = Tiger('savana', 'behavior', 'op')
print(my_tiger.condition())