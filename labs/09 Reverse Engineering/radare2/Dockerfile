FROM remnux/radare2

COPY .bash_aliases /home/nonroot
COPY bomb g1 g2 /home/nonroot/.local/share/radare2/.r2panels/
USER root
RUN chown -R nonroot:nonroot /home/nonroot/.local/share/radare2/.r2panels/
USER nonroot
