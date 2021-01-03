def mynum(a):  # the outside function.
    def num(a):  # This is a nested function.
        return a + 1
    result = num(a)
    return result
print(mynum(4))  # 5  # this is line 3 + line 4

