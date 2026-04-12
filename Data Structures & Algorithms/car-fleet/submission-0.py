class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        For each car we need to calculate at what time they will reach target.
        Since a car cannot pass another, if there is a car in front of it and:
        - curr_car_arrival < front_car_arrival, they become a single fleet and reach target at the same time
        else, they form new fleets
        """
        result = 0
        sorted_cars_by_pos = sorted(zip(position, speed)) 
        timings = []

        for p, s in sorted_cars_by_pos:
            time_to_reach_target = float(target - p) / s
            timings.append(time_to_reach_target)

        while len(timings) > 1:
            lead = timings.pop()
            if lead < timings[-1]:
                result += 1
            else: # if slower, now other cars will get to the same "slower speed"
                timings[-1] = lead

        return result + bool(timings) # remaining car is fleet (if it exists)