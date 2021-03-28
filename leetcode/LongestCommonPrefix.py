# https://leetcode.com/problems/longest-common-prefix/
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            if len(strs) > 0:
                frame = min((word for word in strs), key=len)
                while True:
                    for w in strs:
                        while w.startswith(frame) != True:
                            frame = frame[:-1]
                        continue
                    return frame
            else:
                return ''

    if __name__ == '__main__':
        strs = ["flower", "fglow"]
        f = longestCommonPrefix(0, strs)
        print(f'res = {f}')
