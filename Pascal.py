nums = [4,2,4,3,2]
index = [0,0,1,3,1]
for _ in range(len(index)):
    index[_] += index.count(index[_]) - 1
d = {key: value for key, value in zip(index, nums)}
for _ in range(len(nums)):
    nums[_] = d[_]
print(nums)
