if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    print("Rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    print("Rows with 0 trip distance:", data['trip_distance'].isin([0]).sum())

    # cleaned_data = data[(data['passenger_count']!=0) | (data['trip_distance']!=0)]
    print(data.shape)
    cleaned_data = data[data['passenger_count']!=0]
    print(cleaned_data.shape)
    cleaned_data = cleaned_data[cleaned_data['trip_distance']!=0]
    print(cleaned_data.shape)
    cleaned_data['lpep_pickup_date'] = cleaned_data['lpep_pickup_datetime'].dt.date

    final_columns = ['vendor_id' if column == 'VendorID' else column for column in cleaned_data.columns]

    cleaned_data.columns = final_columns

    

    return cleaned_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # assert output is not None, 'The output is undefined'
    assert 'vendor_id' in output.columns, 'The vendor_id column does not exist'
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with a 0 trip distance'