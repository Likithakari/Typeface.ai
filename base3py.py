class base3:
    def solve(self, n):
        s='-' if n < 0 else ''
        n= abs(n)
        if n<3:
            return str(n)
        ss =''
        while n!=0:
            s= str(n%3) +s
            n=n//3
        return s+ss 
ans= base3()
print(ans.solve(10))
