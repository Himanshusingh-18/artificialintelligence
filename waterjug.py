# 3 water jugs capacity -> (x, y, z) where x > y > z
# Initial state (12, 0, 0)
# Final state (6, 6, 0)

capacity = (12, 8, 5)
# Maximum capacities of 3 jugs -> x, y, z
x, y, z = capacity

# To mark visited states
memory = {}

# Store solution path
ans = []

def get_all_states(state):
    # Let the 3 jugs be called a, b, c
    a, b, c = state

    if a == 6 and b == 6:
        ans.append(state)
        return True

    # If the current state is already visited earlier
    if (a, b, c) in memory:
        return False

    memory[(a, b, c)] = 1

    # Empty jug a
    if a > 0:
        # Empty a into b
        if a + b <= y:
            if get_all_states((0, a + b, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                ans.append(state)
                return True

        # Empty a into c
        if a + c <= z:
            if get_all_states((0, b, a + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                ans.append(state)
                return True

    # Empty jug b
    if b > 0:
        # Empty b into a
        if a + b <= x:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                ans.append(state)
                return True

        # Empty b into c
        if b + c <= z:
            if get_all_states((a, 0, b + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                ans.append(state)
                return True

    # Empty jug c
    if c > 0:
        # Empty c into a
        if a + c <= x:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                ans.append(state)
                return True

        # Empty c into b
        if b + c <= y:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                ans.append(state)
                return True

    return False

initial_state = (12, 0, 0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
    print(i)
