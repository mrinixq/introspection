import  inspect

animals = ['cat', 'tiger', 'dog']

def introspection_info(obj):
    print('')


Inf1=introspection_info(animals)
print(inspect.getmembers(Inf1))
print(type(Inf1))
print(dir(Inf1))
print(callable(Inf1))