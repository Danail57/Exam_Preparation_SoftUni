sequence_of_elements = input().split()
moves = 0

while (command := input()) != "end":
    index1, index2 = map(int, command.split())
    moves += 1

    if index1 == index2 or not (0 <= index1 < len(sequence_of_elements)) or not (0 <= index2 < len(sequence_of_elements)):
        middle_index = len(sequence_of_elements) // 2
        element_to_add = f"-{moves}a"
        sequence_of_elements.insert(middle_index, element_to_add)
        sequence_of_elements.insert(middle_index, element_to_add)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[index1] == sequence_of_elements[index2]:
            element = sequence_of_elements[index1]
            print(f"Congrats! You have found matching elements - {element}!")

            first, second = sorted([index1, index2], reverse=True)
            sequence_of_elements.pop(first)
            sequence_of_elements.pop(second)
        else:
            print("Try again!")

    if not sequence_of_elements:
        print(f"You have won in {moves} turns!")
        break

if sequence_of_elements:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
