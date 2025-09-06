from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import pickle
import os
import numpy as np
import pandas as pd
from model import *
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Score API",
    description="API for predicting student reading scores",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model


def load_model():
    """Load the trained model from disk"""
    model_path = r'D:\score-api\server\models\reading_score_model.pkl'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}. Please train the model first.")
    
    with open(model_path, 'rb') as f:
        model_data = pickle.load(f)
    
    return model_data


# Input data model for the API
class StudentData(BaseModel):
    gender: str
    ethnic_group: Optional[str] = None
    parent_educ: Optional[str] = None
    lunch_type: str
    test_prep: Optional[str] = None
    parent_marital_status: Optional[str] = None
    practice_sport: Optional[str] = None
    is_first_child: Optional[str] = None
    nr_siblings: Optional[float] = None
    transport_means: Optional[str] = None
    wkly_study_hours: Optional[str] = None
    math_score: float
    writing_score: float

# Response model
class PredictionResponse(BaseModel):
    predicted_reading_score: float
    confidence: str
    features_used: List[str]

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
                    "message": "Score API - Student Reading Score Predictor",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API information",
            "GET /health": "Health check",
            "POST /predict": "Predict reading score",
            "GET /model-info": "Model information"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        model_data = load_model()
        return {
            "status": "healthy",
            "model_loaded": True,
            "features": len(model_data['feature_names']),
            "train_score": model_data['train_score'],
            "test_score": model_data['test_score']
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }

@app.get("/model-info")
async def model_info():
    """Get information about the trained model"""
    try:
        model_data = load_model()
        return {
            "model_type": model_data['model_type'],
            "features": model_data['feature_names'],
            "num_features": len(model_data['feature_names']),
            "training_score": model_data['train_score'],
            "test_score": model_data['test_score'],
            "mse": model_data['mse'],
            "mae": model_data['mae'],
            "data_cleaning": model_data.get('data_cleaning_info', {})
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading model: {str(e)}")

@app.post("/predict", response_model=PredictionResponse)
async def predict_reading_score(student_data: StudentData):
    """Predict reading score for a student"""
    try:
        # Load the model
        model_data = load_model()
        model = model_data['model']
        feature_names = model_data['feature_names']
        
        # Create a DataFrame with the input data
        input_df = pd.DataFrame([{
            'Gender': student_data.gender,
            'EthnicGroup': student_data.ethnic_group,
            'ParentEduc': student_data.parent_educ,
            'LunchType': student_data.lunch_type,
            'TestPrep': student_data.test_prep,
            'ParentMaritalStatus': student_data.parent_marital_status,
            'PracticeSport': student_data.practice_sport,
            'IsFirstChild': student_data.is_first_child,
            'NrSiblings': student_data.nr_siblings,
            'TransportMeans': student_data.transport_means,
            'WklyStudyHours': student_data.wkly_study_hours,
            'MathScore': student_data.math_score,
            'WritingScore': student_data.writing_score
        }])
        
        # Encode categorical features
        input_encoded = encode(input_df)
        
        # Select only the features used by the model
        input_features = input_encoded[feature_names].values.astype(float)
        
        # Handle NaN values
        input_features = np.nan_to_num(input_features, nan=-1)
        
        # Make prediction using the scikit-learn model
        prediction = model.predict(input_features)[0]
        
        # Determine confidence based on model performance
        test_score = model_data['test_score']
        if test_score > 0.3:
            confidence = "high"
        elif test_score > 0.2:
            confidence = "medium"
        else:
            confidence = "low"
        
        return PredictionResponse(
            predicted_reading_score=round(prediction, 2),
            confidence=confidence,
            features_used=feature_names
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
