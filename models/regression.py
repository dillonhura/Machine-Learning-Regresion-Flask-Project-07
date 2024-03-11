import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

import mlflow
from mlflow.models.signature import infer_signature

mlflow.set_tracking_uri("http://web:5000")

 # Get path to file dynamically
# WD = os.path.dirname(os.path.abspath(__file__))

def train():
    # running locally
    # dataset = pd.read_csv('data/salary.csv')

    # define x (independent) and y (dependent) variable
    # X = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:, 1].values

    # # Split data to train (67%) and test (33%)
    # X_train, X_test, y_train, _ = train_test_split(X, y, test_size = 0.33, random_state = 0)

    # # Develop regression model
    # regressor = LinearRegression()
    # regressor.fit(X_train, y_train)

    # y_pred = regressor.predict(X_test)

    # print(y_pred)

    # =======================================

    with mlflow.start_run() as run:
        # read data source
        dataset = pd.read_csv('/app/data/salary.csv')

        # define x (independent) and y (dependent) variable
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values

        # Split data to train (67%) and test (33%)
        X_train, X_test, y_train, _ = train_test_split(X, y, test_size = 0.33, random_state = 0)

        # Develop regression model
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)

        print(y_pred)

        signature = infer_signature(X_test, y_pred)
        mlflow.sklearn.log_model(regressor, "model", signature=signature)

        print("Run ID: {}".format(run.info.run_id))

    return run.info.run_id

    # save model to pickle
    # pickle.dump(regressor, open(WD + '/pickled/model.pkl','wb'))

def predict(run_id):
    # load pickled model
    # model = pickle.load(open(WD + '/pickled/model.pkl','rb'))
    logged_model = f'runs:/{run_id}/model'

    model = mlflow.sklearn.load_model(logged_model)
    print(model.predict([[1.8]]))

if __name__ == "__main__":
    run_id = train()
    predict(run_id)
