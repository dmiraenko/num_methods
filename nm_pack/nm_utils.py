# Returns the product of elements in the given list
def prod(l : list) -> float:
    v = l[0]
    for i in range(1, len(l)): v *= l[i]
    return v

# Generates all permutations of n elements, according to Heap's algorithm.
# Each successive permutation has opposite sign compared to previous.
def permutations(n : int):
    a = [_ for _ in range(n)]
    c = [0 for _ in range(n)]
    i = 1
    yield a
    while(i < n):
        if(c[i] < i):
            if(i % 2 == 0):
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]
            c[i] += 1
            i = 1
            yield a
        else:
            c[i] = 0
            i += 1

# Returns the sign of the given permutation.
def permutation_sign(p : list) -> int:
    s = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if(p[i] > p[j]): s += 1
    return 1 - 2*(s % 2)

# for p in permutations(4): print(p, permutation_sign(p))