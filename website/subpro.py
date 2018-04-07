import subprocess

subprocess.Popen(["celery", "-A", "tasks.celery", "worker", "-l", "info"])
subprocess.Popen(["uwsgi", "--ini", "w_uwsgi.ini"])

# RUN celery -A tasks.celery worker -l info
# CMD ["uwsgi", "--ini", "w_uwsgi.ini"]
