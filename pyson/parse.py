import re


OBJ_OPEN = re.compile(r"{")
OBJ_CLOSE = re.compile(r"}")
ARR_OPEN = re.compile(r"\[")
ARR_CLOSE = re.compile(r"\]")


def parse_string(json_string):
    data = None
    stack = []
    line_number = 1
    is_key = False
    is_seperated = False
    is_contained = False
    for line in json_string.split("\n"):
        parse_line(line, stack, is_key, is_seperated, is_contained)
        line_number += 1
    return {"data": data}


def parse_line(json_line, stack, is_key, is_seperated, is_contained):
    json_line = json_line.strip()
    if match := re.match(OBJ_OPEN, json_line):
        stack.append("}")
    elif match := re.match(ARR_OPEN, json_line):
        stack.append("]")
    elif match := re.match(OBJ_CLOSE, json_line):
        if not stack or stack[-1] != "}":
            return (1, match.span()[0] + 1)
        stack.pop()
    elif match := re.match(ARR_CLOSE, json_line):
        if not stack or stack[-1] != "]":
            return (1, match.span()[0] + 1)
        stack.pop()
    return (0, is_key, is_seperated, is_contained)
