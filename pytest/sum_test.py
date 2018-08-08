tishi = '欢迎光临，请问您几个人看电影： '
user_number = int(input(tishi))
user = 0
zongjia = []
while  True:
    if user != user_number:
        user += 1
        renshu = '请输入第' + str(user) + '位观看人员的年龄： '
        age = int(input(renshu))
        if age <= 3:
            print('\t幼儿免费观看')
        elif age <= 12:
            print('\t青少年10元半价观看')
            zongjia.append(10)
        elif age <= 60:
            print('\t成年人观看20元全价')
            zongjia.append(20)
        elif age <= 120:
            print('\t老年人10元半价观看')
            zongjia.append(10)
        elif age > 120:
            user -= 1
            print('\t不要胡闹,请重新输入')
    else:
        break
print('\n请支付：' + str(sum(zongjia)) + '元人民币！')
