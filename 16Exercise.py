# Multiple Inheritance

class A:
    def class_a_method(self):
        return "I'm just class A method"
class D:
    pass
instance_a = A
print(instance_a.class_a_method())
# Multiple Inheritance
class B(D):
    def class_b_method(self):
        return "I'm just class B method"
    def hello(self):
        return "hello from class B"
class C(B, A):
    pass
instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
print(help(C))
print(C.mro())
print(C.__mro__)