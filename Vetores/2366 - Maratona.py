n_post, entre = input().split()
n_post, entre = int(n_post), int(entre)
dist_post = input().split()
if dist_post.count('42195') != 1:
    dist_post.append('42195')
k = True
for x in range (0, len(dist_post)):
    dist_post[x] = int(dist_post[x])
for z in range (0, len(dist_post) - 1):
    if dist_post[z+1] - dist_post[z] > entre:
        print('N')
        k = False
        break
if k == True:
    print('S')

