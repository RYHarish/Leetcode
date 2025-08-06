class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token not in ["*", "+", "-", "/"]:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "*":
                    stack.append(num1 * num2)
                elif token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "/":
                    result = int(float(num1) / num2)
                    stack.append(result)
        
        return stack[0]

            