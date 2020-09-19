import math

income = float(input())
success = float(input())
min_salary = float(input())

social_scholarship = 0.35 * min_salary
success_scholarship = success * 25

if success <= 4.50:
    print("You cannot get a scholarship!")
else:
    if income >= min_salary and success < 5.50:
        print("You cannot get a scholarship!")

    elif income >= min_salary and success >= 5.50:
        print(f"You get a scholarship for excellent results {math.trunc(success_scholarship)} BGN")

    elif income < min_salary and success < 5.50:
        print(f"You get a Social scholarship {math.trunc(social_scholarship)} BGN")

    elif income < min_salary and success >= 5.50:
        if social_scholarship > success_scholarship:
            print(f"You get a Social scholarship {math.trunc(social_scholarship)} BGN")
        elif success_scholarship > social_scholarship:
            print(f"You get a scholarship for excellent results {math.trunc(success_scholarship)} BGN")
