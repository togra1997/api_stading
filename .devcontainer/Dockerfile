FROM python:3.11.10-bullseye
USER root


RUN apt-get update 
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
RUN pip install uv


# # RUN poetry new project
# WORKDIR project
# RUN poetry install
# Poetryが仮想環境を生成しないようにする
# RUN poetry config virtualenvs.create false
# WORKDIR /workdir
# VOLUME /var/test