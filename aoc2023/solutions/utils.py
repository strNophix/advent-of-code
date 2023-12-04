from os import path


def load_input(name: str) -> str:
    input_path = path.join("./inputs", f"{name}.txt")
    with open(input_path, mode="r") as f:
        return f.read()
