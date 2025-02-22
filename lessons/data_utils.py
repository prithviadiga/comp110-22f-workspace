"""Some helpful utility functions for wokring with CSV files."""

from calendar import c
from csv import DictReader


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
    result = dict[str, list[str]] = {}

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