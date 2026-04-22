import sys

path = sys.argv[1]
with open(path, encoding='utf-8') as f:
    text = f.read()

in_string = False
escape = False
found = False
for i, c in enumerate(text):
    if escape:
        escape = False
        continue
    if c == "\\":
        escape = True
        continue
    if c == '"':
        in_string = not in_string
        continue
    if in_string and c == "\n":
        print(f"LITERAL NEWLINE in string at char {i}")
        print(f"Context: {repr(text[max(0,i-80):i+80])}")
        found = True
        break

if not found:
    print("No literal newlines in strings found.")
    print(f"Total chars: {len(text)}")
