# 数组常用操作

ll = ['a', 'b', 'c']
print(ll)
print(type(ll))
print(len(ll))
print(ll[0])
print(ll[1])
print(ll[2])
print(ll[-1])
print(ll[-2])
print(ll[-3])

for var in ll:
    print(f"for-in - {var}")

ll.append('d')
print(ll)

ll.insert(1, 'e')
print(f'll.insert() {ll}')

ll.pop()
print(f"ll.pop() {ll}")

ll[1] = 'f'
print(f'll.replace() {ll}')

ll.reverse()
print(f"ll.reverse() {ll}")


ls = ['ABC', 123, True, [1, 2, 3]]
print("ls->{}".format(ls))

# tuple 操作

tup = ('a', 1, True)
print(f'tup ->{tup}')

tup1 = (1,)
print(f'tup1 ->{tup1}')
