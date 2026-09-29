class Dictionary:
    __load = 2 / 3

    def __init__(self) -> None:
        self.__capacity = 8
        self.hash_table = [None] * self.__capacity
        self.length = 0

    def __resize(self) -> None:
        self.__capacity *= 2
        old_data = self.hash_table
        self.hash_table = [None] * self.__capacity
        self.length = 0

        for i in range(len(old_data)):
            if old_data[i]:
                self.__setitem__(old_data[i][0], old_data[i][2])

    def __setitem__(self, key: any, value: any) -> None:
        i = hash(key) % self.__capacity
        while self.hash_table[i] and self.hash_table[i][0] != key:
            i = (i + 1) % self.__capacity

        was_empty = not self.hash_table[i]
        self.hash_table[i] = (key, i, value)
        if was_empty:
            self.length += 1
            if self.length / self.__capacity > self.__load:
                self.__resize()

    def __getitem__(self, key: any) -> any:
        i = hash(key) % self.__capacity
        while self.hash_table[i] and self.hash_table[i][0] != key:
            i = (i + 1) % self.__capacity
        if self.hash_table[i]:
            return self.hash_table[i][2]
        raise KeyError(f"key {key} not found")

    def __len__(self) -> int:
        return self.length
