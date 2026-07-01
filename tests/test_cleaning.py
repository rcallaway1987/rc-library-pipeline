# Cleaning tests

import pytest
import pandas as pd
import pandas.testing as pdt
from data_processing.cleaning import (
    remove_duplicates,
    handle_missing_values,
    standardize_dates
)

@pytest.fixture
def sample_with_duplicates():
    return pd.DataFrame({
        'id': [1, 2, 2, 3],
        'name': ['Alice', 'Bob', 'Bob', 'Charlie']
    })

@pytest.fixture
def sample_with_missing():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', None, 'Charlie'],
        'value': [10, None, 30]
    })

def test_remove_duplicates_reduces_rows(sample_with_duplicates):
    result = remove_duplicates(sample_with_duplicates, subset=['id'])
    assert len(result) == 3

def test_remove_duplicates_ids_are_unique(sample_with_duplicates):
    result = remove_duplicates(sample_with_duplicates, subset=['id'])
    assert result ['id'] .is_unique

def test_handle_missing_drop(sample_with_missing):
    result = handle_missing_values(sample_with_missing, strategy='drop')
    assert not result.isnull().any().any()
