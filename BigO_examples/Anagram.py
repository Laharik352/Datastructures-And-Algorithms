'''Two check of two strings are anagrams'''
def anagram(s1, s2):
    s1 = s1.replace(' ','').lower()  #put lower to avaoid ignoring the capital letter while comparing
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)
print(anagram('clint eastwood', 'old west action'))
print(anagram('eat','tea'))


# Second Method...using dictionaries
def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1 # if the letter exists in the dictionary, increment it by 1
        else:
            count[letter] = 1   # if the letter does not exist, then add the new key with the value 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1  # if the letter exists in the dictionary, deccrement it by 1
        else:
            count[letter] = 1   # if the letter does not exist, then add the new key with the value 1
    for k in count:
        if count[k] != 0:   # for each letter in the count, check if the value is zero or not
            return False
    return True
print(anagram2('clint eastwood', 'old west action'))
print(anagram2('eat','tea'))