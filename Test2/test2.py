nums = [1, 1, 1, 2, 2, 2, 3, 5, 5, 5]

def remove(nums) -> int:
    lenght=len(nums)
    value=int()
    index_first_duplicated = 0
    for num in range(len(nums)):
        if nums.count(num) > 2:
            nums.pop(nums.index(nums[num]))
            value = nums[num]
            if index_first_duplicated != 0:
                continue
            index_first_duplicated = nums.index(nums[num+2])
        if len(nums) < lenght:
            nums.append(value)
    return index_first_duplicated

print(remove(nums))