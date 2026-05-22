func findThePrefixCommonArray(A []int, B []int) []int {
    var prefix = []int{};

    if len(A) != len(B){
        return prefix
    }
    seenA := make(map[int]bool)
    seenB := make(map[int]bool)

    for i := 0 ; i < len(A) ; i++ {
        seenA[A[i]] = true
        seenB[B[i]] = true
        count := 0
        for num := range seenA{
            if seenB[num]{
                count += 1
            }
        }
        prefix = append(prefix, count)
    }
    return prefix
}