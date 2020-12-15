

def logged_user(objects,username):
    for obj in objects:
        obj.logged_user = username
    # print(objects)
    return objects