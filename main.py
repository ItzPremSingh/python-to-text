import ast


def main() -> None:
    with open("test.py", "r") as f:
        code = f.read()

    tree = ast.parse(code)

    return None


if __name__ == "__main__":
    main()
