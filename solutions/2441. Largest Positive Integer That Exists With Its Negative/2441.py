def find_max_k(nums: list[int]) -> int:
    manuals = []
    for num in nums:
        if -num in nums:
            manuals.append(num)
    return max(manuals, default=-1)
