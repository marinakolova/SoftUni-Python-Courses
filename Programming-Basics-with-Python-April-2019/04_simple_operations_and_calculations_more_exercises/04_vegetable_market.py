vegetables_price = float(input())
fruits_price = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())
total_income_bgn = vegetables_price * kg_vegetables + fruits_price * kg_fruits
total_income_euro = total_income_bgn / 1.94
print(total_income_euro)
# judge 0/100
# zero test 1:
#   expected output: 101
#         my output: 101.0
# zero test 2:
#   expected output: 20.6185567010309
#         my output: 20.61855670103093
