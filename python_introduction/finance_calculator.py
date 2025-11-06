income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
project_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
project_savings = int(project_savings)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${project_savings}")

