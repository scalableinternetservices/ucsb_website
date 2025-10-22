FROM ruby:3.4.5

# Install system dependencies
RUN apt-get update -qq && apt-get install -y \
    build-essential \
    default-mysql-client \
    default-libmysqlclient-dev \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app
ENV HOME=/app

# Create a non-root user
RUN groupadd -r rails && useradd -r -g rails rails

# Set bundle path to a user-writable location
ENV BUNDLE_PATH=/usr/local/bundle
ENV BUNDLE_CACHE_PATH=/usr/local/bundle/cache

# Create the bundle directory and set ownership
RUN mkdir -p /usr/local/bundle && \
    chown -R rails:rails /usr/local/bundle && \
    chown -R rails:rails /app

# Switch to rails user
USER rails

# Expose port 3000
EXPOSE 3000

# Default command (can be overridden in docker-compose)
CMD ["tail", "-f", "/dev/null"]
