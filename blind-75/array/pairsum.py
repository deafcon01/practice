def pairSum(nums: list[int], target: int):
    seen = set()
    found = 0
    for value in nums:
        remain = target - value
        if remain in seen:
            print(f"Pair found ({remain}, {value})")
            found = 1
        seen.add(value)
    if found == 0:
        print("Pair not found")

if __name__ == "__main__":
    nums = [8, 7, 2, 5, 3, 1]
    target = 0
    pairSum(nums, target)