class RiverCrossing:
    def __init__(self, sisters, brothers):
        self.sisters = sisters
        self.brothers = brothers
        self.goal_state = (0, 0, 30, 30, 'right')  # All on the right bank

    def is_valid_action(self, state, action):
        left_sisters, left_brothers, right_sisters, right_brothers, boat = state
        move_sisters, move_brothers = action

        # Check if the boat carries more than 4 people
        if move_sisters + move_brothers > 4 or move_sisters + move_brothers == 0:
            return False

        if boat == 'left':
            new_left_sisters = left_sisters - move_sisters
            new_left_brothers = left_brothers - move_brothers
            new_right_sisters = right_sisters + move_sisters
            new_right_brothers = right_brothers + move_brothers
        else:
            new_left_sisters = left_sisters + move_sisters
            new_left_brothers = left_brothers + move_brothers
            new_right_sisters = right_sisters - move_sisters
            new_right_brothers = right_brothers - move_brothers

        # Check for negative numbers of people
        if new_left_sisters < 0 or new_left_brothers < 0 or new_right_sisters < 0 or new_right_brothers < 0:
            return False

        # Check if sisters are outnumbered by brothers on either bank
        if new_left_sisters > 0 and new_left_sisters < new_left_brothers:
            return False
        if new_right_sisters > 0 and new_right_sisters < new_right_brothers:
            return False

        return True

    def is_goal_state(self, state):
        return state == self.goal_state

    def is_invalid_state(self, state):
        left_sisters, left_brothers, right_sisters, right_brothers, _ = state
        if (left_sisters > 0 and left_sisters < left_brothers) or (right_sisters > 0 and right_sisters < right_brothers):
            return True
        return False

    def move(self, state, action):
        left_sisters, left_brothers, right_sisters, right_brothers, boat = state
        move_sisters, move_brothers = action

        if boat == 'left':
            new_state = (left_sisters - move_sisters, left_brothers - move_brothers,
                         right_sisters + move_sisters, right_brothers + move_brothers, 'right')
        else:
            new_state = (left_sisters + move_sisters, left_brothers + move_brothers,
                         right_sisters - move_sisters, right_brothers - move_brothers, 'left')

        return new_state

def main():
    initial_state = (30, 30, 0, 0, 'left')
    river_crossing = RiverCrossing(30, 30)
    current_state = initial_state

    while not river_crossing.is_goal_state(current_state):
        print(f"Current State: {current_state}")
        action_input = input("Enter the number of sisters and brothers to move (e.g., '2 2'): ")
        try:
            move_sisters, move_brothers = map(int, action_input.split())
            action = (move_sisters, move_brothers)
            if river_crossing.is_valid_action(current_state, action):
                current_state = river_crossing.move(current_state, action)
                if river_crossing.is_invalid_state(current_state):
                    print("Invalid State: Sisters are outnumbered by brothers on one of the banks.")
                    break
            else:
                print("Invalid Action: The action is not allowed.")
        except ValueError:
            print("Invalid Input: Please enter two integers separated by a space.")

    if river_crossing.is_goal_state(current_state):
        print("Congratulations! All sisters and brothers have successfully crossed the river.")

if __name__ == "__main__":
    main()
