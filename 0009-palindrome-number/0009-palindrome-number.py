class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        total=0
        while x>0:
            rem=x%10
            total=total*10+rem
            x=x//10
        if total==temp:
            return True
        else:
            return False
        