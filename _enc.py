mono = {
    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i',
    'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm',
    'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q',
    'm': 'r', 'n': 's', 'o': 't', 'p': 'u',
    'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
    'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c',
    'y': 'd', 'z': 'e', ' ': ' ',
    'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I',
    'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M',
    'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q',
    'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U',
    'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y',
    'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C',
    'Y': 'D', 'Z': 'E',
    '!': '!', '@': '@', '#': '#', '$': '$',
    '^': '^', '&': '&', '*': '*', '(': '(',
    ')': ')', '_': '_', '-': '-', '=': '=',
    '+': '+', '/': '/', '1': '1', '2': '2',
    '3': '3', '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9', ',': ',',
    '.': '.', ';': ';', ':': ':',
    ']': ']', '[': '[', '{': '}', '<': '<',
    '>': '>', '`': '`', '|': '|', '?': '?'
}
rev_mono = {val: key for (key, val) in mono.items()}


def encrypt(inp):
    inp = list(inp)
    for i in range(len(inp)):
        inp[i] = mono[inp[i]]
    out = "".join(str(x) for x in inp)
    return out


def decrypt(inp):
    inp = list(inp)
    for i in range(len(inp)):
        inp[i] = rev_mono[inp[i]]
    out = "".join(str(x) for x in inp)
    return out
