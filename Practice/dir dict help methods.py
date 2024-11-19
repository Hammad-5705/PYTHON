class student:
    A=4
    def __init__(self) -> None:
        self.a=1

s=student
print(s.__dir__)
print(s.__dict__)
print(help(student))
