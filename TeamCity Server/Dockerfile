FROM justdevelopers/java

MAINTAINER JustDevelopers

ENV TEAMCITY_VERSION 9.0.4
ENV TEAMCITY_HOME /opt/lib/teamcity
ENV TEAMCITY_DATA_PATH /var/lib/teamcity

WORKDIR /data

RUN apt-get install -y \
    wget \
    tar
    
    
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get intall -y \
    build-essential
    
RUN wget http://python.org/ftp/python/3.3.0/Python-3.3.0.tar.bz2 && \
    tar jxf ./Python-3.3.0.tar.bz2 && \
    cd ./Python-3.3.0 && \
    ./configure --prefix=/opt/python3.3 && \
    make && sudo make install

VOLUME  ["/data/teamcity"]
ENV TEAMCITY_DATA_PATH /data/teamcity

ENV TEAMCITY_PACKAGE TeamCity-$TEAMCITY_VERSION.tar.gz
ENV TEAMCITY_DOWNLOAD http://download.jetbrains.com/teamcity
RUN wget $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE && \
    tar zxf $TEAMCITY_PACKAGE -C /opt && \
    rm -rf $TEAMCITY_PACKAGE

ENV STORAGE_DIRECTORY $JAVA_HOME/jre/lib/security/cacerts
ENV MOUNT_DIRECTORY /data/teamcity

ADD add_certs.py add_certs.py

EXPOSE 8111
CMD ["python", "-c", "add_certs.py"]
