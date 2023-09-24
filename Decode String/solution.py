class Solution:
    def decodeString(self, s: str) -> str:
        s='1['+s+']'
        return (decode(s,0,1)[0])


def decode(s,start,n):
    stack=[]
    pointer=start
    ret=''
    number=''
    while pointer < len(s): 
        if s[pointer].isnumeric():
            number+=s[pointer]
        elif s[pointer]=='[':
            x,pointer=decode(s,pointer+1,int('1' if number=='' else number))
            number='' 
            stack.append(x)
        elif s[pointer]==']':
            ret=''.join(stack) 
            break
        else:
            stack.append(s[pointer])

        pointer+=1 
        
    return [n*''.join(stack),pointer]