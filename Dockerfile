# Use the official PostgreSQL image from Docker Hub
FROM postgres:15

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=django_user
ENV POSTGRES_PASSWORD=django_password
ENV POSTGRES_DB=django_db

# Expose PostgreSQL default port
EXPOSE 5432
