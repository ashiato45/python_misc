def power_combination(elem, length):
    if length == 1:
        return [[e] for e in elem]
    else:
        base = power_combination(elem, length - 1)
        res = []
        for i in elem:
            res += [[i] + b for b in base]
        return res

if __name__ == "__main__":
    print power_combination(range(3), 3)
