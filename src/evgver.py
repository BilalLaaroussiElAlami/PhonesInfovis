from bokeh.io import output_notebook, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, DataTable, TableColumn

def create_dynamic_height_data_table(n_rows):
    # Create a sample data source with n_rows
    data = {'index': list(range(n_rows))}
    source = ColumnDataSource(data=data)

    # Define columns for the DataTable
    columns = [
        TableColumn(field='index', title='Index')
    ]

    # Calculate the height based on the number of rows
    row_height = 25  # Adjust this value as needed
    table_height = n_rows * row_height

    # Create the DataTable
    data_table = DataTable(source=source, columns=columns, height=table_height)

    return data_table

# Example usage
n_rows = 10  # You can change this value as needed
dynamic_height_table = create_dynamic_height_data_table(n_rows)
dynamic_height_table2 = create_dynamic_height_data_table(n_rows)

# Show the DataTable in a Bokeh layout
layout = column(dynamic_height_table, dynamic_height_table2)
show(layout)
