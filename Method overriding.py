class animal:
    def speak(self):
        self.sound="bababa"
        return self.sound

class dog(animal):
    def speak(self):
        self.sound="woof"
        return self.sound

a=animal()
d=dog()

print(a.speak())
print(d.speak())