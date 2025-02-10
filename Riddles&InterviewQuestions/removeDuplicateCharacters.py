'''Remove duplicate characters in a given string keeping only the first occurrences. For example, if the input
is ‘tree traversal’ the output will be ‘tre avsl’.'''


def removeDuplicates(string):
    result = []
    seen = set()

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)
print(removeDuplicates('tree traversal'))