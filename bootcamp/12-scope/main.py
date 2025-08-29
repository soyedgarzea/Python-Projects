# GLOBAL SCOPE
enemies = 1


def increase_enemies():
    # LOCAL SCOPE
    enemies = 2

    # MODIFY GLOBAL
    # global enemies
    # enemies = 2

    print(f"Enemies inside {enemies}")


increase_enemies()
print(f"Enemies outside {enemies}")

# CONSTANTS
# CONSTANT_VAR = 1
