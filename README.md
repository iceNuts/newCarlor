newCarlor
=========

Reborn Carlor App

Run
===

Install Python3 and virtualenv
------------------------------
Mac: `brew install python3`

install virtualenv via pip or easy_install:
```
pip install virtualenv
easy_install virtualenv
```

Init Repo
---------
```
git clone REPO_LINK newCarlor && cd $_

# create python3 isolated env named venv via virtualenv
virtualenv -p=$(which python3) --no-site-packages venv
source venv/bin/activate

# install requirements
pip install -p requirements.txt

```

Get Running
-----------
```
# use sudo if using 80 port
cd app && python3 main.py
