"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float(input('Enter the revenue (in $) of the firm: '))
costs = float(input('Enter the costs (in $) of the firm: '))
if revenue > costs:
    print('Firm is profitable')
    revenue_prof = (revenue - costs) / revenue
    print(f'revenue profitability level is {round(revenue_prof * 100, 2)}%')
    staff = int(input('How many employees work in the firm?: '))
    profit_per_employee  = round((revenue - costs) / staff, 2)
    print(f'Profit per one employee is {profit_per_employee}$')
elif revenue == costs:
    print('Firm is zero-profitable')
else:
    print('Firm is unprofitable')
