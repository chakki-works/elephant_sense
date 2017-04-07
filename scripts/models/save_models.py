import os
from sklearn.externals import joblib


class SaveModelsScalor():

    def __init__(self, clf, scaler, data_folder=""):
        model_file_name = "banana.pkl"
        scaler_file_name = "banana_scaler.pkl"

        def_file_path = "../../models/"
        self.data_folder = data_folder

        if not data_folder:
            model_file = os.path.join(os.path.dirname(__file__), def_file_path) + model_file_name
            scaler_file = os.path.join(os.path.dirname(__file__), def_file_path) + scaler_file_name
        else:
            model_file = self.data_folder + model_file_name
            scaler_file = self.data_folder + model_file_name

        joblib.dump(clf, model_file)
        joblib.dump(scaler, scaler_file)

