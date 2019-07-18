class Test:
    """Sample Class To Test The documentation String"""
    a=1000
    b=2000
    def display(self):
        print(Test.a)
        print(Test.b)
    def modify(self):
        Test.a=Test.a+100
        Test.b=Test.b-100

print(Test.__doc__)
t1=Test()
t1.display()
t1.modify()
t1.display()
