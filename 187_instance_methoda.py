# Instance method

class Person:  # class name Capital letter se shuru hona chahiye (PascalCase)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"  # comma ki jagah space zyada readable hai

    def is_above_18(self):
        return self.age >= 18   # >= use karo, warna exactly 18 wala False aayega


p1 = Person('Anas', 'Malik', 19)
p2 = Person('Ana', 'Malik', 10)

print(p1.is_above_18())
print(p1.full_name())   # brackets () lagana zaroori hai, warna method call nahi hoga

l = [1, 2, 3, 4]

# clear, pop
# l.clear()
# print(l)

l.append(10)   # normal tareeqa: object.method() — list.append(l,10) bhi chalta hai lekin ye unconventional hai
print(l)