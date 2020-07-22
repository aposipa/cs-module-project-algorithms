'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    x = (len(arr) -1)
    for i in range(x):
        index = 0
        # loop through arr
        while index < (x):
            if (i != index and arr[i] == arr[index]):
                break
            index += 1
        if (index == (x)): 
            return arr[i]

    return -1 #not found


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")