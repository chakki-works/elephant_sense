import os
from sklearn.externals import joblib


class SaveModels():

    def __init__(self, clf, data_folder=""):
        file_name = "banana.pkl"
        def_file_path = "../../models/"
        self.data_folder = data_folder

        if not data_folder:
            self.data_file = os.path.join(os.path.dirname(__file__), def_file_path) + file_name
        else:
            self.data_file = self.data_folder + file_name

        joblib.dump(clf, self.data_file)
