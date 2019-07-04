import csv
import os

def main():

    authors = []
    authors_set = []

    # Open books.csv in read mode
    f = open("books.csv")
    reader = csv.reader(f)

    # Open authors.csv in append mode
    file = open("authors.csv", "a")
    writer = csv.DictWriter(file, fieldnames=["author_id", "author_name"])

    # Get authors in a list
    for isbn, title, author, year in reader:
        authors.append(author)

    # Make a set of unique authors
    tmp = set()
    for i in authors:
        tmp.add(i)

    # Make a list from set
    for author in tmp:
        authors_set.append(author)

    # Write author set in csv file
    count = 0
    for author in authors_set:
        writer.writerow({ "author_id" : count, "author_name" : author })
        count += 1

if __name__ == "__main__":
    main()
