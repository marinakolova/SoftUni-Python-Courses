import math

hours_needed = int(input())
days = int(input())
overtime_workers = int(input())

hours_worked = days * 0.9 * 8
hours_worked += (overtime_workers * 2 * days)

if hours_worked >= hours_needed:
    print(f"Yes!{math.floor(hours_worked) - hours_needed} hours left.")
else:
    print(f"Not enough time!{hours_needed - math.floor(hours_worked)} hours needed.")
