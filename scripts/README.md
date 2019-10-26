# CS291A Scripts

## Installation

1. Clone this repository:
```
git clone https://github.com/scalableinternetservices/ucsb_website.git
```
2. Change into the scripts directory:
```
cd ucsb_website/scripts
```
3. Install python dependencies (re-run this to get latest updates):
```
pip install -r requirements.txt
```

## Project 0 Verification Script

Usage:

```
./project0.py GITHUB_WEBSITE_URL
```

## Project 1 Verification Script

Usage:

```
./project1.py LAMBDA_APP_URL
```

## Project 2 Verification Script

Usage:

```
./project2.py GOOGLE_CLOUD_RUN_URL
```


## Project 3 Server-Side Partial Verification Script

Run the error-case tests, and connect to the stream:

```
./project3.py URL
```

Skip the error-case tests, and just connect to the stream:

```
./project3.py --no-failures URL
```

Test re-connect by copying an event ID, and then run:

```
./project3.py --no-failures --last-event-id LASTID URL
```
