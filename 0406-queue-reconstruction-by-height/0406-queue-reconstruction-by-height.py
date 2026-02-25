class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Step 2: Insert at index k
        queue = []
        for person in people:
            queue.insert(person[1], person)
        
        return queue