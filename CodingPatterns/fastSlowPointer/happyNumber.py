"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast = self.digitSquareSum(n)
        while(slow != fast):
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
        return slow==1
        
    def digitSquareSum(self, n):
        sqsum=0
        while n:
            rem=n%10
            sqsum+=rem*rem
            n//=10
        return sqsum