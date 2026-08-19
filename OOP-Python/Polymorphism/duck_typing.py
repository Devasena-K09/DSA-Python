class Duck:

    def speak(self):
        print("Quack Quack")


class Human:

    def speak(self):
        print("Hello")


def make_sound(obj):
    obj.speak()


duck = Duck()
human = Human()

make_sound(duck)
make_sound(human)
