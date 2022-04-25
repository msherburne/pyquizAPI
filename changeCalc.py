def calculate_version():
    with open('version.txt', 'r') as v:
        version = v.read().strip()
    print(""" What kind of change are you making? (Maj, Min, Bug)

    """)
    current_version = version.split('.')

    value = input()
    if value == "Maj":
        current_version[0] = str(int(current_version[0]) + 1)
    elif value == "Min":
        current_version[1] = str(int(current_version[1]) + 1)
    elif value == "Bug":
        current_version[2] = str(int(current_version[2]) + 1)
    elif value == "":
        current_version = current_version
    else: 
        raise ValueError("Invalid value")

    with open('version.txt', 'w') as v:
        v.write('.'.join(current_version))
    
    return '.'.join(current_version)