import re

def _parse(text):
    stack = [{}]
    key = None

    lines = [line.split('//', 1)[0].strip() for line in text.splitlines() if line.strip()]

    token_re = re.compile(r'"((?:\\.|[^"\\])*)"|(\{)|(\})')

    for line in lines:
        pos = 0
        while pos < len(line):
            match = token_re.search(line, pos)
            if not match:
                break
            pos = match.end()

            if match.group(1):
                value = match.group(1).replace(r'\"', '"')
                if key is None:
                    key = value
                else:
                    stack[-1][key] = value
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