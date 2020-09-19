n = int(input())
salary = int(input())

reductions = {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50
}

for i in range(0, n):
    website = input()
    if website in reductions:
        salary -= reductions[website]
    if salary <= 0:
        print("You have lost your salary.")
        exit()

print(salary)
