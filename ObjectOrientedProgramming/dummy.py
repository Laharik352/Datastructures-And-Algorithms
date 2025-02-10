# def maximumToys(prices, k):
#     count=0
#     for i in range(len(prices)):
#         if prices[i]<=k:
#             k-=prices[i]
#             count+=1
#         else:
#             continue
#     return count
# print(maximumToys([1,2,3,4,1],7))

# def activityNotifications(expenditure, d):
#     notif = 0
#     for i in range(d+1,len(expenditure)+1):
#         print(d+1, len(expenditure)+1)
#         exp = sorted(expenditure[(i-1)-d:i-1])
#         if d%2==1:
#             med = exp[d//2]
#         else:
#             med = (exp[d//2-1]+exp[d//2+1])//2
#         if expenditure[i-1]>=med*2:
#             notif+=1
#     return notif
# foo = "42333116"
# c = ''.join([j for i,j in enumerate(foo) if j not in foo[:i]])
# print(c)
# a = "The fat monkey"
# a = a.split()[::-1]
# print(a)
# b = []
# for i in a :
#     b.append(''.join(i[::-1]))
# print(b)
def add1(*a):
    sum = 0
    for i in a:
        sum+=i
    print(sum)
add1(1,2,3)
add1(1)
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"....",v)
display(name = "yash", salary = 1000)
display(name ="bum", salary = 1001)


from random import randint
for i in range(5):
    print(randint(0,9),randint(0,9), sep='')
