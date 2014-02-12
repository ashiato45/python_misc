class Polynomial:
    coef = []
    def __init__(self, coef_):
        self.coef = coef_
    def apply(self, x_):
        s = 0
        for k, v in enumerate(self.coef):
            s += v*(x_**k)
        return s

if __name__ == "__main__":
    p = Polynomial([1, 2, 3])
    print p.apply(2)
