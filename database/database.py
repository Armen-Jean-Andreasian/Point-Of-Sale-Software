"""
Database Module

This module provides functions to interact with a SQLite database containing product information.

Functions:
- `get_item_by_id(id: int) -> list`: Retrieves product information by ID.
- `get_item_by_name(name: str)`: Retrieves product information by name.
- `add_new_item(info: list[tuple])`: Adds a new product to the database.
- `get_all_items() -> list`: Retrieves a list of all products in the database.

Usage:
- Import this module to access the database functions.
- Use the functions to retrieve, add_product, or query product information in the database.

Example:
if __name__ == '__main__':
    test()
"""


import sqlite3
import os

__all__ = ['get_item_by_name', 'get_item_by_id', 'add_new_item', 'get_all_items']


def connect():
    # Connect to the database using the constructed path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'store.db')

    connection = sqlite3.connect(db_path)

    return connection


def get_item_by_id(id: int) -> list:
    """
    Retrieves product information by ID.

    :param id: The ID of the product to retrieve.
    :return: A list of tuples containing product information.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Products WHERE id={id}")
    result = cursor.fetchall()
    connection.close()
    return result


def get_item_by_name(name: str):
    """
    Retrieves product information by name.

    :param name: The name of the product to retrieve.
    :return: A list of tuples containing product information.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Products WHERE name='{name}'")
    result = cursor.fetchall()
    connection.close()
    return result


def add_new_item(info: list[tuple]):
    """
    Adds a new product to the database.

    :param info: A list containing tuples with product information to be added.
        Example: [(id: int, name: str, price: float)]

            name : item (brand if any)
                Backpack (Nike)
                Snickers
    :return: A string indicating the result of the operation.
    """

    def check_id(local_id: int) -> bool:
        """
        Checks if the record exists in the database.

        :return: True if the record exists, False otherwise.
        """
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Products WHERE id={local_id}")
        result = cursor.fetchall()
        connection.close()

        if not result:
            return True

    def check_name(local_name) -> bool:
        """
        Checks if the product exists in the database.

        :return: False if the product exists, True otherwise.
        """
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Products WHERE name='{local_name}'")
        result = cursor.fetchall()
        connection.close()
        if not result:
            return True

    id, name = info[0][0], info[0][1].title()
    id_check, name_check = check_id(id), check_name(name)

    outer_connection = connect()
    outer_cursor = outer_connection.cursor()

    if id_check and name_check:  # if record doesn't exist
        outer_cursor.executemany('INSERT INTO Products VALUES(?,?,?)', info)
        outer_connection.commit()
        outer_connection.close()
        return 'Record was done.'

    else:
        if not id_check:
            return 'Operation is declined. Reason: The given id is occupied!'
        elif not name_check:
            return 'Operation is declined. Reason: Product exists!'


def get_all_items() -> list[tuple]:
    """
    Retrieves a list of all products in the database.

    :return: A list of tuples containing product information.
        Example:
            [(12, 'Backpack (Nike)', 400.5)]
    """
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM Products ORDER BY ID")
    result = cursor.fetchall()
    connection.close()
    return result


def test():
    print(get_item_by_id(21))
    print(get_item_by_name('Milky Way'))
    print(add_new_item([(32, 'Colgate', 14.2)]))
    print(get_all_items())


if __name__ == '__main__':
    test()
