# merge sorting 3 arrays

def merge (a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] <= b[j] and a[i] <= c[k]:
            yield a[i]
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            yield b[j]
            j += 1
        else:
            yield c[k]
            k += 1
    while i < len(a):
        yield a[i]
        i += 1
    while j < len(b):
        yield b[j]
        j += 1
    while k < len(c):
        yield c[k]
        k += 1