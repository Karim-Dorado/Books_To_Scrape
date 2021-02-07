# Books_To_Scrape

Python 3.9 is required to run this utility. Make sure to download and install this version of Python before proceeding.

## How to create and activate a virtual environment

### Step 1: Create a virtual environment

To create a virtual environment, you need to go to your project’s directory and run venv.

**On macOS and Linux:** run `python3 -m venv env` from your console.

**On Windows:** run `py -m venv env` from your console.

The argument `env` is the location to create the virtual environment.

### Step 2: Activate your virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it.

**On macOS and Linux:** `source env/bin/activate`

**On Windows:** `.\env\Scripts\activate`

If you want to leave your virtual environment, you just need to run `deactivate` from your console.

## Instructions

### How to run this utility

#### On macOS and Linux:

**Step 1:** Create a folder on your computer to use for your Python programs. A good suggestion would be to name it bookstoscrape and place it in your Home folder

**Step 2:** Open your terminal program.

**Step 3:** Type `cd bookstoscrape` to change directory to your bookstoscrape folder, and hit Enter.

**Step 4:** Type `git init` on your console 

**Step 5:** Type `git remote add BTS https://github.com/Karim-Dorado/Books_To_Scrape.git`

**Step 6:** Type `git clone https://github.com/Karim-Dorado/Books_To_Scrape.git`

**Step 7:** Create and activate your virtual environment

**Step 8:** Type `pip freeze` to see a list of all installed packages and their versions.

**Step 9:** Type `python3 main.py` to run this program.

#### On Windows:

**Step 1:** Create a folder on your computer to use for your Python programs, such as `C:\bookstoscrape`

**Step 2:** In the Start menu, select "Run...", and type in cmd. This will cause the Windows terminal to open.

**Step 3:** Type `cd \bookstoscrape` to change directory to your bookstoscrape folder, and hit Enter.

**Step 4:** Type `git init` on your console 

**Step 5:** Type `git remote add BTS https://github.com/Karim-Dorado/Books_To_Scrape.git`

**Step 6:** Type `git clone https://github.com/Karim-Dorado/Books_To_Scrape.git`

**Step 7:** Create and activate your virtual environment

**Step 8:** Type `pip freeze` to see a list of all installed packages and their versions.

**Step 9:** Type `py main.py` to run this program.