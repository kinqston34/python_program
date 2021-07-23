class Outer:
    def __init__(self):
        self.inner = self.Inner()
        self._inner = self._Inner()

    def showclass(self):
        print("this is outer class")
        print(self.inner)
        print(self._inner)
    class Inner:
        def inner_display(self,msg):
            print("this is Inner class")
            print(msg)

    class _Inner:
        def inner_display(self,msg):
            print("this is _Inner class")
            print(msg)

#way1
Outer()._Inner().inner_display("hi")
#way2
outer = Outer()
inner = outer.Inner()
_inner = outer._Inner()
inner.inner_display("hi")
_inner.inner_display("hi")
