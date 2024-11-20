# Assignment 4 (Cleanup-exercise)


## Setup

Create virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate virtual environment (whenever you come back):

```sh
conda activate reports-env-2024
```

Install Packages:

```sh
pip install -r requirements.txt
```

Obtain API Key from AlphaVantage (https://www.alphavantage.co/support/#api-key):

Create a ".env" file & add contents like the following (with your own AlphaVantage API Key)

```sh
ALPHAVANTAGE_API_KEY="..."
```



## Usage

Run the example script:

```sh
python app/example.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment_report.py
#python app/unemployment_report.py

python -m app.unemployment_report
```

Run the stocks report:

```sh
#python app/stocks_report.py

python -m app.stocks_report
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```
