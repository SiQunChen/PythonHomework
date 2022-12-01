from sys import stdin

if __name__ == "__main__":
    for line in stdin:
        res = ""
        line = f"({line.strip()})"

        for i, c in enumerate(line):
            if c == "[":
                res += "*("

            elif c == "]":
                res += ")+"

            elif c.isalpha():
                res += f"'{c}'+"

            else:
                res += c

        res = res.replace("+)", ")")

        print(eval(res))