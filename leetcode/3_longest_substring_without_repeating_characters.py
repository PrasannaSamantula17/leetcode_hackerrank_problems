# Time Complexity - O(n og n)
# Space Complexity - O(1) or O(n)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest and heaviest person can fit in one boat
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always gets a boat (either with the lightest or alone)
            right -= 1
            boats += 1
            
        return boats
        
        return res
