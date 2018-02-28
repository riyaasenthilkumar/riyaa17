num=int(input("Enter anumber:"))
sum=0
temp=num
while temp>0:
      digit=temp%10
      sum+=digit**3
      temp//=10
if num==sum:
      print(num,"is an armstrong number")
else:
      print(num,is an not armstrong number")
      
