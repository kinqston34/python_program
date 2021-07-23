class Outer:
    """外部类"""

    def __init__(self):
        ## 實體化內部類別
        self.inner = self.Inner()
        ## 實體化多級內部類別
        self.innerinner = self.inner.InnerInner()

    def show_classes(self):
        print("This is Outer class")
        print(inner)

    ## 内部類別
    class Inner:
        """First Inner Class"""

        def __init__(self):
            ## 實體化'InnerInner'類別
            self.innerinner = self.InnerInner()

        def show_classes(self):
            print("This is Inner class")
            print(self.innerinner)

        ## 多级内部類別
        class InnerInner:

            def inner_display(self, msg):
                print("This is multilevel InnerInner class")
                print(msg)

        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

    ## ...
outer = Outer()
inner = outer.Inner()
innerinner = inner.InnerInner()
innerinner.inner_display("hi")