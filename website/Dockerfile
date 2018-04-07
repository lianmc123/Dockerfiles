FROM python:3.6
LABEL maintaner="lianmc9408@163.com"
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -i https://pypi.mirrors.ustc.edu.cn/simple -r requirements.txt  \
	&& TZ='Asia/Shanghai'; export TZ
ADD . /app
EXPOSE 5005
RUN celery -A tasks.celery worker -l info
CMD ["uwsgi", "--ini", "w_uwsgi.ini"]

