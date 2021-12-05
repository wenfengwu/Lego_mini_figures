# lego-mini-figs

## Install homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Install pyenv

https://github.com/pyenv/pyenv

```
brew update
brew install pyenv
```

## MacOS, if Pyenv is installed with Homebrew:

```
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile

echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

## Install python

```
pyenv install 3.8.12
```

## Switch python version

```
pyenv local 3.8.12
```

# Install packages
```
pip3 install -r requirements.txt
```

# Set DATABASE_URL environment variable
```
export DATABASE_URL=mysql+pymysql://root:rootroot@localhost:3306/minifigs
```

# Init database

```
flask db init
flask db migrate
# Only run after db schema changes, no need to drop tables in database!
flask db upgrade
python import_db.py
```

# Update the project

```
pip freeze > requirements.txt
pip3 install -r requirements.txt # team members need to install this document
```
