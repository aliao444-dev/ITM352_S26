with open("names.txt", "r") as f:
    # .read() grabs the entire file content as one large string
    content = f.read()
    
    # .splitlines() creates a list by breaking the string at each new line
    names_list = content.splitlines()
    
    print("Names list using .read():")
    print(content)
    print(f"Total number of names: {len(names_list)}")