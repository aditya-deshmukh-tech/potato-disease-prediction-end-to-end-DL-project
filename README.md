# Potato Disease Prediction App

This is Potato Disease Classification End to End Deep Learning project Developed with Tensorflow and CNN

## Requirements
Python 3.12.3

## How to install and run
### Clone the repo:
```shell
git clone https://github.com/aditya-deshmukh-tech/customer-churn-end-to-end-ML-project
```

```shell
cd customer-churn-end-to-end-ML-project
```

### create virtual environment
```shell
python -m venv .venv
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
