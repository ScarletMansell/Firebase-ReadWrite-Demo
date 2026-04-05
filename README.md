# Firebase-ReadWrite-Demo

## Necessary prerequisites:

- A Google account
- Python installed on your computer
- Git installed on your computer


## Included files

- `write_data.py` to write data to your database
- `read_data.py` to read data in your database
- `requirements.txt` for dependencies (for modules not built into python by default)

## Setup

1. Open command prompt
2. Enter your desktop by running:
```
cd desktop
```
4. Clone this repo and enter it with:
```
git clone https://github.com/ScarletMansell/Firebase-ReadWrite-Demo.git
cd Firebase-ReadWrite-Demo
```
5. Install dependencies with:
```
pip install -r requirements.txt
```
## Setting up Firebase:
1. Go to your Firebase account and create a Project
2. Search and open 'Firestore' and create+setup a database
3. In Firebase, go to Settings -> Service Accounts and generate a private key. It'll download as a .json file
## Reading and Writing to your Database
1. Rename your key to 'serviceAccountKey.json' -- BE SURE TO KEEP THIS KEY PRIVATE
2. Write to your database with write_data.py, by running this in a command prompt:
```
python write_data.py
```
3. Read from your database with read_data.py, by running this in a command prompt:
```
python read_data.py
```
All done! Your data will be stored in your database (Firebase -> Firestore)
