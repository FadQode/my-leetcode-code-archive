func search(nums []int, target int) int {
    mapnums := make(map[int]bool)
    for i := 0; i < len(nums); i++{
        mapnums[nums[i]] = true
        if mapnums[target]{
            return i
        } 
    }
    return -1
}