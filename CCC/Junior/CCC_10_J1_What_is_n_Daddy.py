#1->(1,0)
#2->(1,1) (2,0)
#3->(1,2) (3,0)
#4->(2,2) (3,1) (4,0)
#5->(3,2) (4,1) (5,0)
#6->(3,3) (4,2) (5,1)
#7->(4,3) (5,2)
#8->(6,2) (5,3)
#9->(5,4)
#10->(5,5)
x=input()
v={
  '1':1,'2':2,'3':2,'4':3,'5':3,'6':3,'7':2,'8':2,'9':1,'10':1
}
print(v[x])
