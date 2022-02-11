from distutils.command.config import config
import pandas as pd
import argparse

from sklearn.linear_model import ElasticNet
from src.utils.common_utils import read_params,create_dir,save_reports
import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score



logging_str= "[%(asctime)s: %(levelname)s : %(module)s]: %(message)s"
logging.basicConfig(level = logging.INFO)




def eval_metrics(actual,pred):
    rmse= mean_squared_error(actual,pred)
    mae=mean_absolute_error(actual,pred)
    r2 =r2_score(actual,pred)

    return rmse,mae,r2


def evaluate(config_path):
    config = read_params(config_path)
    artifacts= config["artifacts"]
    test_data_path = artifacts["split_data"]["test_path"]
    model_path = artifacts["model_path"]
    target = config['base']['target_col']
    scores_file =artifacts["reports"]["scores"]

    test = pd.read_csv(test_data_path)
    test_y = test[target]
    test_x = test.drop(target, axis=1)

    lr = joblib.load(model_path)

    logging.info(f"model is loaded {model_path}")

    predicted_values = lr.predict(test_x)

    rmse ,mae,r2 = eval_metrics(test_y,predicted_values)

    scores ={
        'rmse' : rmse,
        'mae' :mae,
        'r2_score' :r2
    }

    save_reports(scores_file,scores)





# argpass is like fuction creation 
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default= "params.yaml")
    parsed_args = args.parse_args()

    try:
        data=evaluate(config_path = parsed_args.config)
        logging.info(f"evaluation stage completed")
    except Exception as e:
        logging.error(e)
        raise e