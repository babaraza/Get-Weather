[![Python 3.7](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Get Weather Data
Gets weather data from [https://api-ak.wunderground.com](https://api-ak.wunderground.com) for Sugar Land, TX


### Usage

Run `app.py` and it will ask you:
 
```sh
Enter Start year > 
```
and
```sh
Enter End year > 
```

*To get data for just one year, put the same year for `Start Year` and `End Year`*

The script will then follow the steps:
- Construct proper URL with `Start Year` and `End Year`
- Get *temperature* data for each month
- Get the *Average Maximum Temperature* for each month
- Print out the *temperature* for each month