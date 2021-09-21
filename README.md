# LeekyLeaky
**This project is _NOT_ official, it only serves as an alternative to HIBP's API system.**
## About
A simple Python script to check multiple e-mail addresses for possible breaches at once using HaveIBeenPwned's JSON response, selenium and ChromeDriver.
### Abilities 
Checking for addresses from file/arguments, checking for active Paste links
### Output
Breach Title, Date and (if available) active Paste links
## Installation
Download ChromeDriver according to your Chrome's version [here](https://chromedriver.storage.googleapis.com/index.html), don't forget to add it to your system's PATH!<br>
Install requirements from requirements.txt<br>
```python
pip install -r requirements.txt
```
## Usage
```shell
python leekyleaky.py <path to file with e-mail address inside/e-mail address>
Arguments: --only_valid - outputs non-empty results
```
<br>Example:<br>
```shell
python leekyleaky.py example@example.org example.txt --only_valid
```



