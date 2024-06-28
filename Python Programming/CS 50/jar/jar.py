class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if capacity < 1:
            raise ValueError("Negative Integer")
        self._n = 0

    def __str__(self):
        return self._n * "🍪"

    def deposit(self, n):
        self._n = n + self._n
        if self._n > self._capacity:
            raise ValueError("Max Limit Exceded")

    def withdraw(self, n):
        self._n = self._n - n
        if self._n < 0:
            raise ValueError("No more cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n
