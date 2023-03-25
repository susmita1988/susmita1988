class Employee:
    def __init__(self, name, id):
        self. name=name
        self.id=id


    def showdetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):

    #def __init__(self, technologyused):
        #self.technologyused=technologyused


    #def showtechnology(self):
       # print(f"The language used: {self.technologyused} ")


    def languageused(self):
        print(f"The language used is Python")








e1=Employee("susmita", 40)
e1.showdetails()

#e2=Programmer("Python")
#e2.showtechnology()

e2=Programmer("Rajiv", 35)
e2.showdetails()
e2.languageused()


