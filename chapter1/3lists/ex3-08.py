destinations = ["Munich", "Tokyo", "Paris", "Toronto", "Belgrade"]
mod = []

print(f"raw: {destinations}")
mod = sorted(destinations)
print(f"mod: {mod}")
print(f"raw: {destinations}")


mod = sorted(destinations)
mod.reverse()
print(f"mod: {mod}")
print(f"raw: {destinations}")

destinations.reverse()
print(f"reversed raw: {destinations}")

destinations.reverse()
print(f"raw: {destinations}")

destinations.sort()
print(f"sorted raw: {destinations}")

destinations.sort(reverse=True)
print(f"reverse sorted raw: {destinations}")