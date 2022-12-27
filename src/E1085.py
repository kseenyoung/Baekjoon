nums = list(map(int, input().split()))

result = min(nums[0], nums[2] - nums[0])
if result > min(nums[1], nums[3] - nums[1]):
    result = min(nums[1], nums[3] - nums[1])

print(result)