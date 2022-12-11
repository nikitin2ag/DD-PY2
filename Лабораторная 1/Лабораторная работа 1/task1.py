import doctest


class Bucket:
    def __init__(self, all_volume: float, filled_volume: float):
        """
        Создание и подготовка к работе объектов класса Bucket
        :param all_volume: Объём ведра (в литрах)
        :param filled_volume: Объём жидкости в ведре (в литрах)
        Пример:
        >>> bucket = Bucket(2.5, 1.5)  # инициализация экземпляра класса Bucket
        """
        if not isinstance(all_volume, (int, float)):
            raise TypeError("Объём ведра должен быть типа float или int")
        if all_volume <= 0:
            raise ValueError("Объём ведра должен быть положительным числом")
        self.all_volume = all_volume

        if not isinstance(filled_volume, (int, float)):
            raise TypeError("Объём жидкости должен быть float или int")
        if filled_volume < 0:
            raise ValueError("Объём жидкости не может быть отрицательным числом")
        if filled_volume > all_volume:
            raise ValueError("Объём жидкости в ведре не может быть больше объёма всего ведра")
        self.filled_volume = filled_volume

    def add_liquid_to_bucket(self, liquid_volume: float) -> None:
        """
        Добавление жидкости в ведро
        :param liquid_volume: Объём добавляемой жидкости (в литрах)
        :raise ValueError: Если объём жидкости в ведре после добавления больше объёма всего ведра, то вызываем ошибку
        Пример:
        >>> bucket = Bucket(2.5, 0)
        >>> bucket.add_liquid_to_bucket(2.49)
        """
        if not isinstance(liquid_volume, (int, float)):
            raise TypeError("Объём добавляемой жидкости должен быть типа float или int")
        if liquid_volume < 0:
            raise ValueError("Объём добавляемой жидкости должен быть положительным числом")
        ...

    def remove_liquid_from_bucket(self, liquid_volume: float) -> float:
        """
        Извлечение воды из ведра
        :param liquid_volume: Объём извлекаемой жидкости
        :raise ValueError: Если объём извлекаемой жидкости больше объёма всей имеющейся жидкости в ведре, то вызываем ошибку
        :return: Объём извлечённой жидкости
        Пример:
        >>> bucket = Bucket(4.5, 3.5)
        >>> bucket.remove_liquid_from_bucket(3.5)
        """
        ...

    def is_empty_bucket(self) -> bool:
        """
        Проверка, является ли ведро пустым.
        :return: Является ли ведро пустым (True или False)
        Пример:
        >>> bucket = Bucket(4.5, 0)
        >>> bucket.is_empty_bucket() #True
        """
        ...


class Person:

    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объектов класса Person
        :param age: Возраст человека
        :param name: Имя человека
        Пример:
        >>> person = Person("Артём", 19) # инициализация экземпляра класса Person
        """
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст человека должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст человека должен быть неотрицательным числом")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str (строкой)")
        if name == "":
            raise ValueError("Имя человека не должно быть пустым")
        self.name = name

    def is_juvenile(self) -> bool:
        """
        Проверка человека на совершеннолетие
        :return: Является ли человек совершеннолетним (True или False)
        Примеры:
        >>> person1 = Person("Анна", 19)
        >>> person1.is_juvenile() #True
        >>> person2 = Person("Геннадий", 18)
        >>> person2.is_juvenile() #True
        >>> person3 = Person("Борис", 17)
        >>> person3.is_juvenile() #False
       """
        ...

    def assign_nickname(self, nickname: str):
        """
        Присвоение человеку ник на основе его имени.
        :param nickname: Ник (псевдоним)
        Пример:
        >>> person1 = Person("Михаил", 19)
        >>> person1.assign_nickname("Nagibator228")
        """
        if nickname == "":
            raise ValueError("Ник человека не должен быть пустым")
        ...


class Car:
    def __init__(self, velocity: float, endurance: float):
        """
        Создание и подготовка к работе объектов класса Car
        :param velocity: Скорость машины (в км/ч)
        :param endurance: Прочность машины (в МПа)
        Примеры:
        >>> car1 = Car(100.5, 60.3) # инициализация экземпляра класса Car
        """
        if not isinstance(velocity or endurance, (float, int)):
            raise TypeError("Параметры машины должны быть типа float или int")
        if velocity < 0 or endurance < 0:
            raise ValueError("Параметры машины должны быть больше нуля")
        self.velocity = velocity
        self.endurance = endurance

    def remove_wheels(self):
        """
        Снятие колёс с машины
        Пример:
        >>> car1 = Car(128.35, 67.4)
        >>> car1.remove_wheels() # получаем объект car1 = Car(0, 67.4)
        """
        ...

    def harden_corpus(self, hardening_tool_value: float):
        """
        Укрепление корпуса машины (закалкой металла или диффузионным насыщением)
        Пример:
        >>> car1 = Car(94.35, 108.2)
        >>> car1.harden_corpus(12.3) # hardening_tool_value = 30 => получаем объект car1 = Car(94.35, 120.5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
