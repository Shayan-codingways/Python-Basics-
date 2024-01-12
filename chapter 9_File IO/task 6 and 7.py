with open('logfile.txt') as f:
    data=f.read()

    if 'python' in data:
        print("python present")
    else:
        print("python not present")