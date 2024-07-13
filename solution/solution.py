class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        This function takes in a list of robot positions, healths, and directions, and returns a list of the healths of the robots that have not collided.

        Args:
            positions (List[int]): A list of robot positions.
            healths (List[int]): A list of robot healths.
            directions (str): A string of robot directions, where 'R' means right and 'L' means left.

        Returns:
            List[int]: A list of the healths of the robots that have not collided.
        """
        # Initialize two lists to store the indices of robots moving left and right
        left, right = [], []
        
        # Iterate over the robots in the order of their positions
        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            # If the robot is moving to the right, add its index to the right list
            if directions[i] == 'R':    
                right.append(i)
            else:
                # If the robot is moving to the left, it collides with the robots on the right list
                while right and healths[right[-1]] < healths[i]:
                    # If the left robot's health is greater than the right robot's health, the right robot is removed from the list and the left robot's health is decreased by 1
                    right.pop()
                    healths[i] -= 1
                # If the right list is empty or the left robot's health is not greater than the right robot's health, add the left robot's index to the left list
                if not right:   
                    left.append(i)
                # If the left robot's health is equal to the right robot's health, the right robot is removed from the list
                elif healths[right[-1]] == healths[i]:    
                    right.pop()
                # If the left robot's health is less than the right robot's health, the right robot's health is decreased by 1
                else:           
                    healths[right[-1]] -= 1
        
        # Return the health of the robots that have not collided, in the order they were given
        return [healths[i] for i in sorted(left+right)]
