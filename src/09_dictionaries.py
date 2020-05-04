#
#! A Dictionary is a colletion which is unordered, changeable, and indexed. No duplicate members
"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat": 329, "lon": 84401, "name": "home"})
print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the waypoints list.
# YOUR CODE HERE
waypoints[0]["name"] = "not a real place"
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for i in waypoints:
    print("name:{}, location: {}, {}".format(i["name"], i["lat"], i["lon"]))

for index in range(len(waypoints)):
    for key in waypoints[index]:
        print(waypoints[index][key])

print("-----------------------------")

person = {
    'first_name': "John",
    'last_name': "Doe",
    'age': 42
}
print(person)
print(person["first_name"])
print(person.get("last_name"))

person['phone'] = "555-555-5555"

print("keys", person.keys())
print("items", person.items())

person2 = person.copy()
person2['city'] = "Ogden"
print("copy/add", person2)

del(person["age"])
person.pop("phone")
print("delete", person)

person.clear()
print("clear", person)

print("length", len(person2))
