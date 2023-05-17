def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return print([hash_map[diff], i])
        hash_map = i


# For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# test1, target1 = [10, 15, 3, 7]


def nestedloops(lst, k):
    for num1 in lst:
        for num2 in lst:
            if num1 + num2 == k & num1 != num2:
                return True
    return False


def minus(lst, k):
    for num1 in lst:
        if k - num1 in lst:
            return True
    return False


def sets(lst, k):
    seen = set()
    for num1 in lst:
        if k - num1 in seen:
            return True
        seen.add(num1)
    return False


def enum(lst, k):
    return any(k - num in lst[:i] for i, num in enumerate(lst))


print(enum([10, 15, 3, 7], 17))
