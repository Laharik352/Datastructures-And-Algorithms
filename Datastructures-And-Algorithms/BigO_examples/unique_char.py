'''Here, find all the unique characters in a string
aaaabddcc ===> abdc
abcdee ===> abcde
Indicate whether the given string has unique characters or not'''
def unique(s):
    return set(s), len(set(s)) == len(s)
print(unique("addrfe"))


# More detailed method
def unique2(s):
    chars = set()
    for ele in s:
        # print(ele)
        if ele in chars:
            return False
        else:
            chars.add(ele)
    return True
print(unique2("abccdde"))
print(unique2("abcde"))