class Employee():

    def __init__(self, name, job_title, start_date, salary):
        self.name = name
        self.job = job_title
        self.start = start_date
        self.salary = salary


class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []
        

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name

    def hire_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees


    # Add the remaining methods to fill the requirements above

Cole = Employee("Cole", "Web Developer", "June 15", "1000000")
Patrick = Employee("Patrick", "Web Developer", "June 20", "1000000")
Jessica = Employee("Jessica", "Web Developer", "June 30", "1000000")

eventbrite = Company("Eventbrite", "2000")

eventbrite.hire_employee(Cole)
eventbrite.hire_employee(Patrick)
eventbrite.hire_employee(Jessica)

print(eventbrite.company_name)

for employees in eventbrite.employees:
    print(employees.name, employees.job, employees.start, employees.salary)