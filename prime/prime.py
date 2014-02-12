def prime_gen():
    primes = [2]
    while 1:
        cnt = primes[-1]
        yield cnt
        while 1:
            divisable = False
            cnt += 1
            for d in primes:
                if cnt % d == 0:
                    divisable = True
                    break
                if not (d < cnt*cnt):
                    break
            if not divisable:
                primes.append(cnt)
                break

if __name__ == "__main__":
    n = int(raw_input())
    a = prime_gen()
    for i in range(n):
        print a.next()
