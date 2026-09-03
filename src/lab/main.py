import pandas as pd
info: str = pd.__version__

def main() -> None:
    print("-" * 60)
    print(f"pandas version: {info}")
    print("-" * 60)

if __name__ == "__main__":
    main()