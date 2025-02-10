s=input("Enter the input string: ")
i = 0
print("characters at even positions")
while i<len(s):
    print(s[i], end=' ')
    i = i + 2
print("\n")
print("characters at odd position")
i=1
while i<len(s):
    print(s[i], end=' ')
    i += 2
print("\n")