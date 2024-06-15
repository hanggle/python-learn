# 函数定义
def say(msg):
    print(f'i say {msg}')


say('yes')


def nothing():
    pass


nothing()


def valid_say(msg):
    if not isinstance(msg, str):
        print('msg is not a string')
        raise TypeError('msg is not a string')
    else:
        return True


print(valid_say('1'))
# print(valid_say(1))


def multiple_say(x, y, z):
    return x + 1, y + 1, z + 1


print("multiple_say :{}".format(multiple_say(1, 2, 3)))
print("multiple_say :{}".format(multiple_say('1', 2, 3)))
