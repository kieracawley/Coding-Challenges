// Given an array of strings, return another array containing all of its longest strings.

func allLongestStrings(inputArray: [String]) -> [String] {
    let length = longestStringLength(array:inputArray)
    var strings:[String] = []
    for string in inputArray{
        if string.characters.count == length{
            strings.append(string)
        }
    }
    return strings
}

func longestStringLength(array: [String]) -> Int{
    var length = 0
    for string in array{
        if string.characters.count > length{
            length = string.characters.count
        }
    }
    return length
}
