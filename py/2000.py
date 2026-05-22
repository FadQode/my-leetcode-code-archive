class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                rev=""
                stack = []
                for j in word[:i+1]:
                    stack.append(j)
                print(stack)
                while stack:
                    rev = rev + stack.pop()
                rev = rev + word[i+1:]
                break
            else:
                rev = word
                continue 
        
        return rev
    
# Test the function
word = "abcdefd"
ch = "z"
print(Solution().reversePrefix(word, ch))  # Output: "dcbaefd"