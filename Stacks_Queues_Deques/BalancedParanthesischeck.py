'''In this problem, you have to check the whether every open bracket has a proper closing bracker
([])===> Balanced
([)]===> Not balanced'''
#https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews
def balance_check(s):
    if len(s)%2 != 0:  # Check if for every opening/closing bracket, there is another closing/opening bracket. THis is the basic check
        return False
    opening = set('{[(')  # set contains ('{','[','(')  #These are only opening paranthesis
    matches = set([('(',')'),('[',']'),('{','}')])  #{('[', ']'), ('(', ')'), ('{', '}')} It is a set of tuple pairs
    #matches = {('(', ')'), ('[', ']'), ('{', '}')}
    stack = []

    for paran in s:
        if paran in opening:        # We are checking for opening brackets here
            stack.append(paran)

        else:       # If it is a closing bracket
            if len(stack) == 0:     # Check for the presence of closing paranthesis before its opening
                return False    #becuase there was no matching opening paranthesis for the closing paranthesis
            last_open = stack.pop()
            if (last_open, paran) not in matches:   #Checking if the last opened bracket has a matching closed bracket
                return False                        # By comparing the pair with the one in the matches
    return len(stack) == 0      # if the stack is empty we also return false, because there’s no opening parenthesis associated with this closing one
print(balance_check('[](){([[[]]])}('))
print(balance_check('[{{{(())}}}]((()))'))
print(balance_check('[[[]])]'))
print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
