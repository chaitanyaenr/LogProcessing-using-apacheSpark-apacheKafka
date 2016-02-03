# Edited by Naga Ravi Chaitanya Elluri
FROM ubuntu:latest
MAINTAINER naga.elluri@colorado.edu
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh
USER root
WORKDIR /root
RUN echo 91.189.88.46    archive.ubuntu.com >> /etc/hosts
RUN echo 91.189.88.46    security.ubuntu.com >> /etc/hosts
RUN /etc/init.d/networking restart
RUN echo nameserver 8.8.8.8 >> /etc/resolv.conf
RUN echo nameserver 8.8.4.4 >> /etc/resolv.conf
RUN apt-get update
RUN apt-get -y install wget
RUN wget --quiet --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O jdk-7u51-linux-x64.tar.gz http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz
RUN mkdir -p /usr/lib/jvm; \
    mv jdk-7u51-linux-x64.tar.gz /usr/lib/jvm; \
    tar zxvf /usr/lib/jvm/jdk-7u51-linux-x64.tar.gz -C /usr/lib/jvm; \
    rm /usr/lib/jvm/jdk-7u51-linux-x64.tar.gz
RUN update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk1.7.0_51/bin/javac 1; \
    update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.7.0_51/bin/java 1; \
    update-alternatives --set javac /usr/lib/jvm/jdk1.7.0_51/bin/javac; \
    update-alternatives --set java /usr/lib/jvm/jdk1.7.0_51/bin/java
RUN echo 'JAVA_HOME=/usr/lib/jvm/jdk1.7.0_51' >> /etc/profile; \
    echo 'PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile; \
    echo 'export JAVA_HOME' >> /etc/profile; \
    echo 'export PATH' >> /etc/profile
ENV JAVA_HOME /usr/lib/jvm/jdk1.7.0_51
ENV JRE_HOME /usr/lib/jvm/jdk1.7.0_51
ENV PATH $PATH:$JAVA_HOME/bin

RUN apt-get update
RUN apt-get -y install xdotool
RUN apt-get -y install git
#RUN  apt-get install openjdk-7-jre
#RUN  apt-get install openjdk-7-jdk
# ENV PATH $PATH:/usr/lib/jvm/java-6-openjdk-amd64

# RUN cd /root
# sudo apt-get install default-jdk
RUN mkdir project_kafka
WORKDIR /root/project_kafka

RUN apt-get -y install wget

RUN wget http://www.eu.apache.org/dist/kafka/0.8.2.0/kafka_2.10-0.8.2.0.tgz

RUN tar -xzf kafka_2.10-0.8.2.0.tgz


WORKDIR /root/project_kafka/kafka_2.10-0.8.2.0
RUN wget http://mirrors.ukfast.co.uk/sites/ftp.apache.org/zookeeper/stable/zookeeper-3.4.6.tar.gz

RUN tar -xvf zookeeper-3.4.6.tar.gz

WORKDIR /root/project_kafka/kafka_2.10-0.8.2.0/zookeeper-3.4.6


RUN touch conf/zoo.cfg
RUN chmod 777 conf/zoo.cfg
RUN echo tickTime=2000 > conf/zoo.cfg
RUN echo dataDir=/var/lib/zookeeper >> conf/zoo.cfg
RUN echo clientPort=2181 >> conf/zoo.cfg
RUN echo initLimit=5 >> conf/zoo.cfg
RUN echo syncLimit=2 >> conf/zoo.cfg
RUN mkdir -p /var/lib/zookeeper


RUN apt-get update -y
RUN apt-get install nodejs -y
RUN apt-get install npm -y

ADD run.js . 
