# 1. Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

# def credit_card(num):
#     return len(num[:-4]) * '*' + num[-4:]
# print(credit_card(input('Введите номер кредитной карты: ')))

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# def is_polindrom(slovo):
#     slovo = slovo.lower()
#     slovo_obr = slovo[::-1]
#     if slovo == slovo_obr:
#         print('PALINDROM')
#     else:
#         print('NOT PALINDROM')
#
# is_polindrom(input('Введите слово: '))



class Tomato:
    states = {1: 'вылез из земли', 2: "вырос до своего максимума", 3: "достиг последней стадии созревания"}

    # все стадии созревания томата

    def __init__(self, index):
        self._index = index
        self._state = self.states[1]

    def grow(self):
        self._state = self.states[+1]

    def is_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False


obj_Tomato = Tomato(1)


class TomatoBush:

    def __init__(self, kol_vo):
        self.kol_vo = kol_vo
        tomatoes = []

    def grow_all(self):
        pass

    def all_are_ripe(self):
        pass

    def give_away_all(self):
        pass

# for i in TomatoBush.kol_vo:
#     obj_Tomato1 = Tomato(TomatoBush.kol_vo - 1)




class Gardener(Tomato):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self._plant = obj_Tomato

    def work(self):
        pass

    def harvest(self):
        if Tomato.is_ripe(self):
            pass
        else:
            print('Еще не все плоды созрели')

    @staticmethod
    def knowledge_base():  # справка по садоводству
        print('Справка по садоводству')

# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

Gardener.knowledge_base()
obj_TomatoBush = TomatoBush(5)
obj_Gardeber = Gardener('John Doe')
