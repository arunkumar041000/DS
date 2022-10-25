from printTable import printTable


class Hash:
    def __init__(self) -> None:
        self.table = {}

    def __str__(self) -> str:
        return printTable(["Keys","Value"],[[key, value] for key, value in self.table.items()])

    def set(self, key, value) -> None:
        self.table[key] = value

    def get(self, key) -> any:
        return self.table[key]


if __name__ == "__main__":
    table = Hash()

    table.set(1, 2)
    table.set(2, 3)
    table.set(3, 4)

    table.set(2, 5)
    print(table)
