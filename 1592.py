
def reorderSpaces(text: str) -> str:
    count = 0
    textarr = text.split()
    for i in text:
        if i == ' ':
            count = count + 1
    if len(textarr) == 1:
        return textarr[0] + ' ' * count
    num = count        
    count = count // (len(textarr) - 1)
    ans = ""
    for i in range(len(textarr)):
        if i == len(textarr) - 1:
            ans += textarr[i] + ' ' * num
            break
        else:    
            ans += textarr[i] + ' ' * count
        num = num - count
    return ans

text = "  this   is  a sentence "
textt = " practice  makes   perfect "
print(reorderSpaces(text))  # Output: "practice  makes   perfect "

   