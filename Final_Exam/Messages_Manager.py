capacity = int(input())
sent_messages = {}
received_messages = {}

while (command := input()) != "Statistics":
    parts = command.split('=')
    action = parts[0]

    if action == "Add":
        username = parts[1]
        sent = int(parts[2])
        received = int(parts[3])
        if username not in sent_messages and username not in received_messages:
            sent_messages[username] = sent
            received_messages[username] = received
        else:
            continue

    elif action == "Message":
        sender = parts[1]
        receiver = parts[2]
        if sender in sent_messages and receiver in received_messages:
                sent_messages[sender] += 1
                received_messages[receiver] += 1

        if sent_messages[sender] + received_messages[sender] >= capacity:
            print(f"{sender} reached the capacity!")
            del sent_messages[sender]
            del received_messages[sender]
        if receiver in sent_messages and receiver in received_messages:
            if sent_messages[receiver] + received_messages[receiver] >= capacity:
                del sent_messages[receiver]
                del received_messages[receiver]
                print(f"{receiver} reached the capacity!")

    elif action == "Empty":
        username = parts[1]
        if "All" == str(username):
            sent_messages.clear()
            received_messages.clear()
        else:
            sent_messages.pop(username, None)
            received_messages.pop(username, None)
print(f"Users count: {len(sent_messages)}")

for user in sent_messages:
    total_messages = sent_messages[user] + received_messages[user]
    print(f"{user} - {total_messages}")
