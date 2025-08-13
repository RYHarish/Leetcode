class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # if n == 1:
        #     return ["()"]
        
        visited = set()
        result = []
        queue = []
        
        queue.append(["(", n-1, n, 1])
        options = ["(", ")"]
        
        while queue:
            s,op,cl,su = queue.pop(0)
            
            
            if len(s) == 2*n and su == 0 and op == 0 and cl == 0:
                result.append(s)
                continue
                 
            for ch in options:
                
                if ch == "(" and op > 0 and su >= 0 and (s+"(", op-1, cl, su+1) not in visited:
                    queue.append([s+"(", op-1, cl, su+1])
                    visited.add((s+"(", op-1, cl, su+1))
                        
                elif ch == ")" and cl > 0 and su >= 0 and (s+")", op, cl-1, su-1) not in visited:
                    queue.append([s+")", op, cl-1, su-1])
                    visited.add((s,op,cl,su))
        
        return result
                    
                    
            
            
            
            