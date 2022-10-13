"""
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

s는 길이가 1 이상, 100이하인 스트링입니다.

"abcde" ->	"c"
"qwer" ->	"we"
"""

def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer = s[slice(int(len(s)/2-1), int(len(s)/2+1))]
    else:
        answer = s[slice(int(len(s)/2), int(len(s)/2+1))]
    
    return answer