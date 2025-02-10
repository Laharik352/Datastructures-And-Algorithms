'''Input permutation: given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']'''
#Doubt
# def permute(s):
#     out = []
#     if len(s) == 1:
#         out = [s]
#     else:
#         for i, letter in enumerate(s):
#             # print("i",i)
#             # print("letter",letter)
#             for per in permute(s[:i] + s[i+1: ]):
#                 # print(s[:i] + s[i+1: ])
#                 out += [letter + per]
#                 # print('out', out)
#
#     return out
# print(permute('abc'))

def permute(data, i, length):
    if i==length:
        print(''.join(data) )
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i]
            # print(data)
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]
            # print("djslfadjsl", data)


string = "ABC"
n = len(string)
data = list(string) #Converting the string into a list
permute(data, 0, n)