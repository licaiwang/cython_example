def find(nb_primes):
    cdef list p = []
    cdef unsigned int n = 2
    cdef unsigned int i
    while len(p) < nb_primes:
        # 檢查 n 是否為質數
        for i in p:
            if n % i == 0:
                break

        # 若是質數，則放進 p
        else:
            p.append(n)
        n += 1
    return p