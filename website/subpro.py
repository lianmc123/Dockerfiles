import subprocess

subprocess.Popen(["celery", "-A", "tasks.celery", "worker", "-l", "info"])
# subprocess.Popen(["ps", "-aux"])
subprocess.call(["uwsgi", "--ini", "w_uwsgi.ini"])

# RUN celery -A tasks.celery worker -l info
# CMD ["uwsgi", "--ini", "w_uwsgi.ini"]
