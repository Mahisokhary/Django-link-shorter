echo installing requirements.......
apt-get install python -y
pip install -r required.txt
echo starting.....
python manage.py runserver 0.0.0.0:8000