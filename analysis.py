import pandas as pd
import numpy as np
from supervised.automl import AutoML
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, classification_report

def prepare_data(price_file, dividend_file, split_file):
    # Read the CSV files
    price_data = pd.read_csv(price_file)
    dividend_data = pd.read_csv(dividend_file)
    split_data = pd.read_csv(split_file)
    
    # Convert dates properly
    try:
        price_data['Date'] = pd.to_datetime(price_data['Date'], utc=True).dt.tz_localize(None)
        dividend_data['Date'] = pd.to_datetime(dividend_data['Date'], utc=True).dt.tz_localize(None)
        split_data['Date'] = pd.to_datetime(split_data['Date'], utc=True).dt.tz_localize(None)
    except Exception as e:
        print(f"Error converting dates: {e}")
        print("Input date format samples:")
        print(f"Price data: {price_data['Date'].iloc[0]}")
        print(f"Dividend data: {dividend_data['Date'].iloc[0]}")
        print(f"Split data: {split_data['Date'].iloc[0]}")
        raise
    
    # Merge dataframes
    data = pd.merge(price_data, dividend_data[['Date', 'Dividend']], on='Date', how='left')
    
    # Ensure 'Date' in 'data' is datetime64[ns] after the first merge
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.tz_localize(None)
    
    data = pd.merge(data, split_data[['Date', 'Stock Splits']], on='Date', how='left')
    
    # Fill missing values
    data['Dividend'] = data['Dividend'].fillna(0)
    data['Stock Splits'] = data['Stock Splits'].fillna(0)
    
    # Sort by date
    data = data.sort_values('Date').reset_index(drop=True)
    
    # Create target variables
    data['Next Close Price'] = data['Close Price'].shift(-1)
    data['Target'] = (data['Next Close Price'] > data['Close Price']).astype(int)
    
    # Create lag features
    data['Prev Close Price'] = data['Close Price'].shift(1)
    data['Prev Volume'] = data['Volume'].shift(1)
    
    # Create moving averages
    data['MA5'] = data['Close Price'].rolling(window=5).mean()
    data['MA10'] = data['Close Price'].rolling(window=10).mean()
    data['MA20'] = data['Close Price'].rolling(window=20).mean()
    
    # Drop rows with NaN values
    data = data.dropna().reset_index(drop=True)
    
    return data

def perform_ml_analysis(stock_name, data):
    # Define features and targets
    features = ['Open Price', 'High Price', 'Low Price', 'Close Price', 'Volume', 'Dividend', 'Stock Splits',
                'MA5', 'MA10', 'MA20', 'Prev Close Price', 'Prev Volume']
    X = data[features]
    y_reg = data['Next Close Price']
    y_class = data['Target']
    
    # Split data into training and testing sets
    train_size = int(len(data) * 0.8)
    X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
    y_train_reg, y_test_reg = y_reg.iloc[:train_size], y_reg.iloc[train_size:]
    y_train_class, y_test_class = y_class.iloc[:train_size], y_class.iloc[train_size:]
    
    print(f"\nStarting ML analysis for {stock_name}...\n")
    
    # Regression Analysis
    automl_reg = AutoML(mode='Perform', ml_task='regression')
    automl_reg.fit(X_train, y_train_reg)
    predictions_reg = automl_reg.predict(X_test)
    
    # Evaluate regression model
    mae = mean_absolute_error(y_test_reg, predictions_reg)
    mse = mean_squared_error(y_test_reg, predictions_reg)
    rmse = np.sqrt(mse)
    
    print(f"Regression Model Performance for {stock_name}:")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}\n")
    
    # Classification Analysis
    automl_class = AutoML(mode='Perform', ml_task='binary_classification')
    automl_class.fit(X_train, y_train_class)
    predictions_class = automl_class.predict(X_test)
    
    # Evaluate classification model
    accuracy = accuracy_score(y_test_class, predictions_class)
    print(f"Classification Model Performance for {stock_name}:")
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test_class, predictions_class))

# Prepare data for AAPL
aapl_data = prepare_data('data/AAPL_stock_price.csv', 'data/AAPL_stock_dividend.csv', 'data/AAPL_stock_split.csv')
perform_ml_analysis('AAPL', aapl_data)

# Prepare data for MSFT
msft_data = prepare_data('data/MSFT_stock_price.csv', 'data/MSFT_stock_dividend.csv', 'data/MSFT_stock_split.csv')
perform_ml_analysis('MSFT', msft_data)
