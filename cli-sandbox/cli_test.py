import argparse

parser = argparse.ArgumentParser(description="My CLI tool")
parser.add_argument("filename", help="File to process")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("-o", "--output", default="out.txt", help="Output file")

args = parser.parse_args()
print(args.filename, args.verbose, args.output)