import bcrypt

password= 'cantguessme'
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

hashed_str = hashed.decode('utf-8')  # Convert hash to a string for storage

hashed_from_storage = hashed_str.encode('utf-8')

if bcrypt.checkpw(password.encode('utf-8'), hashed_from_storage):
    print(f"Yaay, It Matches! Original Hash: {hashed_from_storage}and the password is {password.encode('utf-8')} and the decoded {hashed_str}")
else:
    print(f"Oops, It Does not Match :( Original Hash: {hashed_from_storage}")