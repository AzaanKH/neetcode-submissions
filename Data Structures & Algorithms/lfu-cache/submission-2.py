class LFUCache:

    def __init__(self, capacity: int):
        # freq to node
        # node to freq
        # keep track of smallest freq
        # smallest freq -> nodes should be in lru so remove the first one
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0
        self.capacity = capacity

    def _bump_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._bump_freq(key)
        return self.key_to_val_freq[key][0]
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._bump_freq(key)
        else:
            if len(self.key_to_val_freq) == self.capacity:
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[evict_key]
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1