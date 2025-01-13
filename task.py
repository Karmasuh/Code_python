def compute_lps(pattern):
    """
    Computes the LPS (Longest Prefix which is also Suffix) array for the given pattern.
    
    LPS[i] will be the length of the longest proper prefix which is also a suffix for pattern[0..i]
    """
    m = len(pattern)
    lps = [0] * m  # lps[i] stores the length of the longest prefix suffix for pattern[0..i]
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # Mismatch after length matches
            if length != 0:
                length = lps[length - 1]  # Fall back to the previous longest prefix suffix
            else:
                lps[i] = 0
                i += 1
    
    return lps


def kmp_search(text, pattern):
    """
    Searches for occurrences of the pattern in the given text using the KMP algorithm.
    
    Returns a list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    
    # Compute the LPS array for the pattern
    lps = compute_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    result = []
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            # Found a match, append the starting index
            result.append(i - j)
            j = lps[j - 1]  # Use LPS to skip unnecessary comparisons
        
        elif i < n and text[i] != pattern[j]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]  # Shift pattern using LPS array
            else:
                i += 1
    
    return result


# Example usage:
text = "ababcababcabc"
pattern = "ababc"
matches = kmp_search(text, pattern)

print(f"Pattern found at indices: {matches}")
