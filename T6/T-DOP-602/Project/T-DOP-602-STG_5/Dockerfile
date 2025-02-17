FROM jenkins/jenkins:lts

# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
# RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugins -f /usr/share/jenkins/ref/plugins.txt

ENV USER_CHOCOLATEEN_PASSWORD=chocolateen4269*
ENV USER_VAUGIE_G_PASSWORD=vaugie_g4269*
ENV USER_I_DONT_KNOW_PASSWORD=i_dont_know4269*
ENV USER_NASSO_PASSWORD=nasso4269*
