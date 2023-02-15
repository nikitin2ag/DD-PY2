class Building:
    """Базовый класс здания"""

    def __init__(self, address: str, org_list: list):
        """
        Инициализация экземпляра класса Building
        :param address: адрес здания
        :param org_list: список организаций, расположенных в здании
        """
        if not isinstance(address, str):
            raise TypeError("Адрес здания должен быть типа str")
        self._address = address
        if not isinstance(org_list, list):
            raise TypeError("Список организаций должен быть типа list")
        self.org_list = org_list

    def __str__(self) -> str:
        """
        Вывод экземпляра класса
        :return: строка формата - Здание по адресу: адрес здания
        """
        return f"Здание по адресу: {self.address}."

    def __repr__(self) -> str:
        """
        Вывод экземпляра класса, по которому можно инициализировать экземпляр класса
        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(address={self.address!r}, org_list={self.org_list!r})"

    def add_org(self, org: str):
        """
        Добавление организации в список
        :param org: добавляемая организация
        """
        self.org_list.append(org)

    def remove_org(self, org: str):
        """
        Удаление организации из списка
        :param org: удаляемая организация
        """
        self.org_list.remove(org)

    @property
    def address(self) -> str:
        """
        Свойство возвращает защищённый атрибут - адрес здания
        Причина инкапсуляции - адрес здания не должен меняться
        :return: значение _address
        """
        return self._address


class ResidentialBuilding(Building):
    """Дочерний от Building класс - жилой дом"""

    def __init__(self, address: str, org_list: list, number_of_offices: int, number_of_app: int):
        """
        Инициализация экземпляра класса ResidentialBuilding с конструктором родительского класса
        :param address: адрес здания
        :param org_list: список организаций в здании
        :param number_of_offices: число офисов под коммерческие организации
        :param number_of_app: число квартир в жилом доме
        """
        super().__init__(address, org_list)
        if not isinstance(number_of_offices, int):
            raise TypeError("Число офисов должно быть типа int")
        if number_of_offices < len(self.org_list):
            raise ValueError("Число офисов не может быть меньше количества организаций в списке")
        self._number_of_offices = number_of_offices
        if not isinstance(number_of_app, int):
            raise TypeError("Число квартир должно быть типа int")
        if number_of_app <= 0:
            raise ValueError("Число квартир должно быть больше 0")
        self._number_of_app = number_of_app

    def __repr__(self) -> str:
        """
        Вывод экземпляра класса, по которому можно инициализировать экземпляр класса
        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(address={self.address!r}, org_list={self.org_list!r}, number_of_offices={self.number_of_offices}, number_of_app={self.number_of_app})"

    def add_org(self, org: str):
        """
        Добавление организации в список
        Причина перегрузки метода - организаций в здании не может быть больше, чем количество офисов
        :param org: добавляемая организация
        """
        if len(self.org_list) < self.number_of_offices:
            super().add_org(org)

    def available_offices(self) -> int:
        """
        Возвращаение количества свободных офисов
        :return: количество свободных офисов
        """
        return self._number_of_offices - len(self.org_list)

    @property
    def number_of_offices(self) -> int:
        """
        Свойство возвращает защищённый атрибут - количество офисов под коммерческие организации
        Причина инкапсуляции - количество офисов фиксировано
        :return: значение _number_of_offices
        """
        return self._number_of_offices

    @property
    def number_of_app(self) -> int:
        """
        Свойство возвращает защищённый атрибут - количество квартир в жилом доме
        Причина инкапсуляции - количество квартир фиксировано
        :return: значение _number_of_app
        """
        return self._number_of_app


if __name__ == "__main__":
    building_1 = Building("ул. Обручевых, 1", ["Одиннадцатый учебный корпус"])
    print(building_1)
    print(repr(building_1))
    org_1 = "Высшая инженерная школа"
    building_1.add_org(org_1)
    print(building_1)
    print(repr(building_1))
    building_1.remove_org(org_1)

    building_2 = ResidentialBuilding("Ключевая ул., 30", ["Бизнес-центр THE OFFICE"], 10, 200)
    print(building_2)
    print(repr(building_2))
    org_2 = "Адвокат Никулин А. П."
    building_2.add_org(org_2)
    print(building_2)
    print(repr(building_2))
    print("Количество свободных офисов:", building_2.available_offices())
    building_2.remove_org(org_2)
pass
