set -o errexit

pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install -r requirements.txt