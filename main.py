def findLongestIncreasingSequence(array):
    currentSequence = [array[0]]
    longestSequence = []

    for i in range(1, len(array)):
        if array[i] >= array[i - 1]:
            currentSequence.append(array[i])
        else:
            if len(currentSequence) > len(longestSequence):
                longestSequence = currentSequence
            currentSequence = [array[i]]

    if len(currentSequence) > len(longestSequence):
        longestSequence = currentSequence

    return longestSequence

def findLongestDecreasingSequence(array):
    currentSequence = [array[0]]
    longestSequence = []

    for i in range(1, len(array)):
        if array[i] <= array[i - 1]:
            currentSequence.append(array[i])
        else:
            if len(currentSequence) > len(longestSequence):
                longestSequence = currentSequence
            currentSequence = [array[i]]

    if len(currentSequence) > len(longestSequence):
        longestSequence = currentSequence

    return longestSequence

def findValues(filePath):
    with open(filePath, 'r') as f:
        arrayNumbers = []
        for line in f:
            arrayNumbers.append(int(line))

        x = int(len(arrayNumbers) / 2)
        if x % 2 == 0:
            median = (arrayNumbers[x] + arrayNumbers[x-1]) / 2
        else:
            median = arrayNumbers[x]
        

        maxNumber = max(arrayNumbers)
        minNumber = min(arrayNumbers)
        averageOfNumbers = sum(arrayNumbers) / len(arrayNumbers)
        longestSequenceByIncrease = findLongestIncreasingSequence(arrayNumbers)
        longestSequenceByDecrease = findLongestDecreasingSequence(arrayNumbers)

        return [maxNumber, minNumber, median, averageOfNumbers, longestSequenceByIncrease, longestSequenceByDecrease]





result = findValues('10m.txt')

print('Maximal number = ' + str(result[0]))
print('Minimal number = ' + str(result[1]))
print('Median = ' + str(result[2]))
print('Average = ' + str(result[3]))
print('Longest sequence by increase: ' + str(result[4]))
print('Longest sequence by decrease: ' + str(result[5]))


