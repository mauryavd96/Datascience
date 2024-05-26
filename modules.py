def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def smart_sub(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
sub=smart_sub(sub)

def div(a,b):
    return a/b
def multi(a,b):
    return a*b