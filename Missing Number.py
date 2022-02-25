# Iterative solution (slower)
# def missingNumber(self, nums: "list[int]") -> int:
#     for num in range(0, len(nums)+1):
#         if num not in nums:
#             return num       

## Using arithmetic formula
def missingNumber(self, nums: "list[int]") -> int:
    """sum of a series is n/2 * (2a + ((n-1 ) * d))
    we know that the difference is 1 and the first term is always 0, hence sum_of_series == (n/2) * (n-1)
    the sum of nums without the missing number would be sum_of_series but now it's sum_of_series - missing_num
    hence missing num == sum_of_series - sum_of_nums
    """
    n = len(nums) + 1 # length of actual series
    return int(((n / 2) * (n - 1)) - sum(nums))


## Driver code
print(missingNumber(1, [0, 3, 4, 1]))

# def ar_sum(n: "int"):
#     n = len(n)
#     print((n / 2) * (n - 1))
# ar_sum([0, 1, 3, 4]) # n = 4
# ar_sum([0, 1, 2, 3, 4]) # n = 5