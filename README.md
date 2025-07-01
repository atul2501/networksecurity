# Network Security Project: Phishing Data Detection

This project is designed to automate the end-to-end process of detecting phishing attacks using machine learning. It covers data ingestion, validation, transformation, model training, and prediction, with a FastAPI-based web interface and MongoDB integration.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Pipeline Overview](#pipeline-overview)
- [API Endpoints](#api-endpoints)
- [Artifacts & Outputs](#artifacts--outputs)
- [Dependencies](#dependencies)
- [License](#license)

---

## Project Structure

```
networksecurity/
│
├── app.py                      # FastAPI app for training and prediction
├── main.py                     # Script to run the training pipeline
├── networksecurity/            # Core package
│   ├── components/             # Data ingestion, validation, transformation, model training
│   ├── entity/                 # Config and artifact entities
│   ├── exception/              # Custom exception handling
│   ├── logging/                # Logging utilities
│   ├── pipeline/               # Training pipeline and batch prediction
│   ├── utils/                  # Utility functions and ML helpers
│   ├── cloud/                  # S3 sync utilities
│   └── constant/               # Project constants
├── final_model/                # Stores final trained model and preprocessor
├── Artifacts/                  # Stores intermediate and final artifacts
├── prediction_output/          # Stores prediction results
├── templates/                  # HTML templates for web output
├── requirements.txt            # Python dependencies
├── Dockerfile                  # For containerization
└── README.md                   # Project documentation
```

---

## Features

- **Automated ML Pipeline**: Ingests data from MongoDB, validates, transforms, and trains multiple models.
- **Model Selection**: Evaluates several classifiers and selects the best based on performance.
- **Experiment Tracking**: Integrates with MLflow and Dagshub for experiment tracking.
- **Web API**: FastAPI endpoints for training and batch prediction.
- **Data Drift Detection**: Validates data consistency between train and test sets.
- **Cloud Sync**: Syncs artifacts and models to AWS S3.

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/atul2501/networksecurity.git
   cd networksecurity
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory.
   - Add your MongoDB connection string:
     ```
     MONGO_DB_URL=<your_mongodb_url>
     ```

4. **(Optional) Docker Usage**
   ```bash
   docker build -t networksecurity .
   docker run -p 8000:8000 networksecurity
   ```

---

## Usage

### 1. **Train the Model**

- **Via CLI:**
  ```bash
  python main.py
  ```
- **Via API:**
  Start the server:
  ```bash
  python app.py
  ```
  Then visit: [http://localhost:8000/train](http://localhost:8000/train)

### 2. **Make Predictions**

- Use the `/predict` endpoint (via Swagger UI or programmatically) to upload a CSV and get predictions.

---

## Pipeline Overview

1. **Data Ingestion**
   - Connects to MongoDB, fetches data, stores as CSV, and splits into train/test sets.

2. **Data Validation**
   - Checks schema compliance and detects data drift using statistical tests.

3. **Data Transformation**
   - Handles missing values (KNNImputer), encodes features, and saves preprocessed data.

4. **Model Training**
   - Trains multiple classifiers (Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost).
   - Selects the best model based on evaluation metrics.
   - Logs experiments to MLflow/Dagshub.
   - Saves the final model and preprocessor.

5. **Prediction**
   - Loads the trained model and preprocessor to make predictions on new data.

---

## API Endpoints

- `GET /` : Redirects to API docs.
- `GET /train` : Triggers the training pipeline.
- `POST /predict` : Accepts a CSV file and returns predictions as an HTML table.

---

## Artifacts & Outputs

- **Artifacts**: Intermediate files (CSV, NPY, PKL) for each pipeline stage, stored in the `Artifacts/` directory.
- **Final Model**: Saved in `final_model/` as `model.pkl` and `preprocessor.pkl`.
- **Prediction Output**: Results saved in `prediction_output/output.csv`.

---

## Dependencies

Key dependencies (see `requirements.txt` for full list):

- Python 3.x
- pandas, numpy, scikit-learn
- pymongo, certifi, python-dotenv
- fastapi, uvicorn, python-multipart
- mlflow, dagshub
- joblib

---

## License

[MIT License](LICENSE) (or specify your license here)

---

## Acknowledgements

- [MLflow](https://mlflow.org/)
- [Dagshub](https://dagshub.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [scikit-learn](https://scikit-learn.org/)

---

**Feel free to customize this documentation further for your specific needs!**

Would you like this written directly to your `README.md` file?
