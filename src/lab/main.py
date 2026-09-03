import pandas as pd
info: str = pd.__version__

def main() -> None:
    print("-" * 40)
    print(f"pandas version: {info}")
    print("-" * 40)

if __name__ == "__main__":
    main()