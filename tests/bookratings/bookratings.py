
def max_rating_books(amount, horror_books, scifi_books):
    all_books = horror_books + scifi_books
    all_books = sorted(all_books, key=lambda x: x[0]/x[1], reverse=True)
    total_ratings = 0
    amount_spent = 0
    for v in all_books:
        r, p = v
        if amount_spent + p > amount:
            continue
        amount_spent += p
        total_ratings += r
    return total_ratings if amount_spent > 0 else -1
