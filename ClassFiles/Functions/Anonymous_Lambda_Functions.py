'''                 Anonymous Functions  ===   lambda
They are defined by using the lambda keyword.
They can take several arguments but can only have one expression.


'''
a = lambda b: b + 4
print(a(4))  # 8

c = lambda d,e : d + e
print(c(7,8))  # 15




def ghost_number(n):
    return lambda f : f * n

double_num = ghost_number(2)

print(double_num(20))  # 40


