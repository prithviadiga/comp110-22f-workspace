"""Dictionary related utility functions."""

__author__ = "730480357"

from csv import DictReader

from symbol import return_stmt


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding = "utf8")
   
    # Prepare to read the data file as a csv rather than as just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the csv line by line.
    for row in csv_reader:
        result.append(row)

    # Close that file when you're done to free its resources.
    file_handle.close()
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table"""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    return_table: dict[str, list[str]] = {}
    for key in column_table:
        N_list: list[str] = []
        i: int = 0
        while i < N:
            N_list.append(column_table[key][i])
            i += 1
        return_table[key] = N_list
    return return_table


def select(column_table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    return_table: dict[str, list[str]] = {}
    for key in selected_columns:
        return_table[key] = column_table[key]
    return return_table


def concat(column_table1: dict[str, list[str]], column_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    return_table: dict[str, list[str]] = {}
    for key in column_table1:
        return_table[key] = column_table1[key]
    for key in column_table2:
        return_table[key] = column_table2[key]
    return return_table


def count(raw_values: list[str]) -> dict[str, int]:
    return_dict: dict[str, int]
    for item in raw_values:
        if return_dict[item] != 0:
            return_dict[item] += 1
        else:
            return_dict[item] = 0
    return return_dict