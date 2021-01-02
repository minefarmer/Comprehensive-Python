'''                 Continue Statements
Used to stop the current iteration and continue with the next iteration of the loop.

'''
i = 0

while i < 8:
    i += 1
    if i==4:
        continue
    print(i)  # 1
            # 2
            # 3
            # skipped
            # 5
            # 6
            # 7
            # 8
