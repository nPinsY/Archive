class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("COOKIE OVERLOAD")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("😔")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(7)
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.withdraw(6)
    print(jar)

if __name__ == "__main__":
    main()