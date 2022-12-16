# File: employee.py
#  Description: Based off specific attributes provided for each employee, returns the employee's information
#  Student Name: Karim Ladak
#  Student UT EID: kal3635
#  Partner Name: Suren Bhakta
#  Partner UT EID: ssb2943
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 9/13/22
#  Date Last Modified: 9/19/22

import sys


# Class type standard employee with no added input
class Employee:
    # this method assigns values for the names of the variables using kwargs
    # (if value is not available, it assigns none)
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    # this method returns the information of the Employee as a string
    def __str__(self):
        return self.name + ', ' + self.id + ', ' + str(self.salary)


############################################################
############################################################
############################################################
# Class type Permanent Employee which as inheritance from class employee with benefits
class Permanent_Employee(Employee):
    # Uses super to call method from employee class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = str(kwargs.get('benefits'))

    # Depending on benefits, multiplies onto salary
    def cal_salary(self):
        self.benefits = str(self.benefits)
        if self.benefits == str(['health_insurance']):
            return self.salary * 0.9
        elif self.benefits == str(['retirement']):
            return self.salary * 0.8
        else:
            self.benefits == str(['retirement', 'health_insurance'])
            return self.salary * 0.7
    # returns permanent employee information from employee class with benefits
    def __str__(self):
        return super().__str__() + ', ' + self.benefits


############################################################
############################################################
############################################################
# Class type Manager which has inheritence from employee with bonus
class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus', 0)

    # Manager has added benefit bonus added to salary
    def cal_salary(self):
        self.salary = self.salary + self.bonus
        return self.salary

    # Returns salary and other information for manager with bonus as string
    def __str__(self):
        return super().__str__() + ', ' + str(self.bonus)


############################################################
############################################################
############################################################
# Class type Temporary Employee which has inheritance from employee and is payed hourly
class Temporary_Employee(Employee):

    # Method takes input salary and hours
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours', 0)

    # Calculates hourly salary
    def cal_salary(self):
        self.salary = self.salary * self.hours
        return self.salary

    # Returns hourly based salary as string and temporary eployee information
    def __str__(self):
        return super().__str__() + ', ' + str(self.hours)


############################################################
############################################################
############################################################
# Class type Consultant with inheritence of Temporary employee
class Consultant(Temporary_Employee):

    # Method takes input salary, hours, bonus
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel', 0)

    # Calculates hourly salary and add travel benefit as well
    def cal_salary(self):
        self.salary = int(self.salary * self.hours + (self.travel * 1000))
        return self.salary

    def __str__(self):  #returns string with information for consultant
        return super().__str__() + ', ' + str(self.travel)


############################################################
############################################################
############################################################

# class type manager which has inheritance from class consultant and employee
class Consultant_Manager(Consultant, Manager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Adds bonus, travel benefit, hourly salary, all multiplied to standard salary
    def cal_salary(self):
        self.salary = self.salary * self.hours + self.travel * 1000 + self.bonus
        return self.salary
    # returns consultant manager info as a string
    def __str__(self):
        return f'{Consultant.__str__(self)} \n{Manager.__str__(self)}'



############################################################
############################################################
############################################################


###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    # assign each employee with specific attributes
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100, hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
   #With their specific attributes, prints their salary with benefits
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:", matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()