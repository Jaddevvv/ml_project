import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
import kagglehub

# Download latest version
path = kagglehub.dataset_download("./prathamjyotsingh/microsoft-vs-apple-stock-performance")

print("Path to dataset files:", path)

automl = AutoML(mode='Explain')