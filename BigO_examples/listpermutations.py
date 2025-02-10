# import time
# import matplotlib
# import matplotlib.pyplot as plt

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            # print(xs)
            for p in perm1(xs):
                l.append([x] + p)
                # print("**",l)
        return l
data = [1,2,3]
print(perm1(data))

# list of ways of splitting a list into two parts
def splits(lst):
    for i in range(len(lst)+1):
        yield [lst[:i], lst[i:]]
i = splits(data)
print(next(i))
print(next(i))
print(next(i))
print(next(i))


'''def perm2(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm2(xs):
                yield [x] + p

# http://stackoverflow.com/questions/2710713/algorithm-to-generate-all-possible-permutations-of-a-list
# from zhywu at stackoverflow.com
def perm3(lst):
    if len(lst) <= 2:
        yield lst
        lst = lst[::-1]
        yield lst
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm3(xs):
                yield [x]+p

# from Peter Breuer at stackoverflow (ported from Haskell)
def perm4(lst):
    if len(lst) <= 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for p in perm4(lst[1:]):
            for a, b in splits(p):
                yield a + [lst[0]] + b

# list of ways of splitting a list into two parts
def splits(lst):
    for i in xrange(len(lst)+1):
        yield [lst[:i], lst[i:]]


def perm5(xs, low=0):
    if low + 1 >= len(xs):
        yield xs[:]
    else:
        for p in perm5(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in perm5(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

def test(fs, maxlen=5):
    res = []
    for f in fs:
        r = []
        for i in range(maxlen):
            data = range(i)
            start = time.time()
            for p in f(data):
                pass
            end = time.time()
            r.append(end-start)
        res.append(r)
    return res'''

# if __name__ == '__main__':
# 	data = range(3)
# 	print perm1(data)
# 	#print [p for p in perm2(data)]
# 	#print [p for p in perm3(data)]
# 	#print [p for p in perm4(data)]
# 	print [p for p in perm5(data)]
# 	for p in perm5(data):
# 		print p
# 	exit()
# 	res = test([perm1, perm2, perm3, perm4, perm5], 10)
# 	fig = plt.figure(dpi=90)
# 	ax = fig.add_subplot(111)
# 	for r in res:
# 		ax.plot(r)
# 	ax.legend(['perm1', 'perm2', 'perm3', 'perm4', 'perm5'],
# 		loc='upper center',
# 		#bbox_to_anchor=(0.5, 1.05),
# 		ncol=2, fancybox=True, shadow=True)
# 	#ax.set_yscale('log')
# 	plt.show()