FROM python:3.9

ENV UWSGI_PIP_VERSION 2.0.20

RUN mkdir /opt/lrs /opt/lrs/logs

# Install our reqs
RUN apt-get update && \
	apt-get install -y && \
	pip3 install fabric3 virtualenv	

COPY . ./opt/lrs/ADL_LRS	

WORKDIR /opt/lrs/ADL_LRS

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

# Prepare the configuration
COPY docker/lrs/uwsgi/lrs_uwsgi.ini /etc/uwsgi/vassals/lrs_uwsgi.ini
COPY docker/lrs/uwsgi/lrs.service /lib/systemd/system/lrs.service

COPY docker/lrs/modified-fabfile.py /opt/lrs/ADL_LRS/fabfile.py

# We'll need to run the setup
COPY docker/lrs/scripts/setup-lrs.sh /bin/setup-lrs.sh

CMD ["/bin/setup-lrs.sh"]
