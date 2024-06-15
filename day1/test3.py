# 条件判断
from unittest import case

a = 10
if a > 10:
    print(True)
elif a > 0:
    print(False)
else:
    print('Y')

# 模式匹配
match a:
    case 10:
        print(True)
    case 0:
        print(False)
    case _:
        print('-')

arr = ['a']
arr = ['c']
arr = ['a', 'b', 'c']

match arr:
    case ['a']:
        print('only had [a] ')
    case ['a', *s]:
        print('is ok ')
    case ['c']:
        print('is C')
