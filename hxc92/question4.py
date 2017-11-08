class Fibo:
    @staticmethod
    def get_all(n):  # 用于获取斐波那契数列前n+1个值,也可以通过列表获取任意值
        seq = list()
        for i in range(n+1):
            if len(seq) == 0:
                seq.append(0)
            elif len(seq) == 1:
                seq.append(1)
            else:
                seq.append(seq[i-1] + seq[i-2])
        return seq

    def get_certain_rec(self, n):  # 递归获取斐波那契数列第n+1个值
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.get_certain_rec(n - 1) + self.get_certain_rec(n - 2)

    @staticmethod
    def get_certain(n):  # 迭代方式
        fibo_0 = 0
        fibo_1 = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n+1):
                fibo_n = fibo_0 + fibo_1
                fibo_0, fibo_1 = fibo_1, fibo_n
        return fibo_n


f = Fibo()
print(f.get_certain(20))
print(f.get_certain_rec(20))
print(f.get_all(20))
