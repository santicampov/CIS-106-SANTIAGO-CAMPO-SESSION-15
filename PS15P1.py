class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def employee(self):
        print("Manager name :", self.name, ", Salary : $ ", self.salary)
    def compbonus(self, rate):
        return self.salary * rate

class manager(employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def compltbonus(self):
        return self.salary * 0.4

def main():
    man = manager("Santiago Campo", 95000)
    man.employee()
    ltbonus = man.compltbonus()
    print("The long term bonus is: $ ", ltbonus)

if __name__ == "__main__":
    main()