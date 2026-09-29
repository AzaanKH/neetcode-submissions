from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # username -> list of websites
        username_websites = defaultdict(list)
        # map all the users to websites
        data = sorted(zip(timestamp, username, website))  # sorts by timestamp (first element)

        for t, u, w in data:
            username_websites[u].append(w)
        # map string to occurences but need to do sliding window 
        # if the list is > 3 since it is only 3 sites
        sites_occerence = {}
        for u, sites in username_websites.items():
            seen = set()
            for combo in combinations(sites, 3):
                if combo not in seen:
                    seen.add(combo)
                    sites_occerence[combo] = sites_occerence.get(combo, 0) + 1

        max_count = max(sites_occerence.values())
        res = [p for p, c in sites_occerence.items() if c == max_count]
        return list(min(res))