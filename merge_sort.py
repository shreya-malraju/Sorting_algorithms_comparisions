def mergesort(arr):
    if len(arr) > 1:
        a = len(arr)//2
        l = arr[:a]
        r = arr[a:]
        mergesort(l)
        mergesort(r)
        b = c = d = 0
        while b < len(l) and c < len(r):
            if l[b] < r[c]:
                arr[d] = l[b]
                b += 1
            else:
                arr[d] = r[c]
                c += 1
            d += 1
        while b < len(l):
            arr[d] = l[b]
            b += 1
            d += 1
        while c < len(r):
            arr[d] = r[c]
            c += 1
            d += 1
    return arr