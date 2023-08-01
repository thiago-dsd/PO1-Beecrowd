nums = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

n = int(input())
for _ in range(n):
    k = input()
    num_leds = 0
    for i in k:
        num_leds += nums[i]
    print(f'{num_leds} leds')
