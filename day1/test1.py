# 字符串常用操作
a = 1
print(a)

b = 2_2_323_3232
print(b)

c = 'I am "OK"'
print(c)

d = 'I\'m "OK"'
print(d)

e = 'I\'m learn python'
print(e)

d = '''this 
is 
a 
test'''
print(d)

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print('ord("A") ==>', ord("A"))
print('chr(65) == >', chr(65))

# 要计算str包含多少个字符，可以用len()函数：
print("ABC length", len("ABC"))
print("中文 length", len("中文"))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print("ABC byte length", len(b"ABC"))
print("中文 byte length", len("中文".encode('utf-8')))

# 占位符
print("hello %s world!" % "python")

# 格式化
print("hello {} world!".format("python"))

# f-string
name = 'python'
print(f'hello {name}')
