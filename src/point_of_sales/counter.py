from database import database


class BarcodeScanner:
    receipt = dict()  # {'name': [10, 400.2], }
    total_sum = 0

    def point_of_sales(self) -> tuple[dict, float]:
        """
        :return: (receipt, total)
        :rtype: tuple[dict, float]
        """

        while True:
            id = input('Press \'f\' to stop. Enter id: ')
            if id == 'F'.lower():
                for key, value in self.receipt.items():
                    price = value[1]
                    self.total_sum += price

                break

            try:
                response = database.get_item_by_id(int(id))
                # response: [(12, 'Backpack (Nike)', 400.5)]

                item = response[0]
                product_name = item[1]
                product_price = item[2]

                if product_name not in self.receipt:

                    amount = 1
                    total = [amount, product_price]

                    self.receipt[product_name] = total

                elif product_name in self.receipt:
                    # receipt = {'name': [10, 400.2], }

                    item_total = self.receipt[product_name]

                    # updating amount
                    item_total[0] += 1

                    # updating total
                    item_total[1] += product_price

            except Exception:
                print('Incorrect id')

        return self.receipt, self.total_sum
