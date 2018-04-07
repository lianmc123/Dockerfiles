import subprocess

subprocess.call('celery -A tasks.celery worker -l info', shell=True)
subprocess.call('uwsgi --ini w_uwsgi.ini', shell=True)

#RUN celery -A tasks.celery worker -l info
# CMD ["uwsgi", "--ini", "w_uwsgi.ini"]