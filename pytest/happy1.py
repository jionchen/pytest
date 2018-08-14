n=input("输入一个数字：")
n=int(n)
print(type(n))
while True:
  if n==1:
    print("aaa")
    print('%s is a happy number' %(n)) 
    break
    
  elif n==4:
    print("bbb")
    print('%s is a not  happy number' %(n))
    break
  else:
    n=str(n)
    print(n)
    for i in n:
      n=int(n)
      i=int(i)
      print(i)
      n+=i**2
      
      break
