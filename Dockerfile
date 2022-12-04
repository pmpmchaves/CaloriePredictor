FROM python:3.8.15-bullseye

RUN mkdir -p /app/source

WORKDIR /app/source

COPY requirements.txt /app/source/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/source

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["streamlitapp.py"]
