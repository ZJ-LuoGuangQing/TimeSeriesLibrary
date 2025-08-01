import subprocess
import os

# 设置环境变量
env = os.environ.copy()
env["CUDA_VISIBLE_DEVICES"] = "1"

# 定义数据集根目录
DATASET_ROOT = "../../dataset/m4"
RUN_PY_ROOT = "../../run.py"
MODEL = "Autoformer"
USE_GPU = "False"

def run_yearly():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Yearly",
        "--model_id", "m4_Yearly",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True,env=env)


def run_quarterly():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Quarterly",
        "--model_id", "m4_Quarterly",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True,env=env)

def run_monthly():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Monthly",
        "--model_id", "m4_Monthly",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True,env=env)

def run_weekly():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Weekly",
        "--model_id", "m4_Weekly",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True,env=env)

def run_daily():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Daily",
        "--model_id", "m4_Daily",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True,env=env)

def run_hourly():
    cmd = [
        "python", "-u", RUN_PY_ROOT,
        "--task_name", "short_term_forecast",
        "--is_training", "1",
        "--root_path", DATASET_ROOT,
        "--seasonal_patterns", "Hourly",
        "--model_id", "m4_Hourly",
        "--model", MODEL,
        "--data", "m4",
        "--features", "M",
        "--e_layers", "2",
        "--d_layers", "1",
        "--factor", "3",
        "--enc_in", "1",
        "--dec_in", "1",
        "--c_out", "1",
        "--batch_size", "16",
        "--d_model", "512",
        "--des", "Exp",
        "--itr", "1",
        "--learning_rate", "0.001",
        "--loss", "SMAPE",
        "--use_gpu", USE_GPU
    ]
    subprocess.run(cmd, text=True)

if __name__ == "__main__":
    run_hourly()
    # run_daily()
    # run_weekly()
    # run_monthly()
    # run_quarterly()
    # run_yearly()