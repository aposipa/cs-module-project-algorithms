'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n == 3:
#             return 4
        
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# Second pass with cache improvements:
def eating_cookies(n, cache=None):
    print(n)
    if n < 0:
        return 0
    
    elif n == 0:
        return 1
    
    elif cache is not None and cache[n] > 0:
        return cache[n]

    else:
        if cache is None:
            cache = [0 for i in range(n + 1)]
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
