from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = dict()
    for idx,value  in enumerate(nums):
        remaining =  target - value
        if remaining in seen:
            return [seen[remaining], idx]
        seen[value]=idx
    return [-1]

if __name__ == "__main__":
    nums,target = [3,2,4],6
    print(twoSum(nums, target))