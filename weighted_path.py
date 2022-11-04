# WeightedPath 
# Data Members:
#   - mPaths: dict[int, float]
#   - mPositiveWeight: float
#   - mNegativeWeight: float
# 
# Methods:
#   - __init__(paths: list[int], startingWeight: float, positiveWeight: float, negativeWeight: float)
#   - SetPath(pathId: int, weight: float) -> float
#   - PositivePass(pathId: int) -> float
#   - NegativePass(pathId: int) -> float

class WeightedPath:
    def __init__(self, paths, startingWeight, positiveWeight, negativeWeight):
        self.mPaths = {}
        for path in paths:
            self.mPaths[path] = startingWeight

        self.mPositiveWeight = positiveWeight
        self.mNegativeWeight = negativeWeight

    def SetPath(self, pathId, weight):
        self.mPaths[pathId] = weight
        return self.mPaths[pathId]

    def PositivePass(self, pathId):
        self.mPaths[pathId] *= self.mPositiveWeight
        return self.mPaths[pathId]

    def NegativePass(self, pathId):
        self.mPaths[pathId] *= self.mNegativeWeight
        return self.mPaths[pathId]

    def GetPaths(self):
        return self.mPaths