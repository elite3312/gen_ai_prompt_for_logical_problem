# from collections import deque
#
# # Maximum number of people the boat can carry
# BOAT_CAPACITY = 4
# # Total number of sisters
# NUM_SISTERS = 30
# # Total number of brothers
# NUM_BROTHERS = 30
#
# # State representation: (left_sisters, left_brothers, right_sisters, right_brothers, boat_side)
# # boat_side: 0 means the boat is on the left bank, 1 means it's on the right bank
# initial_state = (NUM_SISTERS, NUM_BROTHERS, 0, 0, 0)
# goal_state = (0, 0, NUM_SISTERS, NUM_BROTHERS, 1)
#
# # Check if a state is valid according to the rule that sisters can't be outnumbered by brothers on either bank
# def is_valid_state(state):
#     left_sisters, left_brothers, right_sisters, right_brothers, _ = state
#     return (left_sisters == 0 or left_sisters >= left_brothers) and \
#            (right_sisters == 0 or right_sisters >= right_brothers)
#
# # Generate all possible next states from the current state
# def generate_next_states(state):
#     next_states = []
#     left_sisters, left_brothers, right_sisters, right_brothers, boat_side = state
#     for sisters in range(BOAT_CAPACITY + 1):
#         for brothers in range(BOAT_CAPACITY + 1 - sisters):
#             if sisters + brothers > 0 and sisters + brothers <= BOAT_CAPACITY:
#                 if boat_side == 0:
#                     new_left_sisters = left_sisters - sisters
#                     new_left_brothers = left_brothers - brothers
#                     new_right_sisters = right_sisters + sisters
#                     new_right_brothers = right_brothers + brothers
#                     new_boat_side = 1
#                 else:
#                     new_left_sisters = left_sisters + sisters
#                     new_left_brothers = left_brothers + brothers
#                     new_right_sisters = right_sisters - sisters
#                     new_right_brothers = right_brothers - brothers
#                     new_boat_side = 0
#                 new_state = (new_left_sisters, new_left_brothers, new_right_sisters, new_right_brothers, new_boat_side)
#                 if is_valid_state(new_state):
#                     next_states.append(new_state)
#     return next_states
#
# # Breadth-first search to find the solution
# def solve():
#     visited = set()
#     queue = deque([(initial_state, [])])
#     while queue:
#         current_state, path = queue.popleft()
#         if current_state == goal_state:
#             return path
#         visited.add(current_state)
#         for next_state in generate_next_states(current_state):
#             if next_state not in visited:
#                 sisters_moving = abs(current_state[0] - next_state[0])
#                 brothers_moving = abs(current_state[1] - next_state[1])
#                 direction = "right" if current_state[4] == 0 else "left"
#                 move_info = f"Move {sisters_moving} sisters and {brothers_moving} brothers to the {direction} bank"
#                 new_path = path + [move_info, next_state]
#                 queue.append((next_state, new_path))
#     return None
#
# solution_path = solve()
# if solution_path:
#     print("Initial state:")
#     print(f"Left bank - Sisters: {initial_state[0]}, Brothers: {initial_state[1]}, Right bank - Sisters: {initial_state[2]}, Brothers: {initial_state[3]}, Boat is on {'left' if initial_state[4] == 0 else 'right'} bank")
#     for step, element in enumerate(solution_path):
#         if isinstance(element, tuple):
#             state = element
#             print(f"Step {step // 2}: Left bank - Sisters: {state[0]}, Brothers: {state[1]}, Right bank - Sisters: {state[2]}, Brothers: {state[3]}, Boat is on {'left' if state[4] == 0 else 'right'} bank")
#         else:
#             print(f"Step {step // 2}: {element}")
# else:
#     print("No solution found.")

from collections import deque

# State representation: (left_sisters, left_brothers, right_sisters, right_brothers, boat_side)
# boat_side: 0 means the boat is on the left bank, 1 means it's on the right bank

# Check if a state is valid according to the sisters not being outnumbered by brothers condition
def is_valid_state(state):
    left_sisters, left_brothers, right_sisters, right_brothers, _ = state
    if left_sisters > 0 and left_brothers > left_sisters:
        return False
    if right_sisters > 0 and right_brothers > right_sisters:
        return False
    return True

# Generate all possible next states from the current state
def generate_next_states(current_state):
    next_states = []
    left_sisters, left_brothers, right_sisters, right_brothers, boat_side = current_state
    max_people_in_boat = 4
    # Decide which side to load people from based on the boat's position
    if boat_side == 0:
        sisters_range = range(left_sisters + 1)
        brothers_range = range(left_brothers + 1)
    else:
        sisters_range = range(right_sisters + 1)
        brothers_range = range(right_brothers + 1)

    for num_sisters in sisters_range:
        for num_brothers in brothers_range:
            if num_sisters + num_brothers > 0 and num_sisters + num_brothers <= max_people_in_boat:
                if boat_side == 0:
                    new_left_sisters = left_sisters - num_sisters
                    new_left_brothers = left_brothers - num_brothers
                    new_right_sisters = right_sisters + num_sisters
                    new_right_brothers = right_brothers + num_brothers
                    new_boat_side = 1
                else:
                    new_left_sisters = left_sisters + num_sisters
                    new_left_brothers = left_brothers + num_brothers
                    new_right_sisters = right_sisters - num_sisters
                    new_right_brothers = right_brothers - num_brothers
                    new_boat_side = 0
                new_state = (new_left_sisters, new_left_brothers, new_right_sisters, new_right_brothers, new_boat_side)
                if is_valid_state(new_state):
                    next_states.append(new_state)
    return next_states

# Breadth-first search to find the solution
def solve():
    start_state = (30, 30, 0, 0, 0)
    visited = set()
    queue = deque([(start_state, [])])
    while queue:
        current_state, path = queue.popleft()
        if current_state[2:] == (30, 30, 1):  # All people are on the right bank and the boat is there too
            return path + [current_state]
        visited.add(current_state)
        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None

solution_path = solve()
if solution_path:
    for i in range(len(solution_path) - 1):
        current_state = solution_path[i]
        next_state = solution_path[i + 1]
        left_sisters_change = current_state[0] - next_state[0]
        left_brothers_change = current_state[1] - next_state[1]
        right_sisters_change = next_state[2] - current_state[2]
        right_brothers_change = next_state[3] - current_state[3]
        boat_movement = "from left to right" if current_state[4] == 0 and next_state[4] == 1 else "from right to left"
        print(f"Step {i + 1}: The boat moves {boat_movement} carrying {abs(left_sisters_change)} sisters and {abs(left_brothers_change)} brothers.")
        print(f"Left Bank - Sisters: {next_state[0]}, Brothers: {next_state[1]}, Right Bank - Sisters: {next_state[2]}, Brothers: {next_state[3]}")
else:
    print("No solution found.")