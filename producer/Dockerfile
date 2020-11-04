FROM continuumio/miniconda3:4.8.2-alpine

ADD . /app
WORKDIR /app

ENV PATH /opt/conda/bin:$PATH

RUN conda install -c conda-forge --yes --file requirements_conda.txt && \
	pip install -r requirements_pip.txt && \
	conda clean --all --yes