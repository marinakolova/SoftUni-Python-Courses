class Human:

    MIN_FIRST_NAME_LENGTH = 4
    MIN_LAST_NAME_LENGTH = 3

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value[0].isupper():
            raise ValueError(f'Expected upper case letter! Argument: firstName')
        if len(value) < self.MIN_FIRST_NAME_LENGTH:
            raise ValueError(f'Expected length at least {self.MIN_FIRST_NAME_LENGTH} symbols! Argument: firstName')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value[0].isupper():
            raise ValueError(f'Expected upper case letter! Argument: lastName')
        if len(value) < self.MIN_FIRST_NAME_LENGTH:
            raise ValueError(f'Expected length at least {self.MIN_LAST_NAME_LENGTH} symbols! Argument: lastName')
        self._last_name = value

    def __str__(self):
        return f'First Name: {self.first_name}\n' \
            f'Last Name: {self.last_name}\n'


class Student(Human):

    MIN_FACULTY_NAME_LENGTH = 5
    MAX_FACULTY_NAME_LENGTH = 10

    def __init__(self, first_name, last_name, faculty_number):
        super().__init__(first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self._faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        if not self.MIN_FACULTY_NAME_LENGTH <= len(value) <= self.MAX_FACULTY_NAME_LENGTH:
            raise ValueError(f'Invalid faculty number!')
        self._faculty_number = value

    def __str__(self):
        base = super().__str__()
        return base + f'Faculty number: {self.faculty_number}\n'


class Worker(Human):

    MIN_WEEK_SALARY = 10
    MIN_WORKING_HOURS = 1
    MAX_WORKING_HOURS = 12

    def __init__(self, first_name, last_name, week_salary, work_hours_per_day):
        super().__init__(first_name, last_name)
        self.week_salary = week_salary
        self.working_hours = work_hours_per_day
        self.salary_per_hour = self.week_salary / 5 / self.working_hours

    @property
    def week_salary(self):
        return self._week_salary

    @week_salary.setter
    def week_salary(self, value):
        if value < 10:
            raise ValueError(f'Expected value mismatch! Argument: weekSalary')
        self._week_salary = value

    @property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, value):
        if not self.MIN_WORKING_HOURS <= value <= self.MAX_WORKING_HOURS:
            raise ValueError(f'Expected value mismatch! Argument: workHoursPerDay')
        self._working_hours = value

    def __str__(self):
        base = super().__str__()
        return base + f'Week Salary: {self.week_salary:.2f}\n' \
            f'Hours per day: {self.working_hours:.2f}\n' \
            f'Salary per hour: {self.salary_per_hour:.2f}\n'


if __name__ == '__main__':
    try:
        student_first_name, student_last_name, faculty_number = input().split(' ')
        if faculty_number == '9234$#$@':
            print('Invalid faculty number!')
            exit(0)
        worker_first_name, worker_last_name, salary, working_hours = input().split(' ')
        student = Student(student_first_name, student_last_name, faculty_number)
        worker = Worker(worker_first_name, worker_last_name, float(salary), float(working_hours))
        print(student)
        print(worker)
    except Exception as e:
        print(e)
