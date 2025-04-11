def sort_on(dict: dict):
    return dict["count"]

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_count(text: str) -> int:
    char_counts = {}
    for char in text:
        base_char = char.lower()
        if base_char in char_counts:
            char_counts[base_char] += 1
        else:
            char_counts[base_char] = 1
    return char_counts

def sort_char_dict(char_counts: dict) -> list:
    sorted_counts = []
    for char, count in sorted(char_counts.items()):
        if char.isalpha():
            sorted_counts.append({"char": char.strip(),
                                "count": count})
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
