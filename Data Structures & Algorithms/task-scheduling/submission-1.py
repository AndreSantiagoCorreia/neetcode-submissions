class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        A   A   A   A   A   B   B   B   B   B   C   C   C   D   E -> N = 3
        -Simulation:
        A   B   C   D   A   B   C   E   A   B   C   _   A   B   _   _   A   B   
        
        Keep track of time (it will be our result)
        First, let's compute the frequencies of each task
        - Whenever we are to pick a task, we want to pick the most frequent one
        - When we pick the most_freq, we add it to a queue with the time it can be released
        """
        ALPHABET_SIZE = 26
        frequencies = [0] * ALPHABET_SIZE
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        
        max_heap = []
        for i in range(ALPHABET_SIZE):
            if frequencies[i] > 0:
                heapq.heappush(max_heap, -frequencies[i])
        
        time = 0
        cooldown_queue = deque()
        while max_heap or cooldown_queue:
            # check queue status before deciding which task to pick (max_freq could be here)
            # only pop from queue if cooldown_time has passed
            if cooldown_queue and time >= cooldown_queue[0][1]:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])

            if max_heap:
                curr_task_freq = heapq.heappop(max_heap) + 1 # We increment 1 because we have freqs stored as negative values
                # Only append to cooldown_queue if we are not done with this task
                if curr_task_freq < 0:
                    cooldown_queue.append((curr_task_freq, time + n + 1))

            
            time += 1

        

        return time