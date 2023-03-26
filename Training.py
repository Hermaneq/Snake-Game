class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swimming")

    def breath(self):
        super().breath()
        print("Underwater")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)