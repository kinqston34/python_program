# class Outer:
#     class Inner:
#         pass
#         class InnerInner:
#             pass
#     class Inner:
#         pass
#     pass

class Outer:
    def __init__(self):
        self.inner = self.Inner()

    def reveal(self):
        self.inner.inner_display('call')

    class Inner:
        def inner_display(self,msg):
            print(msg)
outer = Outer()
outer.reveal()

Outer().Inner().inner_display("call")
inner = Outer.Inner()
inner.inner_display("just print it")

