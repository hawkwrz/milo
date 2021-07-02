# MILO
Technical test
## Installation project
Clone project.

```bash
git clone https://github.com/hawkwrz/milo.git
```
Create virutalenv and then activate virtualenv.
```bash
python3 -m venv venv
venv\Scripts\activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Last steps.
```bash
python mange.py migrate
python mange.py runserver
```
Project will work on http://127.0.0.1:8000/
## Usage python task
input.txt should have one line in the "A/B/C" format, where A,B,C are integers between 0 and 2999.
```bash
python task.py input.txt
```
It will print output the earliest possible legal date between Jan 1, 2000 and Dec 31, 2999 (inclusive)


## List what was done
```
+ Installed latest Django
+ Extend the User model
+ Create views for: list of all users, viewing, adding, editing and deleting a single user
+ Create two template tags
+ Create simple Unit Test
+ Optional task (CSV file view)
``` 

## Changelog

```
- Screenshots.
- Requirements and python task.
- CSV download option.
- Unittesting.
- Views, templates.
- CustomUser model.
- Initial commit.
```