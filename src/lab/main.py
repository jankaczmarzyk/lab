import pandas as pd
from lab.functions import hello
info: str = pd.__version__

def main() -> None:
    print("-" * 60)
    print(f"pandas version: {info}")
    print("-" * 60)
    print(hello())

if __name__ == "__main__":
    main()