def library_book_analysis(records):
    borrow_data = {}
    for record in records:
        title, days = record.split(" - ")
        days = int(days)
        if title in borrow_data:
            borrow_data[title] += days
        else:
            borrow_data[title] = days

    most_borrowed = max(borrow_data, key=borrow_data.get)
    least_borrowed = min(borrow_data, key=borrow_data.get)

    total_days = sum(borrow_data.values())
    total_books = len(borrow_data)
    average_days = total_days / total_books if total_books > 0 else 0

    unique_titles = set(borrow_data.keys())

    sorted_books = sorted(borrow_data.items(), key=lambda item: item[1], reverse=True)

    print("Most Borrowed Book:", most_borrowed, "with", borrow_data[most_borrowed], "days")
    print("Least Borrowed Book:", least_borrowed, "with", borrow_data[least_borrowed], "days")
    print("Average Days Borrowed:", round(average_days, 2))
    print("Unique Titles:", unique_titles)
    print("Books Sorted by Borrowing Days:", sorted_books)


records = [
    "Book A - 12",
    "Book B - 5",
    "Book C - 7",
    "Book D - 10",
    
]

library_book_analysis(records)
