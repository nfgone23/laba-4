class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)

# Пример использования
collection = Collection()
collection.add("Элемент 1")
collection.add("Элемент 2")
collection.add("Элемент 3")

for item in collection:
    print(item)
