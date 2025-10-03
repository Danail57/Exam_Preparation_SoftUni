n = int(input())
user_activity = {}

while (command := input()) != "End":
    parts = command.split("=")
    action = parts[0]

    if action == 'Add':
        username = parts[1]
        logins = int(parts[2])
        posts = int(parts[3])
        comments = int(parts[4])
        if username not in user_activity:
            user_activity[username] = {"logins": logins, "posts": posts, "comments": comments}
        else:
            continue

    elif action == 'Update':
        username = parts[1]
        new_logins = int(parts[2])
        if username in user_activity:
            user_activity[username]['logins'] = new_logins

    elif action == 'Remove':
        username = parts[1]
        if username in user_activity:
            user_activity.pop(username, None)

for data_user_activity, stats in user_activity.items():
    print(f'{data_user_activity} -> Logins: {stats["logins"]}, Posts: {stats["posts"]}, Comments: {stats["comments"]}')
