def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for time in permanence_period:
        if (
            type(time) != tuple
            or len(time) != 2
            or type(time[0]) != int
            or type(time[1]) != int
            or time[0] > time[1]
            or time[0] < 0
            or time[1] < 0
        ):
            return None
        if time[0] <= target_time <= time[1]:
            count += 1

    return count
