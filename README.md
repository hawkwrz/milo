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
It will print outputthe earliest possible legal date between Jan 1, 2000 and Dec 31, 2999 (inclusive)
## Changelog/release note

```
(unreleased)
------------
- Screenshots. [Jakub Żmuda]
- Requirements and python task. [Jakub Żmuda]
- CSV download option. [Jakub Żmuda]
- Unittesting. [Jakub Żmuda]
- Migrations. [Jakub Żmuda]
- Views, templates, model fix, urls. [Jakub Żmuda]
- CustomUser model. [Jakub Żmuda]
- Initial commit. [Jakub Żmuda]
```
