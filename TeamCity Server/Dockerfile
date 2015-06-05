FROM justdevelopers/java

MAINTAINER JustDevelopers

ENV TEAMCITY_VERSION 9.0.4
ENV TEAMCITY_HOME /opt/lib/teamcity
ENV TEAMCITY_DATA_PATH /var/lib/teamcity

WORKDIR /data

RUN apt-get install -y \
    wget \
    tar

VOLUME  ["/data/teamcity"]
ENV TEAMCITY_DATA_PATH /data/teamcity

ENV TEAMCITY_PACKAGE TeamCity-$TEAMCITY_VERSION.tar.gz
ENV TEAMCITY_DOWNLOAD http://download.jetbrains.com/teamcity
RUN wget $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE && \
    tar zxf $TEAMCITY_PACKAGE -C /opt && \
    rm -rf $TEAMCITY_PACKAGE

EXPOSE 8111
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]