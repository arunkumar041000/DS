from typing import List


def printTable(header: List[str], rows: List[List[str]]) -> str:
    row = " {} |" * (len(header))
    border = ""
    row_format = ""

    for head in header:
        headlen = len(head)
        border += "+" + ("-" * (headlen + 2))
        row_format += "| {:>" + str(headlen) + "} "

    row_format += "|"
    border += "+"
    row = "\n|" + row
    table = border + row.format(*header) + "\n" + border + "\n"
    for row in rows:
        table += row_format.format(*row) + "\n"

    table += border
    return table
