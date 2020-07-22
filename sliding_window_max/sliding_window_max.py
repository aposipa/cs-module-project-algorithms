'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    last_index = len(nums) - k
    window_array = []

    for i in range(last_index + 1):
        current_index = i
        large_value = nums[i]

        while current_index is not i + k -1:
            if large_value < nums[current_index + 1]:
                large_value = nums[current_index + 1]
            current_index +=1

        window_array.append(large_value)
    return window_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
