from sys import argv

_, work_time, work_salary, bonus = argv


def salary_count():
    salary = float(work_time) * float(work_salary) + float(bonus)
    return salary


print(f'Salary with entered parameters is: {salary_count()} $')
