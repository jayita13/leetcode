# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big == 0 or carType == 2 and self.medium == 0 or carType == 3 and self.small == 0:
            return False;            
        if carType == 1:
            self.big-=1;
        if carType == 2:
            self.medium-=1;
        if carType == 3:
            self.small-=1;
        return True;


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# Runtime: 239 ms, faster than 20.36% of Python3 online submissions for Design Parking System.
# Memory Usage: 14.4 MB, less than 68.60% of Python3 online submissions for Design Parking System.
