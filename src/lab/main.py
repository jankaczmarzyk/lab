import pandas as pd
info: str = pd.__version__

def main() -> None:
    print("-" * 80)
    print(f"pandas version: {info}")
    print("-" * 80)

if __name__ == "__main__":
    main()