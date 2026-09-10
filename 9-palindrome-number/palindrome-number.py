class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        c=x[::-1]
        if x == c:
            return True 
        else:
            return False

        