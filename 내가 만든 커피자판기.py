#test
coffee = 10
price = 300
while coffee > 0:
    money = int(input("금액을 넣어주세요, 커피 값은 300원입니다.: "))
    maxcoffee = money // price
    lastmoney = money % price
    if money < 300:
        print("금액이 부족합니다. %s원을 거슬러줍니다." %money)
    elif money == 300:
        print("커피를 줍니다.")
        coffee += -1
        print("커피가 %s개 남았습니다." %coffee)
    elif money > 300:
        givecoffee = int(input("커피를 몇 개 드립니까? 최대치는 {}개 입니다.: ".format(coffee if coffee < maxcoffee else coffee)))
        if givecoffee > coffee:
            print("커피의 수량이 부족합니다. 처음부터 다시 시작해주세요.")
            print("돈 %s원을 돌려줍니다." %money)
            continue
        else:
            pass
        if givecoffee <= maxcoffee:
            print("커피를 %s개 드립니다. 거스름 돈은 %s원입니다." %(givecoffee, (money-givecoffee*price)))
            coffee -= givecoffee
            print("커피가 %s개 남았습니다." % coffee)
        elif givecoffee > maxcoffee:
            print("돈이 부족합니다. %s원을 돌려드립니다." %money)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 종료합니다.')
