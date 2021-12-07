# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(str(len(self.letters)))


# alph = Alphabet('eng', 'AEIOUYBCDFGHJKLMNPQRSTVWXZ')
# alph.print()
# alph.letters_num()

# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение
# свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__(lang='Eng', letters=string.ascii_uppercase)
        self.__letters_num = len(self.letters)

    def is_en_letter(self, l):

        if l in self.letters:
            print('Буква отноcится к английскому алфавиту')
        else:
            print('Эта буква не из английского алфавита')

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The Tesla CEO took aim at a signature Biden administration legislative proposal " \
               "and said China is adjusting to its growing position as a dominant world power in" \
               " an interview with The Wall Street Journal."


#                                                   Тесты

# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке


obj_engAlphabet = EngAlphabet()
print(obj_engAlphabet.letters)
print(obj_engAlphabet.letters_num())
obj_engAlphabet.is_en_letter("F")
obj_engAlphabet.is_en_letter("Щ")
print(obj_engAlphabet.example())
