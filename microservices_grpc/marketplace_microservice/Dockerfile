FROM python:3

RUN mkdir service
COPY recommendpb/ service/recommendpb/
COPY marketplace_microservice/ service/
WORKDIR /service/
RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. recommendpb/recommend.proto

EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
