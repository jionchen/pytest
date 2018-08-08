#!/env/python3
#-*- coding=utf-8 -*-
#根据人数计算电影票总价
sum=0
p=0
i=input("请问您几个人看电影：")
i=int(i)
while p<i :
    try:
     p+=1
     m=input("请问您多大：")
     m=int(m)
    except Exception:
      raise Exception("类型错误")
    if m<18:
       sum+=10
    elif m<=60:
       sum+=20
    elif m<120:
       sum+=10
    elif m>=120:
       print("滚一边去")
       p-=1
       continue
    print('第%s个人年龄是%s' %(p,m))
print('需要支付%s元' %(sum))

