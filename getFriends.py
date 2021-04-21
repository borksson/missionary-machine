import json

file = json.loads(open("facebook/friends/friends.json", "r").read())

with open("facebook/friends/friends.json", "r") as read_file:
    data = json.load(read_file)["friends"]

for friend in data:
	print(friend["name"])

#Now I have everyones name, I can simply search for them on Facebook and get their profile link
#With that link I can get their photo and more easily classify them+