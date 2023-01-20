FROM alpine
MAINTAINER jgourd@ut.edu

RUN set -xe && apk add -U python3 && rm -rf /var/cache/apk/*

EXPOSE 31337

COPY run-chat.sh server.py /usr/bin/
CMD ["/usr/bin/run-chat.sh"]
