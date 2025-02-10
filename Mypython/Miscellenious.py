import time
currmonth = time.strftime("%b").lower()
datlst=["15-oct","21-dec","11-jan","10-apr","1-oct","25-oct"]
lst = filter(lambda i:i.split("-")[1]==currmonth, datlst)
print(list(lst))

numlst = [10,20,30,None,None,40,50,None,60,None]
numlst = filter(None, numlst)
print(list(numlst))

a = [10,20,30,21,23,25]
lst = filter(lambda x:x%2==0, a)
print(list(lst))

numlst = [1,2,54,3,76,34,76,32,31]
lst = [elm for elm in numlst if elm%2==0]
print(lst)

alst = [10,20,30,40,50]
blst = [1,2,3,4,5]
clst= map(lambda x,y : x+y , alst,blst)
print(list(clst))


from functools import reduce
rlst = [10,20,30,40,50]
rlst = reduce(lambda x,y:x+y, rlst)
print(rlst)

alst = ["arun","hari","manu","yash"]
blst = [10,20,30,40]
elst = {elem1:elem2 for elem1, elem2 in zip(alst,blst)}
print(elst)
elst2 = dict(zip(alst,blst))
print(elst2)


def trycheck():
    try:
        1/0
        #return 2
    except:
        print("Cant divide by zero")
        return 0
    finally:
        print("Can't divide by zero")
        return 1
print(trycheck())
# when there is an exception in try, the print statements present in except block will be executed first and then those present in the finally block will be executed.
# When it comes to return statements, only one return statement, will be executed in the entire try-except-finally.
# Highest priority will be given to the return statement present in finally block
# You'll notice that python always returns the last thing to be returned and the return statement will be executed in the end
