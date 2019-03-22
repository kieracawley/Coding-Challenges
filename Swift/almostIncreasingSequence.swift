// Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

func almostIncreasingSequence(sequence: [Int]) -> Bool {
    var sequence2: [Int] = sequence
    var sequence3: [Int] = sequence
    let outOfOrderIndex = testArray(array:sequence)
    if outOfOrderIndex == 0{
        return true
    }
    else{
        sequence2.remove(at: outOfOrderIndex)
        let z = testArray(array:sequence2)
        if z == 0{
            return true
        }
        else{
            sequence3.remove(at: outOfOrderIndex - 1)
            let y = testArray(array: sequence3)
            if y == 0{
                return true
            }
            else{
                return false
            }
        }
    }
}

func testArray(array:[Int]) -> Int{
    for index in 0..<array.count {
        if index > 0{
            if array[index - 1] >= array[index]{
                return index
            }
        }
    }
    return 0
}
