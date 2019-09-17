input_money = float(input('please enter money'))
required_money = int(input_money)

number_of_100_dollors_bill = required_money // 100
required_money = required_money % 100

number_of_50_dollors_bill = required_money // 50
required_money = required_money % 50

number_of_20_dollors_bill = required_money // 20
required_money = required_money % 20

number_of_10_dollors_bill = required_money // 10
required_money = required_money % 10

number_of_2_dollors_coins = required_money // 2
required_money = required_money % 2

number_of_1_dollors_coins = required_money // 1
required_money = required_money % 1

required_money = int((input_money * 100) % 100) #cents

number_of_50_cents_coins = required_money // 50
required_money = required_money % 50

number_of_25_cents_coins = required_money // 25
required_money = required_money % 25

number_of_10_cents_coins = required_money // 10
required_money = required_money % 10

number_of_5_cents_coins = required_money // 5

print(number_of_100_dollors_bill, "100$")
print(number_of_50_dollors_bill, "50$")
print(number_of_20_dollors_bill, "20$")
print(number_of_10_dollors_bill, "10$")
print(number_of_2_dollors_coins, "2$")
print(number_of_1_dollors_coins, "1$")
print(number_of_50_cents_coins, "50c")
print(number_of_25_cents_coins, "25c")
print(number_of_10_cents_coins, "10c")
print(number_of_5_cents_coins, "5c")

