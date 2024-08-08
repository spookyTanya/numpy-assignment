import numpy as np
import datetime

DEFAULT_TRANSACTION_COUNT = 100


def print_arr(array: np.array, message=None):
    if message:
        print(message)

    print(array)
    print("~~~~~~~~~")


def create_data(rows_num=20) -> np.ndarray:
    data = np.empty((rows_num, 6), dtype=object)

    for i in range(rows_num):
        data[i] = [
            i + 1,  # transaction_id
            np.random.randint(1, 15),  # user_id
            np.random.randint(1, 20),  # product_id
            np.random.randint(0, 10),  # quantity
            np.random.uniform(10.0, 100.0),  # price
            (datetime.datetime.now() - datetime.timedelta(days=i, hours=i)).timestamp()
        ]

    return data


def get_revenue(data: np.ndarray) -> float:
    return np.sum(data[:, 3] * data[:, 4])


def get_unique_users(data: np.ndarray) -> np.ndarray:
    return np.unique(data[:, 1])


def get_most_sold_product_by_quantity(data: np.ndarray) -> (int, int):
    # without grouping by product
    # return data[np.argmax(data[:, 3])][2], data[np.argmax(data[:, 3])][3]

    # with grouping by product
    product_ids = data[:, 2]
    unique_product_ids = np.unique(product_ids)

    total_quantities = {}
    for product_id in unique_product_ids:
        total_quantities[product_id] = np.sum(data[:, 3][product_ids == product_id])

    max_product_id = max(total_quantities, key=total_quantities.get)
    max_quantity = total_quantities[max_product_id]
    return max_product_id, max_quantity


def cast_prices_to_int(data: np.ndarray) -> np.ndarray:
    return np.array(data[:, 4], dtype=int)


def get_products_and_quantities(data: np.ndarray) -> np.ndarray:
    return data[:, 2:4]


def get_transactions_count_by_user(data: np.ndarray) -> np.ndarray:
    user_ids = data[:, 1]
    unique_user_ids = np.unique(user_ids)

    total_transactions_by_user = {}
    for user in unique_user_ids:
        total_transactions_by_user[user] = len(data[data[:, 1] == user])

    total_quantities_arr = np.array(list(total_transactions_by_user.items()))
    return total_quantities_arr


def get_non_zero_quantity_mask(data: np.ndarray) -> bool:
    return data[:, 3] != 0


def increase_prices(data: np.ndarray, percentage=5) -> np.ndarray:
    prices_old = data[:, 4]
    data[:, 4] = prices_old / 100 * percentage + prices_old
    return data


def get_transaction_with_multiple_products(data: np.ndarray) -> np.ndarray:
    return data[data[:, 3] > 1]


def transactions_by_dates(data: np.ndarray, start_date: datetime.datetime, end_date: datetime.datetime) -> np.ndarray:
    start_timestamp = start_date.timestamp()
    end_timestamp = end_date.timestamp()

    mask = (data[:, 5] >= start_timestamp) & (data[:, 5] <= end_timestamp)
    return data[mask]


def revenue_by_dates(data: np.ndarray, start_date: datetime.datetime, end_date: datetime.datetime) -> float:
    filtered_data = transactions_by_dates(data, start_date, end_date)

    return get_revenue(filtered_data)


def compare_revenue(data: np.ndarray, start_date1: datetime.datetime, end_date1: datetime.datetime,
                    start_date2: datetime.datetime, end_date2: datetime.datetime):
    revenue_period1 = revenue_by_dates(data, start_date1, end_date1)
    revenue_period2 = revenue_by_dates(data, start_date2, end_date2)

    print(f"Revenue for period {start_date1} - {end_date1} = {revenue_period1}")
    print(f"Revenue for period {start_date2} - {end_date2} = {revenue_period2}")
    print("Revenue difference: ", revenue_period2 - revenue_period1)
    assert type(revenue_period1) is float, "Revenue must be float"
    assert type(revenue_period2) is float, "Revenue must be float"


def get_transactions_by_user(data: np.ndarray, user_id: int) -> np.ndarray:
    return data[data[:, 1] == user_id]


def get_top_products(data: np.ndarray) -> np.ndarray:
    unique_product_ids = np.unique(data[:, 2])

    revenues = np.zeros(unique_product_ids.size)
    for i, product_id in enumerate(unique_product_ids):
        filtered = data[data[:, 2] == product_id]
        revenues[i] = get_revenue(filtered)

    indices = np.argsort(revenues)[::-1][:5]
    return unique_product_ids[indices]


def get_transactions_by_products(data: np.ndarray, product_ids: np.ndarray) -> np.ndarray:
    mask = np.isin(data[:, 2], product_ids)
    return data[mask]


# Start
transactions = create_data(DEFAULT_TRANSACTION_COUNT)
print_arr(transactions, "Initial transactions:")
assert transactions.shape == (DEFAULT_TRANSACTION_COUNT, 6), "Should have correct shape"

# 2
total_revenue = get_revenue(transactions)
print("Total revenue =", total_revenue)
assert type(total_revenue) is float, "Total revenue should be float"


# unique users who made transactions
unique_users = get_unique_users(transactions)
print_arr(unique_users, "Unique users:")
assert type(unique_users) is np.ndarray, "Unique users should be an array"


most_sold_product_by_quantity, total_quantity = get_most_sold_product_by_quantity(transactions)
print(f"Most sold product based on total quantity:\nid = {most_sold_product_by_quantity}, quantity = {total_quantity}")
assert type(most_sold_product_by_quantity) is int, "Product id must be int"


prices = cast_prices_to_int(transactions)
print_arr(prices, "Prices casted to integers")
print(type(prices[0]))
all_integers = all([isinstance(x, np.integer) for x in prices])
assert all_integers is True, "Prices should have int type"

# 3
products_and_quantities = get_products_and_quantities(transactions)
print_arr(products_and_quantities, "Products and quantities")
assert products_and_quantities.shape == (DEFAULT_TRANSACTION_COUNT, 2), "Should have all rows and 2 columns"

count_by_user = get_transactions_count_by_user(transactions)
print_arr(count_by_user, "Transactions count by user")
assert count_by_user.shape[1] == 2, "Each row must have user_id and quantity"
assert max(count_by_user[:, 0]) == 14, "User id can't be greater than 14 (defined in creation func)"

non_zero_mask = get_non_zero_quantity_mask(transactions)
non_zero_transactions = transactions[non_zero_mask]
print_arr(non_zero_transactions, "Transactions without zero quantities")
all_non_zero = all([i[3] != 0 for i in non_zero_transactions])
assert all_non_zero, "All quantities must be greater than 0"
assert non_zero_transactions.shape[1] == 6, "Should have correct shape"

# 4
copy = np.copy(transactions)
copy = increase_prices(copy, 10)
print_arr(copy, "Transactions after price increase")
assert not np.array_equal(copy, transactions), "Prices should be updated"

multiple_products = get_transaction_with_multiple_products(transactions)
print_arr(multiple_products, "Transactions with quantity > 1")
assert multiple_products.shape[1] == 6, "Should have correct shape"


start_date1 = datetime.datetime(2024, 7, 1)
end_date1 = datetime.datetime(2024, 7, 15)
start_date2 = datetime.datetime(2024, 7, 16)
end_date2 = datetime.datetime(2024, 7, 31)
compare_revenue(transactions, start_date1, end_date1, start_date2, end_date2)

# 5
user_transactions = get_transactions_by_user(transactions, 2)
print_arr(user_transactions, "Transaction made by user with id 2")
assert user_transactions.shape[1] == 6, "Should have correct shape"


start_date3 = datetime.datetime(2024, 7, 15)
end_date3 = datetime.datetime(2024, 8, 7)
transaction_for_period = transactions_by_dates(transactions, start_date3, end_date3)
print_arr(transaction_for_period, f"Transactions for period {start_date3} - {end_date3}")
assert transaction_for_period.shape[1] == 6, "Should have correct shape"


top_products = get_top_products(transactions)
print_arr(top_products, "Top 5 products")
top_products_transactions = get_transactions_by_products(transactions, top_products)
print_arr(top_products_transactions, "Transactions with top 5 products")
assert top_products_transactions.shape[0] >= 5, "Should be at least 5 transactions"
assert top_products_transactions.shape[1] == 6, "Should have correct shape"
assert top_products_transactions[0, 2] in top_products, "Product id must be in top 5 products"
