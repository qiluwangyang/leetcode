class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        # replace返回一个字符串，原先字符串不发生改变
        res = S[:length].replace(' ', '%20')
        return res
