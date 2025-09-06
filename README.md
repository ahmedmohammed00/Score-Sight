# Student Reading Score Prediction API

A machine learning API for predicting student reading scores based on various features, following the exact pattern from your data cleaning notebook.

## Project Structure

```
score-api/
├── server/
│   ├── app/
│   │   ├── model.py              # Main model training logic (scikit-learn)
│   │   ├── api.py                # FastAPI web service
│   │   └── column_mappings.py    # Categorical feature mappings (from notebook)
│   ├── data/
│   │   └── Expanded_data_with_more_features.csv  # Training data
│   ├── models/                   # Trained models will be saved here
│   ├── main.py                   # Entry point to run model training
│   ├── run_api.py                # Entry point to run the API server
│   └── test_api.py               # Test script for the API
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Navigate to Server Directory

```bash
cd server
```

### 3. Train the Model (Required First Time)

```bash
python main.py
```

### 4. Start the API Server

```bash
python run_api.py
```

### 5. Test the API

```bash
python test_api.py
```

## What the Project Does

- **Data Processing**: Encodes categorical features using the exact mappings from your notebook
- **Data Cleaning**: Implements comprehensive data cleaning following your notebook pattern:
  - **Missing Value Handling**: Fills missing values using mode (categorical) and median (numerical)
  - **Outlier Removal**: Removes outliers from ReadingScore using IQR method (1.5 × IQR rule)
  - **Data Quality**: Ensures clean, reliable data for training
- **Model Training**: Trains a Linear Regression model using scikit-learn to predict reading scores
- **Feature Engineering**: Handles various student characteristics like:
  - Demographics (gender, ethnicity)
  - Family background (parent education, marital status)
  - Academic factors (test preparation, study hours)
  - Lifestyle factors (sports practice, transport)
- **Web API**: Provides RESTful endpoints for making predictions
- **Real-time Scoring**: Accepts student data and returns predicted reading scores

## API Endpoints

- **GET /** - API information and available endpoints
- **GET /health** - Health check and model status
- **GET /model-info** - Model performance and feature information
- **POST /predict** - Predict reading score for a student

## Expected Output

When you run the training, you should see:
```
🚀 Starting Student Reading Score Model Training...
📖 Loading student performance data...
✅ Loaded 30,641 records with 15 columns
🧹 Cleaning data - Handling missing values...
🧹 Missing values after cleaning: [0, 0, 0, ...]
📊 Removing outliers from ReadingScore using IQR method...
🚨 Found X outliers in ReadingScore
📊 ReadingScore bounds: XX.XX to XX.XX
🧹 Data after outlier removal: XX,XXX records (removed X outliers)
🧹 Final clean training data: XX,XXX samples
✅ Model trained and saved to models/reading_score_model.pkl
```

When you start the API server, you should see:
```
🚀 Starting Student Reading Score Prediction API...
📖 Interactive API Documentation: http://localhost:8000/docs
🔗 Health Check: http://localhost:8000/health
🎯 Make Predictions: http://localhost:8000/predict
```

The trained model will be saved as `models/reading_score_model.pkl`.

## Troubleshooting

- Make sure you have Python 3.7+ installed
- Ensure all dependencies are installed with `pip install -r requirements.txt`
- Check that the data file exists in `server/data/`
- Run from the `server` directory, not the root directory

