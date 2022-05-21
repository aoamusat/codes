def reverseParentheses(strr, lenn):
    st = []
    for i in range(lenn):
 
        # Push the index of the current
        # opening bracket
        if (strr[i] == '('):
            st.append(i)
 
        # Reverse the substring starting
        # after the last encountered opening
        # bracket till the current character
        elif (strr[i] == ')'):
            temp = strr[st[-1]:i + 1]
            strr = strr[:st[-1]] + temp[::-1] + \
                   strr[i + 1:]
            del st[-1]
 
    # To store the modified string
    res = ""
    for i in range(lenn):
        if (strr[i] != ')' and strr[i] != '('):
            res += strr[i]
    return res
            
        

def solution(inputString):
    lenn = len(inputString)
 
    return reverseParentheses(inputString, lenn)

string = 'foo(bar(baz))blim'
print(solution(string))
