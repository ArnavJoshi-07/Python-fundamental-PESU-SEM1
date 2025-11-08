def two_sum(nums, target):
    """
    Given a list of integers nums and an integer target, return indices of the two numbers such
    that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Args:
        nums (list[int]): A list of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the indices of the two numbers that sum to target.
    """
    num_map = {}  # Dictionary to store number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [] # Should not reach here based on problem statement "exactly one solution"

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = two_sum(nums1, target1)
    print(f"Input: nums={nums1}, target={target1}")
    print(f"Output: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = two_sum(nums2, target2)
    print(f"Input: nums={nums2}, target={target2}")
    print(f"Output: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = two_sum(nums3, target3)
    print(f"Input: nums={nums3}, target={target3}")
    print(f"Output: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"

    # Test case 4 (negative numbers)
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    expected4 = [2, 4]
    result4 = two_sum(nums4, target4)
    print(f"Input: nums={nums4}, target={target4}")
    print(f"Output: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"

    # Test case 5 (larger numbers)
    nums5 = [10, 20, 30, 40, 50]
    target5 = 70
    expected5 = [2, 3] # Corrected expected output
    result5 = two_sum(nums5, target5)
    print(f"Input: nums={nums5}, target={target5}")
    print(f"Output: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {result5}"

    print("\nAll test cases passed!")
