FROM python:3.10-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
#RUN mkdir -p /app/static && chown 1006:1006 -R /app/static && chmod 744 -R /app/static
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /short_urls .
RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]
RUN chown -R 1006:1006 /app
EXPOSE 8000
USER 1006:1006
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
