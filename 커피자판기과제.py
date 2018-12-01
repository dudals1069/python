money = int(input("투입금액을 입력하세요:"))
number = int(input("주문할 커피 개수를 입력하세요:"))
coffee = number*200
if money >= 0:
    money = money - coffee
    print("거스름돈:",money)

