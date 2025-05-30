class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary          # Protected attribute
        self.__ssn = ssn               # Private attribute

    # Getter method for SSN
    def get_ssn(self):
        return self.__ssn

    # Optional: Setter method for SSN
    def set_ssn(self, new_ssn):
        self.__ssn = new_ssn

# Object creation
emp = Employee("John", 50000, "123-45-6789")

# Accessing attributes
print("Name:", emp.name)             # Public
print("Salary:", emp._salary)        # Protected (still accessible)
print("SSN:", emp.get_ssn())         # Private (access via method)
