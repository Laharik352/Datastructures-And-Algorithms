'''Given a string, write a function that uses recursion to reverse it.'''

def reverse(s):
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]

print(reverse('abcdef'))