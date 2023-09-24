class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap={
          ')':'(',
          ']':'[',
          '}':'{'
        }
        stack=[]
        for i in s:
          if i not in bracketMap:
            stack.append(i)
          else:
            if len(stack)==0:
              return False
            if stack[-1]!=bracketMap[i]:
              return False
            stack.pop()
        
        return len(stack)==0