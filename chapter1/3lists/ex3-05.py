guest_list = ["Me", "Myself", "I"]
print(f"Please come to my party, {guest_list[0]}")
print(f"Please come to my party, {guest_list[1]}")
print(f"Please come to my party, {guest_list[2]}")

print(f"{guest_list[1]} cannot make it!")
del guest_list[1]

print(f"Please come to my party, {guest_list[0]}")
print(f"Please come to my party, {guest_list[1]}")