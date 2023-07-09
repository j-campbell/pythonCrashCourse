guest_list = ["Me", "Myself", "I"]
print(f"Please come to my party, {guest_list[0]}")
print(f"Please come to my party, {guest_list[1]}")
print(f"Please come to my party, {guest_list[2]}")

print(f"{guest_list[1]} cannot make it!")
del guest_list[1]

print(f"Please come to my party, {guest_list[0]}")
print(f"Please come to my party, {guest_list[1]}")

print("More invites!")
guest_list.insert(0, "Someone")
guest_list.insert(2, "Noone")
guest_list.append("Anyone")

print(f"Please come to my party, {guest_list[0]}")
print(f"Please come to my party, {guest_list[1]}")
print(f"Please come to my party, {guest_list[2]}")
print(f"Please come to my party, {guest_list[3]}")
print(f"Please come to my party, {guest_list[4]}")