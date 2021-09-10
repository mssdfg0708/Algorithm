def solution(new_id):
    allowed_character = "0123465789abcdefghijklmnopqrstuvwxyz_-."
    # 1
    new_id = new_id.lower()
    # 2
    for i in range(len(new_id)):
        if new_id[i] in allowed_character:
            pass
        else:
            new_id = new_id.replace(new_id[i], " ")
    while " " in new_id:
        new_id = new_id.replace(" ", "")
    # 3
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # 4
    new_id = new_id.rstrip('.')
    new_id = new_id.lstrip('.')
    # 5
    if not new_id:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    # return
    return new_id


print(solution(input()))
