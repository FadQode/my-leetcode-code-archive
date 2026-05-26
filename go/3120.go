func numberOfSpecialChars(word string) int {
    special_count := 0
    seen := map[rune]bool{}

    for _, c := range word{
        seen[c] = true
    }
    for i := 'A'; i <= 'Z'; i++{
        if seen[i] && seen[i+32]{
            special_count++
        }
    }

    return special_count
}