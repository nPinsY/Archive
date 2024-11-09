import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py 'DATABASE'.csv 'SEQUENCE'.txt")

    with open(sys.argv[2], "r") as seq_file:
        sequence = seq_file.read()

    with open(sys.argv[1], "r") as database_file:
        database = list(csv.DictReader(database_file))

    dna_strs = database[0].keys() - ["name"]

    results = [count(sequence, str_) for str_ in dna_strs]

    match_name = match(database, dna_strs, results)
    print(match_name)


def match(database, dna_strs, results):
    str_results = [str(result) for result in results]

    for person in database:
        person_str_counts = [person[str_] for str_ in dna_strs]

        if person_str_counts == str_results:
            return person["name"]

    return "No match"


def count(s, match):
    match_length = len(match)
    max_count = 0
    current_count = 0
    i = 0

    while i < (len(s) - match_length + 1):
        if s[i : i + match_length] == match:
            current_count += 1
            i += match_length
        else:
            max_count = max(max_count, current_count)
            current_count = 0
            i += 1

    max_count = max(max_count, current_count)
    return max_count


if __name__ == "__main__":
    main()
