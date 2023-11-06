import pandas as pd


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (mandatory)
    -> df (pd.Dataframe): Pandas dataframe (default set to None)
    -> cols_list (list): List of columns names of dataset (default set to empty list)
    -> n_rows (int): Number of rows of dataset (default set to 0)
    -> n_cols (int): Number of columns of dataset (default set to 0)
    -> n_duplicates (int): Number of duplicated rows of dataset (default set to 0)
    -> n_missing (int): Number of missing values of dataset (default set to 0)
    -> n_num_cols (int): Number of columns that are numeric type (default set to 0)
    -> n_text_cols (int): Number of columns that are text type (default set to 0)
    -> table (pd.Series): Pandas DataFrame containing the list of columns, their data types and memory usage from dataframe (default set to None)
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cols_list = []
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.n_num_cols = 0
        self.n_text_cols = 0
        self.table = None

    def set_data(self):
        self.df = pd.read_csv(self.file_path)
        self.n_rows,self.n_cols = self.df.shape
        
    

        self.n_duplicates = len(self.df[self.df.duplicated()])

        self.n_missing = self.df.isnull().sum().sum()
    
        return None

        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Dataframe tab of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        
        
    def set_df(self):
        if self.df is None:
            try:

                self.df = pd.read_csv(self.file_path)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
            else:
                print("DataFrame already provided.")
        """
        --------------------
        Description
        --------------------
        -> set_df (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def is_df_none(self):

        if self.df is None:
            return True
        return self.df.empty

        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if self.df is empty or not

        """
        

    def set_columns(self):
        if self.is_df_none() is not True:
            self.cols_list = list(self.df.columns)
        return None
        """
        --------------------
        Description
        --------------------
        -> set_columns (method): Class method that extract the list of columns names and store the results in the relevant attribute (self.cols_list) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_dimensions(self):
        if self.is_df_none() is not True:


            self.n_rows, self.n_cols = self.df.shape
        return None
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df  and store the results in the relevant attributes (self.n_rows, self.n_cols) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_duplicates(self):
        if self.is_df_none() is not True:


            self.n_duplicates = len(self.df[self.df.duplicated()])
        return None

        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store the results in the relevant attribute (self.n_duplicates) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_missing(self):
        if self.is_df_none() is not True:


            self.n_missing = self.df.isnull().sum().sum()
        return None
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store the results in the relevant attribute (self.n_missing) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_numeric(self):
        if self.is_df_none() is not True:
            numeric_cols = self.df.select_dtypes(include=['number'])
            self.n_num_cols = numeric_cols.shape[1]

            
        return None
        """
        --------------------
        Description
        --------------------
        -> set_numeric (method): Class method that computes the number of columns that are numeric type and store the results in the relevant attribute (self.n_num_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def set_text(self):
        if self.is_df_none() is not True:
            numeric_cols = self.df.select_dtypes(exclude=['number'])
            self.n_num_cols = numeric_cols.shape[1]

            
        return None
        """
        --------------------
        Description
        --------------------
        -> set_text (method): Class method that computes the number of columns that are text type and store the results in the relevant attribute (self.n_text_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        

    def get_head(self, n=5):
        if self.is_df_none() is not True:
            return self.df.head(n)

            
        return None
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): First rows of dataframe

        """
        

    def get_tail(self, n=5):
        if self.is_df_none() is not True:
            return self.df.tail(n)

            
        return None
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Last rows of dataframe

        """
        

    def get_sample(self, n=5):
        if self.is_df_none() is not True:
            return self.df.sample(n)

            
        return None
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Sampled dataframe

        """
        


    def set_table(self):
        if self.is_df_none() is not True:
            data = []
            for col in self.cols_list:
                data_type = str(self.df[col].dtype)
                memory = self.df[col].memory_usage(deep=True)
                data.append({"Description": col, "data_type": data_type, "memory": memory})

            return pd.DataFrame(data)
        return pd.DataFrame(columns=["Description", "data_type", "memory"])

            
 

        """
        --------------------
        Description
        --------------------
        -> set_table (method): Class method that computes the Dataframe containing the list of columns with their data types and memory usage and store the results in the relevant attribute (self.table) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """


    def get_summary(self):
        if self.is_df_none() is not True:
            summary_data = [
            {"Description": "Number of Rows", "Value": self.n_rows},
            {"Description": "Number of Columns", "Value": self.n_cols},
            {"Description": "Number of Duplicated Rows", "Value": self.n_duplicates},
            {"Description": "Number of Rows with Missing Values", "Value": self.n_missing}
        ]

            return pd.DataFrame(summary_data)
        return pd.DataFrame(columns=["Description", "Value"])
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Dataframe tab of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
