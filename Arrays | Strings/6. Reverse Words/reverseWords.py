def reverse_words(s: str) -> str:
    s = s.split()
    return ' '.join(s[:: -1])
