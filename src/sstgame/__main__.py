import argparse
from src.sstgame import madlib
def main():
    parser = argparse.ArgumentParser(description="Generate a madlib story")
    parser.add_argument("--file", required=True, help="Path to the madlib input file")

    args = parser.parse_args()
    file_path = args.file

    madlib_result = madlib.madlib(file_path)
    print(madlib_result)

if __name__ == "__main__":
    main()