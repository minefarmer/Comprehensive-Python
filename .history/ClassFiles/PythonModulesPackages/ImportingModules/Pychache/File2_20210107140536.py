import File1 as f1

print("Hello from file 2")  # Hello from file 1

print("bla bla")  # bla bla


if __name__ == "__main__":
    print("file2 is being run as directory")  # file1 is being run as directory
else:
    print("file is being imported ")