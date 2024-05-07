def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return None 

def add_many(*args, raise_type_error=False):
    if raise_type_error:
        raise TypeError()
    return sum(args)

def add_numalpha(a, b):
    if isinstance(a, int) and isinstance(b, str):
        return str(a) + b
    return add_numalpha(b, a)
