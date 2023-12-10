def day1code(trajectory_string):
    trajectory_list = trajectory_string.split(", ")

    north_from_start = 0
    west_from_start = 0

    previous_trajectory = "N"
    possible_trajectories = ["N", "E", "S", "W"]
    for trajectory in trajectory_list:
        current_trajectory = ""
        # determining trajectory
        if "L" in trajectory:
            current_trajectory = possible_trajectories[
                possible_trajectories.index(previous_trajectory) - 1
            ]
        elif "R" in trajectory:
            if (
                possible_trajectories.index(previous_trajectory)
                == len(possible_trajectories) - 1
            ):
                current_trajectory = possible_trajectories[0]
            else:
                current_trajectory = possible_trajectories[
                    possible_trajectories.index(previous_trajectory) + 1
                ]

        # parsing
        move_count = int(trajectory[1:])

        # actual operations
        if current_trajectory == possible_trajectories[0]:
            north_from_start += move_count
        elif current_trajectory == possible_trajectories[1]:
            west_from_start -= move_count
        elif current_trajectory == possible_trajectories[2]:
            north_from_start -= move_count
        elif current_trajectory == possible_trajectories[3]:
            west_from_start += move_count

        previous_trajectory = current_trajectory
    # print(f"Distance from start is {north_from_start} North, {west_from_start} West == {abs(north_from_start) + abs(west_from_start)}")
    return abs(north_from_start) + abs(west_from_start)
