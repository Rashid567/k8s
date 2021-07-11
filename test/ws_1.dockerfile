FROM python:3.9

COPY ./ /app
RUN pip install --no-cache-dir -r /app/requirements.txt
#EXPOSE 8080
CMD ["python", "/app/ws-1.py"]
