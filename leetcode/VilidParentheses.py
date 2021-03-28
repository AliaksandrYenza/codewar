# https://leetcode.com/problems/valid-parentheses/
# Input: s = "([)]"
# Output: false
#
# Input: s = "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        dict_brt = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        res_list = list()
        if len(s) >= 2:
            for i in s:
                if i in dict_brt.values():
                    res_list.append(i)
                    # print(f'01res_list = {res_list}')
                elif i in dict_brt.keys():
                    if len(res_list) > 0 and res_list[-1] == dict_brt[i]:
                        res_list.pop(-1)
                        # print(f'02res_list = {res_list}')
                        continue
                    else:
                        return False
        return True if len(s) >=2 and len(res_list) == 0 else False


    if __name__ == '__main__':
        f = isValid(0,'{}}')
        print(f)