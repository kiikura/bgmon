FROM centos:centos6
MAINTAINER ME


RUN rpm -ivh http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/epel-release-6-5.noarch.rpm
RUN rpm -ivh http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-release-1.0-11.ius.centos6.noarch.rpm

RUN yum install --nogpgcheck -y python27 python27-virtualenv

#RUN virtualenv -p python27 --no-site-packages /opt/ve/bgmon

ADD . /opt/apps/bgmon

#RUN /opt/ve/djdocker/bin/pip install -r /opt/apps/djdocker/requirements.txt
#RUN (cd /opt/apps/bgmon && /opt/ve/bgmon/bin/python manage.py syncdb --noinput)
#RUN (cd /opt/apps/bgmon && /opt/ve/bgmon/bin/python manage.py collectstatic --noinput)


EXPOSE 8000

CMD ["/bin/bash"]
