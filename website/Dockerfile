FROM python:3.6
LABEL maintaner="lianmc9408@163.com"
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -i https://pypi.mirrors.ustc.edu.cn/simple -r requirements.txt \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ADD . /app
EXPOSE 5005
CMD ["python", "subpro.py"]

