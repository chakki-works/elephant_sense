FROM continuumio/miniconda3

ENTRYPOINT []
CMD [ "/bin/bash" ]

# Remove (large file sizes) MKL optimizations.
RUN conda install -y nomkl

# matplotlib issue
# https://github.com/ContinuumIO/anaconda-issues/issues/1068
RUN conda install -y numpy scipy scikit-learn pandas

ADD ./requirements_app.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD . /opt/app/
WORKDIR /opt/app/

CMD python run.py
