string = input()

while (command := input()) != "Done":
    parts = command.split()
    action = parts[0]

    if action == "Change":
        char = parts[1]
        replacement = parts[2]
        string = string.replace(char, replacement)
        print(string)

    elif action == "Includes":
        substring = parts[1]
        print("True" if substring in string else "False")

    elif action == "End":
        substring = parts[1]
        print("True" if string.endswith(substring) else "False")

    elif action == "Uppercase":
        string = string.upper()
        print(string)

    elif action == "FindIndex":
        char = parts[1]
        print(string.index(char))

    elif action == "Cut":
        start_index = int(parts[1])
        count = int(parts[2])
        string = string[start_index:start_index + count]
        print(string)
