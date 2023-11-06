import streamlit as st

from tab_df.logics import Dataset

def display_tab_df_content(file_path):

    dataset = Dataset(file_path)

    dataset.set_data()


    st.sidebar.title("Data Exploration Options")


    num_rows = st.sidebar.slider("Number of Rows to Display", min_value=1, max_value=dataset.n_rows, value=5)


    display_method = st.sidebar.radio("Display Method", ["Head", "Tail", "Sample"])


    if display_method == "Head":
        st.dataframe(dataset.get_head(num_rows))
    elif display_method == "Tail":
        st.dataframe(dataset.get_tail(num_rows))
    elif display_method == "Sample":
        st.dataframe(dataset.get_sample(num_rows))


    st.title("Dataframe")
    st.table(dataset.get_summary())


    st.title("Columns")
    dataset.set_table()

if __name__ == "__main__":
    st.title("Data Exploration App")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        display_tab_df_content(uploaded_file)
    """
    --------------------
    Description
    --------------------
    -> display_overall_df (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file

    --------------------
    Returns
    --------------------
    -> None
    
    """
