from utils import read_data
def test_read():
    assert (read_data() == True)
    df = pd.read_excel("2010 Federal STEM Education Inventory Data Set.xls", skiprows = 1)
    df = df.select_dtypes(exclude = ['object'])
    assert (check_numeric_data(df) == True)
    assert (check_shape(df.drop('target', axis = 1), df['target']) == True)
    assert (train_data(df.dropna()) == True)

