# import socket
# 
# 
# class Resolver:
#     def __init__(self):
#         self._cache = {}
# 
#     def __call__(self, host):
#         if host not in self._cache:
#             self._cache[host] = socket.gethostbyname(host)
# 
#         return self._cache
# 
#     def clear(self):
#         self._cache.clear()
# 
#     def has_host(self, host):
#         return host in self._cache
#     
#     
# resolve = Resolver()
# resolve('sixty-north.com')
# print(resolve._cache)    

# 
# def sort_by_last_letters(strings):
#     def last_letter(s):
#         return s[-1]
#     return sorted(strings,key=last_letter)
# 
# print(sort_by_last_letters(['hello','from','a','local','finction']))

# 
# g='global'
# def outer(p='parm'):
#     l = 'local'
#     def inner():
#         print(g,p,l)
#     inner()
# outer()   

# def enclosing():
#     def local_func():
#         print('local func')
#     return local_func
# 
# lf=enclosing()
# lf()

# def outer():
#     x= 3
#     def inner(y):
#         return x+y
#     return inner 
# 
# i=outer()
# print(i(2))


# 
# print("function factiories")
# def raise_to(exp):
#     def raise_to_exp(x):
#         return pow(x,exp)
#     return raise_to_exp
# square =raise_to(2)
# print(square(5))
# print(square(9))
# cube = raise_to(3)
# print(cube(10))
# print(cube(23))

# 
# def p_decorate(func):
#     def func_wrapper(name):
#         return"<p>{0}</p>".format(func(name))
#     return func_wrapper
# 
# @p_decorate
# 
# def get_text(name):
#     return "lorem ipsum, {0} dolor  sit amet".format(name)
# print(get_text("Jhon"))



# try: 
#     
#     print(1/0)
# except ZeroDivisionError:
#     print("Nu poti imparti la zero") 
def test_catch(level):
    if level < 2:
        print(level)
    else:
        raise ValueError('test test')

try: 
    test_catch(0)
except ValueError as e:
    print("Test")
    print(e.args)