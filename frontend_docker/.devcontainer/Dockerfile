FROM node
USER root


RUN apt-get update 
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8


# RUN npx tailwindcss init

# Tailwindとかを入れる
# https://tailwindcss.com/docs/guides/vite

# https://mui.com/material-ui/getting-started/installation/
# https://ui.shadcn.com/docs/installation/vite
# https://qiita.com/Junpei_Takagi/items/3615505dcabd2e97f3e1