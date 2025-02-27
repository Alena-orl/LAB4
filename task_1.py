class SocialNetwork:
    """
    Базовый класс для социальных сетей.
    """

    def __init__(self, name: str, users_count: int) -> None:
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей в социальной сети.
        """
        self.__name = name  # Инкапсуляция для защиты атрибута
        self.__users_count = users_count  # Инкапсуляция для защиты атрибута

    def add_user(self) -> None:
        """
        Добавляет пользователя в социальную сеть, увеличивая общее количество пользователей.
        """
        self.__users_count += 1

    def get_users_count(self) -> int:
        """
        Возвращает текущее количество пользователей.

        :return: Количество пользователей.
        """
        return self.__users_count

    def __str__(self) -> str:
        """Возвращает строковое представление социальной сети."""
        return f"{self.__class__.__name__}(name={self.__name}, users_count={self.__users_count})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление социальной сети."""
        return f"SocialNetwork(name={self.__name!r}, users_count={self.__users_count!r})"


class VK(SocialNetwork):
    """
    Класс для социальной сети ВКонтакте, наследуется от класса SocialNetwork.
    """

    def __init__(self, users_count: int, vk_features: list[str]) -> None:
        """
        Инициализация социальной сети ВКонтакте.

        :param users_count: Количество пользователей в ВКонтакте.
        :param vk_features: Особенности, доступные в ВКонтакте.
        """
        super().__init__("VK", users_count)
        self.vk_features = vk_features  # Публичный атрибут

    def add_user(self) -> None:
        """
        Переопределяет метод добавления пользователя для ВКонтакте,
        добавляя дополнительную логику (например, уведомление о новом пользователе).

        :return: None
        """
        super().add_user()  # Вызов метода родительского класса
        print(f"New user added to VK! Total users: {self.get_users_count()}")

    def __str__(self) -> str:
        """Возвращает строковое представление ВКонтакте с учетом его особенностей."""
        return f"{super().__str__()}, vk_features={self.vk_features}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление ВКонтакте."""
        return f"VK(users_count={self.get_users_count()!r}, vk_features={self.vk_features!r})"


class Facebook(SocialNetwork):
    """
    Класс для социальной сети Facebook, наследуется от класса SocialNetwork.
    """

    def __init__(self, users_count: int, fb_groups: int) -> None:
        """
        Инициализация социальной сети Facebook.

        :param users_count: Количество пользователей в Facebook.
        :param fb_groups: Количество групп в Facebook.
        """
        super().__init__("Facebook", users_count)
        self.__fb_groups = fb_groups  # Инкапсуляция для защиты атрибута

    def add_group(self) -> None:
        """
        Добавляет новую группу в Facebook, увеличивая общее количество групп.
        """
        self.__fb_groups += 1

    def get_groups_count(self) -> int:
        """
        Возвращает текущее количество групп.

        :return: Количество групп.
        """
        return self.__fb_groups

    def __str__(self) -> str:
        """Возвращает строковое представление Facebook с учетом количества групп."""
        return f"{super().__str__()}, fb_groups={self.get_groups_count()}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление Facebook."""
        return f"Facebook(users_count={self.get_users_count()!r}, fb_groups={self.get_groups_count()!r})"


if __name__ == "__main__":
    # Пример использования классов
    vk = VK(users_count=1000000, vk_features=["Messaging", "Groups", "Videos"])
    print(vk)
    vk.add_user()  # Добавляем пользователя

    facebook = Facebook(users_count=2000000, fb_groups=50000)
    print(facebook)
    facebook.add_group()  # Добавляем группу


# Базовый класс SocialNetwork:
# Имеет конструктор для инициализации имени социальной сети и количества пользователей.
# Методы add_user и get_users_count управляют количеством пользователей.
# Магические методы __str__ и __repr__ возвращают строковые представления объекта.
# Дочерний класс VK:
# Унаследует от SocialNetwork и добавляет атрибут vk_features, который хранит особенности ВКонтакте.
# Переопределяет метод add_user, добавляя дополнительную логику (например, вывод сообщения при добавлении пользователя).
# Переопределяет методы __str__ и __repr__ для отображения информации о ВКонтакте.
# Дочерний класс Facebook:
# Унаследует от SocialNetwork и добавляет атрибут __fb_groups, который инкапсулирует количество групп в Facebook.
# Реализует метод add_group, который увеличивает количество групп.
# Переопределяет методы __str__ и __repr__ для отображения информации о Facebook.
