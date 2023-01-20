FROM alpine
MAINTAINER jgourd@ut.edu

RUN set -xe && apk add -U vsftpd && rm -rf /var/cache/apk/*

ADD vsftpd.conf vsftpd.banner /etc/vsftpd/
RUN ln -sf /proc/1/fd/1 /var/log/vsftpd.log

RUN install -d -m u+wx,u-r,g+rwxs,o-rwx -o ftp -g root /var/lib/ftp/incoming
VOLUME /var/lib/ftp/incoming
WORKDIR /var/lib/ftp

EXPOSE 21 32022-32041

COPY run-vsftpd.sh /usr/sbin
CMD ["/usr/sbin/run-vsftpd.sh"]
