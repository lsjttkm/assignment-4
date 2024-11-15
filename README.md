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
python app/unemployment_report.py
```

Run the stocks report:

```sh
python app/stocks_report.py
```



## Testing

Run tests:

```sh
pytest
```
