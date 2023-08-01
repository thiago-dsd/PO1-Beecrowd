n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

_nums = {}

nums.sort()  # ordenar para o dict

for num in nums:
    _nums[num] = 0

for num in nums:
    _nums[num] += 1

for num, qtd in _nums.items():
    print(f'{num} aparece {qtd} vez(es)')
