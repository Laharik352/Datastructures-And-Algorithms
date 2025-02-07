'''String Compression problem
Eg. AAB ===> A2B1
    AAaa ===> A2a1
    ABCCEED ===> A1B1C2E2D1'''
def string_comp():
    s = input("Enter the string: ")
    d = {}
    output = ''
    for letter in s:
        d[letter] = d.get(letter, 0) + 1    # if the letter exists, then take that value. Else, take the default value as 0 for that letter
    for k,v in d.items():
        output += str(k)+str(v)
    print(output)
string_comp()


####################################

def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    # Intialize Values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r
print(compress('AABB'))

