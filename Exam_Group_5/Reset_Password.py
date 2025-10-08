password = input()

while (command := input()) != 'Done':
    parts = command.split()

    if parts[0] == "TakeOdd":
        password = ''.join([password[i] for i in range(len(password)) if i % 2 == 1])
        print(password)
    elif parts[0] == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif parts[0] == "Substitute":
        substring = parts[1]
        substitute = parts[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
