FROM ubuntu:latest




RUN apt-get clean && \ 
	 apt-get update && \
    apt-get install  --no-install-suggests -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /home/zhou/python/Pythonblog/ && \
   rm -rf /tmp && \     

COPY ./  /home/zhou/python/Pythonblog
COPY blog_nginx.config /etc/nginx/sites-available/default
RUN pip3 install -r /home/zhou/python/Pythonblog/requirements.txt && \
	cd /home/zhou/python/Pythonblog/ && \
	uwsgi --ini blog_uwsgi.ini

EXPOSE 80
##uwsgi --ini blog_uwsgi.ini
