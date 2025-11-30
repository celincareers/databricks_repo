from functools import reduce

calc = lambda a,b : (a+b)/100
print(calc(5,10))

stringlist=[1,2,3,4,5,6]
stringvar = list(map(lambda x : x*2,stringlist))
stringmultiply= list(map(lambda x: x*10, stringlist))
print(stringmultiply)
strmul=reduce( lambda x,y:x+y, stringlist)
print("add nos =", strmul)



stringvar=['cat','dog','cow']
print(stringvar)
stringconcat = list(map(lambda x : x+'concatenation' , stringvar))
print(stringconcat)


number=[10000,2,1,2]
fun=reduce(lambda x,y:x/y , number)
print(fun)

listno=[1,2,3,4,5]
def add(a,b):
    return a+b

x=reduce(add, listno)
print (x)

sum = reduce(lambda x,y:x+y, listno) #very costly
print(sum)

maxno=max(listno) #cost effective
print(maxno)

maxno=reduce(max,listno) #very costly
print(maxno)

maxno=(lambda x:max(x)) (listno)
minno=(lambda x:min(x)) (listno)
print("max no is ", maxno)
print("min no is ", minno)
