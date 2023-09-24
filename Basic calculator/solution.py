class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        for c in s:
            if c == ' ':
                continue
            if c!=')':
                st.append(c)
            else:
                temp=''
                while st[-1]!='(':
                    temp=st.pop()+temp
                res=calc(temp)
                st.pop()
                if res[0]=='-' and st:
                    if st[-1]=='-':
                        st[-1]='+'
                    else:
                        st[-1]='-'
                    st.append(res[1:])
                else:
                    st.append(res)
                
        
        return int(calc(''.join(st)))
        

def calc(s):
    st=[]
    op="+"
    num='0'
    s+="+"
    for c in s:
        if c.isdigit():
            num+=c
        else:
            if op=='+':
                st.append(int(num))
            elif op=='-':
                st.append(-int(num))
            num=''
            op=c
    return str(sum(st))