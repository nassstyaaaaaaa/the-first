def find_missing_nums(nums):

n = nums[-1]
a = list(range(1, n+1))
k = []
for o in a:
if o not in nums: k.append(o)
return k
