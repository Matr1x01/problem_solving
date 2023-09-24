class Solution:
    def calculate(self, s: str) -> int:
        numberStack=[]
        curOp="+"
        number=''
        s+="+"
        for c in s:
            if c==' ':
                continue
            if c.isdigit():
                number+=c
            else:
                if curOp=='+':
                    numberStack.append(int(number))
                elif curOp=='-':
                    numberStack.append(-int(number))
                elif curOp=='/':
                    n=numberStack.pop()
                    numberStack.append(int(n/int(number)))
                elif curOp=='*':
                    n=numberStack.pop()
                    numberStack.append(n*int(number))
                
                curOp=c
                number=''
        
        return sum(numberStack)