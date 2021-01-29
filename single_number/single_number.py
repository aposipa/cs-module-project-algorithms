'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#     x = (len(arr) -1)
#     for i in range(x):
#         index = 0
#         # loop through arr
#         while index < (x):
#             if (i != index and arr[i] == arr[index]):
#                 break
#             index += 1
#         if (index == (x)): 
#             return arr[i]

#     return -1 #not found

# new pass at code:
def single_number(arr):
    counts = {}
    # iterate through the arr
    for arr in arr: #O(n)
        if arr not in counts:
            counts[arr] = 1
        else:
            counts[arr] += 1

    for k, v in counts.items(): #O(n)
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")