

def readFileToString(fileName):
    try:
        with open(fileName, "r") as f:
            return f.read()
    
    except Exception as e:
        print("Couldn't read file "+fileName+"!")
        print(e)