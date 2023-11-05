import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    num_col = NumericColumn(file_path, df)
    num_col.find_num_cols()
    selected_column = st.selectbox("Select a numeric column", num_col.cols_list)
    if selected_column:
        num_col.set_data(selected_column)
        num_col.set_unique()
        num_col.set_missing()
        num_col.set_zeros()
        num_col.set_negatives()
        num_col.set_mean()
        num_col.set_std()
        num_col.set_min()
        num_col.set_max()
        num_col.set_median()
        num_col.set_histogram()
        num_col.set_frequent()
        st.write("### Numeric Column Summary")
        st.table(num_col.get_summary())
        st.write("### Histogram")
        st.altair_chart(num_col.histogram)
        st.write("### Most Frequent Values")
        st.write(num_col.frequent)
if __name__ == "__main__":
    display_tab_num_content()




    