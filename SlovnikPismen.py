retezec1 = input("Zadej jmeno: ")
slovnik = {'a, á, b, c, č, d, ď, e, é, ě, f, g, h, ch, i, í, j, k, l, m, n, ň, o, ó, p, q, r, ř, s, š, t, ť, u, ú, ů, v, w, x, y, ý, z, ž'}
slovnik1 = {}

for retezec1 in retezec1:
    if retezec1 in slovnik:
        slovnik1[retezec1] += 1
    else:
        slovnik1[retezec1] = 1
print(slovnik1)

