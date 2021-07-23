employees = []
# データの取得
with open('input/employees.csv', encoding='utf-8') as f:
    for row in f:
        column = row.strip().split(',')
        employee_id = column[0]
        employee_name = column[1]
        
        employee = f'{employee_id}_{employee_name}'
        employees.append(employee)
        
# 並び替え
sorted_employees = sorted(employees)

# 表示
for row in sorted_employees:
    print(row)