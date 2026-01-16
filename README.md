# Potato Disease Prediction App

This is Potato Disease Classification End to End Deep Learning project Developed with Tensorflow and CNN

## Requirements
Python 3.12.3

## Dataset for notebook
https://www.kaggle.com/datasets/muhammadardiputra/potato-leaf-disease-dataset

## How to install and run
### Clone the repo:
```shell
git clone https://github.com/aditya-deshmukh-tech/potato-disease-prediction-end-to-end-DL-project.git
```

```shell
cd potato-disease-prediction-end-to-end-DL-project
```

### create virtual environment (linux with python 3.12.3)
```shell
python3 -m venv .venv
```

### create virtual environment (windows with python 3.12.3)
here download python `3.12.3` specifically and use that
```batch
py -3.12.3 -m venv .venv
```

### Activate virtual environment (linux)
```shell
source .venv/bin/activate
```

### Activate virtual environment (windows)
```shell
.venv\Scripts\activate
```

### install dependencies
```shell
pip install -r requirements.txt
```

### run project
```shell
uvicorn app.main:app --reload --port 8080
```

Once you see in logs `Application startup complete.` go to http://localhost:8080/ui/potato_disease_ui
