from collections import defaultdict
class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        
        max = float('-inf')
        for key, value in count.items():
            if value > max :
                max = value
        ans = []
        for key, value in count.items():
            if value == max:
                ans.append(key)
        ans.sort()
        return ans[0]