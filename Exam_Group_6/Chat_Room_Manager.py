capacity = int(input())
messages_folder = {}

while (command := input()) != "End":
    parts = command.split('=')
    action = parts[0]

    if action == 'Register':
        username = parts[1]
        if username not in messages_folder:
            messages_folder[username] = {"sent": 0, "received": 0}

    elif action == 'Send':
        sender = parts[1]
        receiver = parts[2]
        if sender in messages_folder and receiver in messages_folder:
            messages_folder[sender]['sent'] += 1
            messages_folder[receiver]['received'] += 1

            if messages_folder[sender]['sent'] + messages_folder[receiver]['received'] >= capacity:
                del messages_folder[sender]
                print(f"{sender} reached the capacity!")
            if receiver in messages_folder:
                if messages_folder[receiver]["sent"] + messages_folder[receiver]["received"] >= capacity:
                    del messages_folder[receiver]
                    print(f"{receiver} reached the capacity!")

    elif action == 'Delete':
        username = parts[1]
        if username == 'All':
            messages_folder.clear()
        elif username in messages_folder:
            del messages_folder[username]
print(f"Users count: {len(messages_folder)}")

for user, stats in messages_folder.items():
    total_messages = stats['sent'] + stats['received']
    print(f'{user} - {total_messages}.')
