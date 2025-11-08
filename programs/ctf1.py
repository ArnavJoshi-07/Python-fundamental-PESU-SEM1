
# Hidden flag extractor from invisible characters in text
# Copy the entire text of the CTF riddle into the 'text' variable exactly as-is

text = """
An attacking bull, a symbol of sheer power and strength, is set free in a huge field, bustling with life and death alike, a titan frozen mid-charge. It weathers the seasons at the foot of towering ambition, its gaze fixed on the flow of fortune and despair. Its gleaming form an altar for the hopeful and a testament to the untamed spirit of the bull. The bull isn’t the only one of its kind, there exists a rather troublesome homegrown counterpart, planted not by surprise but careful planning, only to be shooed away by the fed up villagers. Find me this bull.
"""  # paste exactly including spaces

# Zero-width characters to check:
# U+200B: ZERO WIDTH SPACE → 1
# U+200C: ZERO WIDTH NON-JOINER → 0
# (other zero-widths can be added if needed)

zero_map = {
    '\u200B': '1',
    '\u200C': '0'
}

bits = ""
for c in text:
    if c in zero_map:
        bits += zero_map[c]

# Now, group bits into bytes
flag = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        flag += chr(int(byte, 2))

print("Hidden flag:", flag)


### How it works:

