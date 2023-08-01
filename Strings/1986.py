_ = input()
nums = [int('0x'+x, 16) for x in input().split()]

letras = [chr(x) for x in nums]

print(''.join(letras))
