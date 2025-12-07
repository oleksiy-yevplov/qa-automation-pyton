lst=[1,2,3,4,5,6,8,56,78,99,3,5,6,78,99,34,34,66,7,88]
lst2=[]
for par_int in lst:
    if par_int%2==0:
        lst2.append(par_int)
toal=sum(lst2)    
print("Сума парних чисел:",toal)
