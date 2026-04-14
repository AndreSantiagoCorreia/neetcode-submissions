class TimeMap:

    def __init__(self):
        """
        We can build a hashmap with the following structure:
        - key1 -> timestamp1 -> val1
               -> timestamp2 -> val2
               -> timestamp3 -> val3
        """
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Note: For all calls to set, the timestamps are in strictly increasing order.
        
        When storing a value, we will either insert the first time stamp (new dictionary)
        OR
        we will retrieve the current array (with other timestamps populated)
            and add a new timestamp->value mapping
        """
        timestamp_array = []
        if key in self.dic:
            timestamp_array = self.dic[key]
        timestamp_array.append((timestamp, value))
        self.dic[key] = timestamp_array

    def get(self, key: str, timestamp: int) -> str:
        """
        When getting a value:
        - first check if that key exists
        -- If so, retrieve it's timestamps dictionary
            and iterate through its timestamps to retrieve the value
        - When iterating, we can either:
        -- Achieve O(n) time by going through EVERY single timestamp key
        -- Achieve O(logn) time by performing binary search on it
        the input timestamp might be smaller/greater than the last "set" timestamp

        0 3 6 9 12.  => 10
        l   m    r
            l m  r   
        """        
        res = ""
        if key in self.dic:
            timestamp_array = self.dic[key]
            l, r = 0, len(timestamp_array) - 1

            # if first ever timestamp set is greater than target
            # we can return early, as it is guaranteed subsequent will be greater
            if timestamp_array[0][0] > timestamp:
                return res

            while l <= r:
                mid = l + (r - l) // 2
                mid_timestamp = timestamp_array[mid][0]
                
                # perfect match, just return
                if mid_timestamp == timestamp:
                    return timestamp_array[mid][1]
                # mid timestamp is greater than target
                # move r to mid - 1 as nothing to the right is valid
                elif mid_timestamp > timestamp:
                    r = mid - 1
                # mid timestamp is smaller than target
                # move l to mid, as mid could be the answer
                else:
                    res = timestamp_array[mid][1]
                    l = mid + 1
            
        return res








