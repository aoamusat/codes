from typing import List
import json

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    sortedBoxes = sorted(boxTypes,  key=lambda x: (-x[1], x[0]))
    maxSize = 0
    for box in sortedBoxes:
        if truckSize > 0 and box[0] <= truckSize:
            maxSize += box[0]*box[1]
            truckSize -= box[0]
        elif truckSize > 0:
            maxSize +=  truckSize*box[1]
            break
    return maxSize  

boxTypes = json.loads(input())
truckSize = int(input())
print('boxTypes:', boxTypes, 'truckSize:', truckSize)
print(maximumUnits(boxTypes, truckSize))