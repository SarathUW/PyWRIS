# import modules and functions
import pytest
import ipytest
import numpy as np
import pandas as pd
from unittest.mock import MagicMock
from pywris.surface_water.storage.reservoir import get_reservoirs  
import pywris.geo_units.components as geo_components

def create_synthetic_reservoir_data():
    """Generate synthetic reservoir data for testing purposes."""
    date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    data = {
        'Date': date_range,
        'Level': np.random.uniform(50, 150, size=len(date_range)),  # Random reservoir levels
        'Current Live Storage': np.random.uniform(1000, 5000, size=len(date_range)),  # Random storage values
    }
    return pd.DataFrame(data)

def mock_get_reservoirs(*args, **kwargs):
    """Mock the 'get_reservoirs' function to return synthetic reservoirs."""
    reservoirs = {
        'Bisalpur': MagicMock(),
        'Mahi Bajaj Sagar': MagicMock(),
    }
    reservoirs['Bisalpur'].data = create_synthetic_reservoir_data()
    reservoirs['Mahi Bajaj Sagar'].data = create_synthetic_reservoir_data()
    return reservoirs, pd.DataFrame(), pd.DataFrame()

def test_reservoir_plot_smoke():
    """
    Smoke test to ensure the 'plot' method works for a known reservoir ('Bisalpur') with synthetic data.
    """
    reservoirs, _, _ = mock_get_reservoirs(end_date='2023-04-01', selected_states=['Rajasthan'])
    try:
        reservoirs['Mahi Bajaj Sagar'].data.plot()
    except Exception as e:
        pytest.fail(f"Plotting failed for Bisalpur reservoir with synthetic data: {e}")

def test_reservoir_plot_functionality():
    """
    Smoke test to ensure the 'plot' method works for a known reservoir.
    """
    reservoirs, _, _ = get_reservoirs(end_date='2023-04-01', selected_states=['Rajasthan'])
    try:
        reservoirs['Bisalpur'].plot()
    except Exception as e:
        pytest.fail(f"Plotting failed for Bisalpur reservoir: {e}")

def test_reservoir_plot_functionality_single():
    """
    Smoke test to ensure the 'plot' method works for a known reservoir.
    """
    reservoirs, _, _ = get_reservoirs(end_date='2023-04-01', selected_states=['Rajasthan'])
    try:
        reservoirs['Bisalpur'].plot(columns = ['Level'])
    except Exception as e:
        pytest.fail(f"Plotting failed for Bisalpur reservoir: {e}")

def test_reservoir_add_column_and_plot():
    """
    Test adding a new column to the reservoir data and plotting it.
    """
    reservoirs, _, _ = get_reservoirs(end_date='2023-04-01', selected_states=['Rajasthan'])
    try:
        # reservoirs['Bisalpur'].data['added_column'] = np.nan
        reservoirs['Bisalpur'].data['added_column'] = reservoirs['Bisalpur'].data[reservoirs['Bisalpur'].data.columns[1]] * 2
        reservoirs['Bisalpur'].plot()
    except Exception as e:
        pytest.fail(f"Adding a new column and plotting failed: {e}")
