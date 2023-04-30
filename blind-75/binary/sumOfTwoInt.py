from typing import List
def count_one(num:int)-> int:
    count =0
    while num:
        num&=(num-1)
        count+=1
    return count

def sum_of_two(a:int, b:int)->int:
    while b!=0:
        a,b=a^b,(a&b)<<1
    return a

def find_missing_number(nums: List[int])->int:
    xor = 0
    for i in nums:
        xor = xor ^ i
    for i in range(0, len(nums) + 1):
        xor = xor ^ i
    return xor

if __name__ == '__main__':
    # print(count_one(5))
    # print(sum_of_two(4,7))
    print(find_missing_number([0,1,2,4]))