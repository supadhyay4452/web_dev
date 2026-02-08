class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_details(self):
        print("name:",self.name)
        print("Marks:",self.marks)
    
    def result(self):
            if self.marks >= 40:
                print("pass")
            else:
                print("fail")

s1=Student("sumit",34)
s2=Student("amit",64)

s1.show_details()
s1.result()
s2.show_details()
s2.result()
        
