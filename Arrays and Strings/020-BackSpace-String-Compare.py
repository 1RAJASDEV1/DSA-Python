class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def f(x):
            res = ""

            for ch in x:
                if ch == '#':
                    if len(res) > 0:
                        res = res[:-1]
                else:
                    res += ch

            return res

        return f(s) == f(t)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        j=len(s)-1
        k=len(t)-1
        s1 = ""

        x=0
        while j>=0:

            if s[j]=='#':
                x+=1
            else:
                if x==0:
                    s1=s[j]+s1
                else:
                    x-=1
            j-=1

        y=0
        t1=""
        while k>=0:

            if t[k]=='#':
                y+=1
            else:
                if y==0:
                    t1=t[k]+t1
                else:
                    y-=1 
            k-=1 

        return s1==t1