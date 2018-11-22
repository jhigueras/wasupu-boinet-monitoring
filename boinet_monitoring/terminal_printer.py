from terminaltables import AsciiTable


def print_summary(row_data):
    table = AsciiTable([row_data])
    table.outer_border = False
    table.padding_left = 10
    table.padding_right = 2
    print(table.table)


def _prettify_money(amount):
    return "{0:,.0f}".format(amount) + " EUR"
