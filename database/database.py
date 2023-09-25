import sqlite3
import os

# Connect to the database using the constructed path
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'store.db')


connection = sqlite3.connect(db_path)

cursor = connection.cursor()

__all__ = ['get_item_by_name', 'get_item_by_id', 'add_new_item']


def get_item_by_id(id: int) -> list:
    """
    Return: list[tuple]

    Return Example:
            [(12, 'Backpack (Nike)', 400.5)]
    """
    cursor.execute(f"SELECT * FROM Products WHERE id={id}")
    result = cursor.fetchall()
    return result


def get_item_by_name(name: str):
    """
    :param name: str.title()
    """
    cursor.execute(f"SELECT * FROM Products WHERE name='{name}'")
    result = cursor.fetchall()
    return result


def add_new_item(info: list[tuple]):
    """
    :param info
        Example: [(id: int, name: str, price: float)]
                    [(1, 'Coca-cola', 1.25)]

    name: item (brand - optional)
        Backpack (Nike)
        Snickers
    """

    def check_id(local_id: int) -> bool:
        """
        Checks if the record exists in the database.
        :return: True if the record exists, False otherwise
        """
        cursor.execute(f"SELECT * FROM Products WHERE id={local_id}")
        result = cursor.fetchall()

        if not result:
            return True

    def check_name(local_name) -> bool:
        """
        Checks if the product exists in the database.
        :return: False = exists | True = doesn't exist
        """

        cursor.execute(f"SELECT * FROM Products WHERE name='{local_name}'")
        result = cursor.fetchall()

        if not result:
            return True

    id, name = info[0][0], info[0][1].title()
    id_check, name_check = check_id(id), check_name(name)

    if id_check and name_check:  # if record doesn't exist
        cursor.executemany('INSERT INTO Products VALUES(?,?,?)', info)
        connection.commit()
        connection.close()
        return 'Record was done.'

    else:
        if not id_check:
            return 'Operation is declined. Reason: The given id is occupied!'
        elif not name_check:
            return 'Operation is declined. Reason: Product exists!'


if __name__ == '__main__':
    # print(add_new_item([(21, 'Milky Way', 9.2)]))
    print(get_item_by_id(21))
