while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    maxN = max(nums)
    nums.remove(maxN)

    if nums[0]*nums[0] + nums[1]*nums[1] == maxN*maxN:
        print("right")
    else:
        print("wrong")
