class A:
    def a1(self):
        print("a1")


class B:
    def b(self):
        print('b')
        A().a1()


object_b = B()
object_b.b()
