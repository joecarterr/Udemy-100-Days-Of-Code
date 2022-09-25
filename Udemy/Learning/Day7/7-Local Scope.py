# scope:
enemies = 1


def increase_enemies():
    enemies = 2
    # outputs 2 (local scope)
    print(f"enemies inside function {enemies}")


increase_enemies()
# outputs 1 (local scope)
print(f"enemies outside function: {enemies}")
