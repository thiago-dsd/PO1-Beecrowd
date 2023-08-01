while True:
    n = int(input())
    
    if n == 0:
        break
    
    nums = [int(x) for x in input().split()]
    _nums = {}
    for num in nums:
        _nums[num] = 0
    
    for num in nums:
        _nums[num] += 1
        
    for num in _nums:
        if _nums[num] % 2 == 1:
            sol = num
            break

    print(sol)
