export DATABASE_PORT=27017
export DATABASE_NAME=ShortUrlData4
export SHORTURL=http://127.0.0.1:8000/
export SECRET_KEYS='django-insecure-06929wb#(0pold7-q4v%y#9z@ab&2y0)wsjh(bj7in@jp$a75&'
echo "started here......."
cd /home/plutusdev/Projects/Task/shorturl/



. env/bin/activate

cd app
python tests.py


echo "Ended here....."
