import re

def parse(text):
    stack = [{}]
    key = None

    lines = text.splitlines()

    token_re = re.compile(r'"([^"]+)"|(\{)|(\})')

    for line in lines:
        line = line.split('//', 1)[0].strip()
        if not line:
            continue

        pos = 0
        while pos < len(line):
            match = token_re.search(line, pos)
            if not match:
                break
            pos = match.end()

            if match.group(1):
                if key is None:
                    key = match.group(1)
                else:
                    stack[-1][key] = match.group(1)
                    key = None
            elif match.group(2):
                new_dict = {}
                if key is not None:
                    stack[-1][key] = new_dict
                    key = None
                stack.append(new_dict)
            elif match.group(3):
                stack.pop()

    return stack[0]