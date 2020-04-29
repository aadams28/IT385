#!/usr/bin/python3

# Create dictionary object
eng2esp = { "one":"uno", "two":"dos", "three":"tres" }

print(eng2esp)

# View elements
print(eng2esp["one"])
print(eng2esp['three'])

# add and remove items from dictionary
eng2esp.update({"four":"cuatro", "five":"cinco"})
eng2esp.pop("two")
print(eng2esp)

# show all keys and valuess
print(eng2esp.keys())
print(eng2esp.values())

