class Dictionary:
    __capacity = 8
    __load = 2 / 3
    __count = 0
    __data = []

    def __init__(self) -> None:
        self.__data = [None] * self.__capacity

    def __resize(self) -> None:
        self.__capacity *= 2
        old_data = self.__data
        self.__data = [None] * self.__capacity
        self.__count = 0

        for i in range(len(old_data)):
            if old_data[i]:
                self.__setitem__(old_data[i][0], old_data[i][1])

    def __setitem__(self, key: any, value: any) -> None:
        i = hash(key) % self.__capacity
        while self.__data[i] and self.__data[i][0] != key:
            i = (i + 1) % self.__capacity

        was_empty = not self.__data[i]
        self.__data[i] = (key, value)
        if was_empty:
            self.__count += 1
            if self.__count / self.__capacity > self.__load:
                self.__resize()

    def __getitem__(self, key: any) -> any:
        i = hash(key) % self.__capacity
        while self.__data[i] and self.__data[i][0] != key:
            i = (i + 1) % self.__capacity
        if self.__data[i]:
            return self.__data[i][1]
        raise KeyError(f"key {key} not found")

    def __len__(self) -> int:
        return self.__count
