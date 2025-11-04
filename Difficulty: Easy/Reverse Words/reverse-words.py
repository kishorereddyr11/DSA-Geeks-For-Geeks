class Solution:
    def reverseWords(self, s):
        s = s.strip('.').split('.')
        s.reverse()
        return '.'.join(word for word in s if word != '')
        