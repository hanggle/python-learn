# 循环

arr = ['a', 1, False, [1, 2, 3]]

for i in arr:
    print(f"for in read is {i}")

print('arr rang read', list(range(6)))

# 字典
dic = {'a': 1, 'b': 2, 'c': 3}
for i in dic:
    print(f"for in read dic is {i} -> {dic[i]}")

if 'a' in dic:
    print(f"for in read dic a is {dic['a']}")

# 找到a返回值
print(f"dic.get('a') ->{dic.get('a')}")
# 找不到’aa‘返回None
print(f"dic.get('aa') ->{dic.get('aa')}")
# 找不到’aa‘返回自己制定值 -1
print(f"dic.get('aa') ->{dic.get('aa', -1)}")

dic.pop('a')
print(f"删除一个key a 后的值 {dic}")

# set
s = {'a', 'b', 'c'}
print(f'set s ->{s}')

s.add('e')
print(f'set s add->{s}')

s.remove('a')
print(f'set s remove->{s}')

s1 = {1, 2, 3, 4}
s2 = {3, 5, 6, 7}

print(f's1&s2 ->{s1 & s2}')
print(f's1|s2 ->{s1 | s2}')
