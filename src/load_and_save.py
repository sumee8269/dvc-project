from operator import index
import pandas as pd
import argparse
from src.utils.common_utils import read_params,clean_prev_dirs_if_exists,create_dir,save_local_df
import logging


#logging_str = "%(asctime)s %(name)s %(levelname)s %(message)s"
logging.basicConfig(level= logging.INFO)


def get_data(config_path):
    config = read_params(config_path)
    data_path =config["data_source"]["s3_source"]
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_data_dir = config["artifacts"]["raw_local_data_dir"]
    raw_local_data = config["artifacts"]["raw_local_data"]

    clean_prev_dirs_if_exists(artifacts_dir)

    create_dir(dirs=[artifacts_dir,raw_local_data_dir])

    df = pd.read_csv(data_path,index_col=0)

    save_local_df(df,raw_local_data,header =True)


# argpass is like fuction creation 
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default= "params.yaml")
    parsed_args = args.parse_args()

    try:
        data=get_data(config_path = parsed_args.config)
        logging.info(f"reading and writing raw data stage completed")
    except Exception as e:
        logging.error(e)
        raise e
