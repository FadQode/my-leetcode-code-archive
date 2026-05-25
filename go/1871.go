func canReach(s string, minJump int, maxJump int) bool {
reachable := make([]bool, len(s))
prefix := make([]int, len(s)+1)

reachable[0] = true
prefix[1] = 1

for i := 1; i < len(s); i++ {
    if s[i] == '0' {
        left := i - maxJump
        right := i - minJump

        if left < 0 {
            left = 0
        }

        if right >= 0 {
            countReachable := prefix[right+1] - prefix[left]

            if countReachable > 0 {
                reachable[i] = true
            }
        }
    }

    prefix[i+1] = prefix[i]
    if reachable[i] {
        prefix[i+1]++
    }
}

return reachable[len(s)-1]

}