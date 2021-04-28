"""MLOps Library"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import xgboost as xgb
import logging

logging.basicConfig(level=logging.INFO)

import warnings

warnings.filterwarnings("ignore", category=UserWarning)


def load_model(model="stroke_prediction.joblib"):
    """Grabs model from disk"""

    clf = joblib.load(model)
    return clf
    
def data():
    df = pd.read_csv("healthcare-dataset-stroke-data.csv")
    return df
    
def retrain(tsize=.2, model_name="stroke_prediction.joblib"):
    """Retrains the model
    See this notebook: Baseball_Predictions_Export_Model.ipynb
    """
    dataset = data()
    bmi_median = dataset["bmi"].median()
    dataset = dataset.fillna(bmi_median, inplace=False)
    dataset['bmi'].fillna(dataset['bmi'].mean(), inplace=True)
    dataset['smoking_status'].fillna(dataset['smoking_status'].mode()[0], inplace = True)
    labels = dataset.pop("stroke")
    
    dataset_onehotted = pd.get_dummies(dataset)
    dataset_onehotted.drop('id',axis=1,inplace=True)
    dataset_onehotted['age'] = dataset_onehotted['age'].astype('float')
    dataset_onehotted = dataset_onehotted.astype('float')
    
    smote = SMOTE()
    dataset_resampled, labels_resampled = smote.fit_resample(dataset_onehotted, labels)
    train_data, test_data, train_labels ,test_labels = train_test_split(
        dataset_resampled, labels_resampled, test_size=tsize)
    xgb_clf = xgb.XGBClassifier(use_label_encoder=True, objective="binary:logistic").fit(train_data, train_labels)

    accuracy = xgb_clf.score(test_data, test_labels)
    logging.debug(f"Model Accuracy: {accuracy}")
    joblib.dump(xgb_clf, model_name)
    return accuracy, model_name
    
def predict(payload):
    
    load = pd.DataFrame(data=payload)
    clf =  load_model()
    prediction = clf.predict_proba(load)[0][0]
    predict_log_data = {
        "payload" : payload,
        "prediction" : prediction,
    }
    logging.debug(f"Prediction: {predict_log_data}")
    return prediction
