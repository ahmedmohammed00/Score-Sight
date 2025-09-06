import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

from column_mappings import *


def encode(df):
    """Encode categorical features to numerical values"""
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)
    # Create a copy to avoid modifying the original dataframe
    df_encoded = df.copy()
    if "Unnamed: 0" in df_encoded.columns:
        df_encoded.drop(columns=["Unnamed: 0"], inplace=True)
    
    # Apply mappings to categorical columns
    df_encoded['Gender'] = df_encoded['Gender'].map(gender_map)
    df_encoded['EthnicGroup'] = df_encoded['EthnicGroup'].map(ethnicity_map)
    df_encoded['ParentEduc'] = df_encoded['ParentEduc'].map(education_map)
    df_encoded['LunchType'] = df_encoded['LunchType'].map(lunch_map)
    df_encoded['TestPrep'] = df_encoded['TestPrep'].map(prep_map)
    df_encoded['ParentMaritalStatus'] = df_encoded['ParentMaritalStatus'].map(marital_map)
    df_encoded['PracticeSport'] = df_encoded['PracticeSport'].map(sport_map)
    df_encoded['IsFirstChild'] = df_encoded['IsFirstChild'].map(first_child_map)
    df_encoded['TransportMeans'] = df_encoded['TransportMeans'].map(transport_map)
    df_encoded['WklyStudyHours'] = df_encoded['WklyStudyHours'].map(study_map)
    
    # Handle NaN values by filling with -1 (indicating missing data)
    df_encoded = df_encoded.fillna(-1)
    
    return df_encoded



def train_model():
    """Train a linear regression model using scikit-learn"""
    print("📖 Loading student performance data...")
    
    # Load the data
    df = pd.read_csv('data/Expanded_data_with_more_features.csv')
    print(f"✅ Loaded {len(df):,} records with {len(df.columns)} columns")
    
    # Display column information
    print(f"📊 Available columns: {df.columns.tolist()}")
    
    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"🔍 Missing values per column:\n{missing_values}")
    
    # Data cleaning - Handle missing values (following your notebook pattern)
    print("🧹 Cleaning data - Handling missing values...")
    df["EthnicGroup"].fillna(df["EthnicGroup"].mode()[0], inplace=True)
    df["ParentEduc"].fillna(df["ParentEduc"].mode()[0], inplace=True)
    df["TestPrep"].fillna(df["TestPrep"].mode()[0], inplace=True)
    df["ParentMaritalStatus"].fillna(df["ParentMaritalStatus"].mode()[0], inplace=True)
    df["PracticeSport"].fillna(df["PracticeSport"].mode()[0], inplace=True)
    df["WklyStudyHours"].fillna(df["WklyStudyHours"].mode()[0], inplace=True)
    df["NrSiblings"].fillna(df["NrSiblings"].median(), inplace=True)
    df["IsFirstChild"].fillna(df["IsFirstChild"].mode()[0], inplace=True)
    df["TransportMeans"].fillna(df["TransportMeans"].mode()[0], inplace=True)
    
    # Check missing values after cleaning
    missing_after = df.isnull().sum()
    print(f"🧹 Missing values after cleaning:\n{missing_after}")
    
    # Data cleaning - Remove outliers from ReadingScore using IQR method (following your notebook pattern)
    print("📊 Removing outliers from ReadingScore using IQR method...")
    Q1_Value = df["ReadingScore"].quantile(0.25)
    Q3_Value = df["ReadingScore"].quantile(0.75)
    IQR_Value = Q3_Value - Q1_Value
    
    # Define outlier bounds
    Lower_Bound = Q1_Value - (1.5 * IQR_Value)
    Upper_Bound = Q3_Value + (1.5 * IQR_Value)
    
    # Identify outliers
    Out_Liers = df[(df["ReadingScore"] < Lower_Bound) | (df["ReadingScore"] > Upper_Bound)]
    print(f"🚨 Found {len(Out_Liers)} outliers in ReadingScore")
    print(f"📊 ReadingScore bounds: {Lower_Bound:.2f} to {Upper_Bound:.2f}")
    
    # Remove outliers from the DataFrame
    df_clean = df[~((df["ReadingScore"] < Lower_Bound) | (df["ReadingScore"] > Upper_Bound))]
    print(f"🧹 Data after outlier removal: {len(df_clean):,} records (removed {len(df) - len(df_clean):,} outliers)")
    
    # Prepare features and target (following your notebook pattern)
    print("🔧 Preparing features and target...")
    
    # Drop all score columns and use ReadingScore as target
    X = df_clean.drop(columns=['WritingScore', 'ReadingScore', 'MathScore'])
    y = df_clean['ReadingScore']
    
    print(f"📈 Features shape: {X.shape}")
    print(f"🎯 Target shape: {y.shape}")
    print(f"✅ Features used: {X.columns.tolist()}")
    
    # Encode categorical features
    print("🔤 Encoding categorical features...")
    X_encoded = encode(X)
    
    # Convert to numpy arrays
    X_array = X_encoded.values.astype(float)
    y_array = y.values.astype(float)
    
    # Additional safety check for any remaining NaN values
    valid_indices = ~np.isnan(X_array).any(axis=1) & ~np.isnan(y_array)
    X_final = X_array[valid_indices]
    y_final = y_array[valid_indices]
    
    print(f"🧹 Final clean training data: {X_final.shape[0]:,} samples")
    
    # Split data using scikit-learn (following your notebook pattern)
    print("📚 Splitting data into training and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_final, y_final, test_size=0.2, random_state=42, shuffle=True
    )
    
    print(f"📚 Training set: {X_train.shape[0]:,} samples")
    print(f"🧪 Test set: {X_test.shape[0]:,} samples")
    
    # Train the model using scikit-learn (following your notebook pattern)
    print("🚀 Training linear regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Calculate metrics (following your notebook pattern)
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    mse = mean_squared_error(y_test, y_pred_test)
    mae = mean_absolute_error(y_test, y_pred_test)
    
    print(f"📊 Training Score (R²): {train_score:.6f}")
    print(f"📊 Testing Score (R²): {test_score:.6f}")
    print(f"📊 Mean Squared Error: {mse:.6f}")
    print(f"📊 Mean Absolute Error: {mae:.6f}")
    
    # Save the model
    model_data = {
        'model': model,
        'feature_names': X.columns.tolist(),
        'train_score': train_score,
        'test_score': test_score,
        'mse': mse,
        'mae': mae,
        'model_type': 'Linear Regression (scikit-learn)',
        'training_samples': len(X_train),
        'test_samples': len(X_test),
        'data_cleaning_info': {
            'original_samples': len(df),
            'samples_after_outlier_removal': len(df_clean),
            'final_training_samples': len(X_final),
            'outliers_removed': len(df) - len(df_clean),
            'reading_score_bounds': {
                'lower_bound': float(Lower_Bound),
                'upper_bound': float(Upper_Bound),
                'q1': float(Q1_Value),
                'q3': float(Q3_Value),
                'iqr': float(IQR_Value)
            }
        }
    }
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    with open('models/reading_score_model.pkl', 'wb') as f:
        pickle.dump(model_data, f)
    
    print("✅ Model trained and saved to models/reading_score_model.pkl")
    print(f"📝 Model uses {len(X.columns)} features")
    print(f"🎯 Model performance: R² = {test_score:.6f}, MSE = {mse:.6f}")
    
    return model_data

if __name__ == "__main__":
    train_model()
