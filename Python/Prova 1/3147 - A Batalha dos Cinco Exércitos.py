h, e, a, o, w, x = input().split()
h = int(h)
e = int(e)
a = int(a)
o = int(o)
w = int(w)
x = int(x)
bem = h + e + a + x
mal = o + w
if bem > mal:
    print('Middle-earth is safe.')
if mal > bem:
    print('Sauron has returned.')

