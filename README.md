# Convert long url into short url

### Create virtual environment

```
$ virtualenv env
```

### Activate virtual environment

```
$ source env/bin/activate
```

### Install requirement.txt file 
```
$ pip install -r requirement.txt
```

### Migration command

```
$ python manage.py migrate
```

### Create super admin user
```
$  python manage.py createsuperuser
	>>>  username : admin
	>>>  password : admin
```

### Run django server
```
$ python3 manage.py runserver
```

### Install crontab in local system

```
$ pip install crontab
```

### set crontab in local system

```
$ crontab -e

11 12 * * * sh /home/plutusdev/Projects/Task/shorturl/cruntabrun.sh

```