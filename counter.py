import database

receipt = dict()  # {'name': [10, 400.2], }
total_sum = 0

while True:
    id = input('Enter id: ')
    if id == 'F'.lower():
        for key, value in receipt.items():
            price = value[1]
            total_sum += price

        break

    try:
        response = database.get_item_by_id(int(id))
        # response: [(12, 'Backpack (Nike)', 400.5)]

        item = response[0]
        product_name = item[1]
        product_price = item[2]

        if product_name not in receipt:

            amount = 1
            total = [amount, product_price]

            receipt[product_name] = total

        elif product_name in receipt:
            # receipt = {'name': [10, 400.2], }

            item_total = receipt[product_name]

            # updating amount
            item_total[0] += 1

            # updating total
            item_total[1] += product_price

    except Exception:
        print('Incorrect id')

print(receipt)
print('\n')

for key, value in receipt.items():
    print(f"{key} : Amount: {value[0]}, Sum: {value[1]}")

print('Total: ', total_sum)

