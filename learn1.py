# -*- encoding=UTF-8 -*-
import requests
import random
import re

def demo_string():
    stra = 'hello world'
    print(stra.capitalize())
    print(stra.replace('hello', 'Hello'))
    strb = '\n\rhello nowcoder \r\n'
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    strc = 'hello w'
    print(3, strc.startswith('hel'))
    print(4, strc.endswith('x'))
    print(5, strc + strb + strc)
    print(6, len(strc))
    print(7, '-'.join(['a', 'b', 'c', 'd']))
    print(8, strc.split(' '))
    print(9, strc.find('ello'))
def demo_operation():
    print(1, 1+2 , 5/2, 5*2, 5-2)
    print(2, True, not True)
    print(3, 1 < 2,5 > 2)
    print(4, 2 << 3)
    print(5, 5 | 3, 5 & 3, 5 ^ 3)
    x = 2
    y = 3.3
    print(x, y, type(x), type(y))

if __name__ ==  '__main__':
     '''
     user1 = User('ul',l)
     print(user1)
     '''
     print('hello newworld')
     # demo_string()
     demo_operation()


     
            

