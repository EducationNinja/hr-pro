from datetime import datetime

class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def __str__(self):
        return f"{self.name} | {self.age} | ${self.salary} | {self.get_working_years()}"

    def get_working_years(self):
        return datetime.now().year - int(self.employment_year)

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def __str__(self):
        return super().__str__() + f" | ${self.get_bonus()}"

    def get_working_years(self):
        return super().get_working_years() - 10

    def get_bonus(self):
        return int(self.salary) * float(self.bonus_percentage)/100


def main():
    employees = []
    managers = []

    while True:
        option = input("""Options:
            1. Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
        """)
        option = int(option)
        if option == 1:
            for employee in employees:
                print(employee)
        elif option == 2:
            for manager in managers:
                print(manager)
        elif option == 3:
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")
            new_employee = Employee(name, age, salary, employment_year)
            employees.append(new_employee)

        elif option == 4:
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")
            bonus_percentage = input("Bonus %: ")
            new_manager = Manager(name, age, salary, employment_year, bonus_percentage)
            managers.append(new_manager)

        elif option == 5:
            break;
        else:
            print("Incorrect input, select a number from 1 to 5")



if __name__ == '__main__':
    main()
