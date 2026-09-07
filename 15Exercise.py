


class person:
    def info(self):
        print("INFO")
class laptop(person):
    def prosesser(self):
        print("prosesser")

class book(laptop):
    def math(self):
     print("math")

book = book()
book.info()

book.math()

