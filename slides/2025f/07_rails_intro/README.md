# Rails Development Environment

This directory contains a Docker-based development environment for learning Ruby on Rails.

## Quick Start

### 1. Start the Development Environment

```bash
# In a terminal, navigate to the directory whith your Dockerfile and docker-compose.yml file
# Start the development environment
docker-compose up -d

# Check that services are running
docker-compose ps
```

### 2. Launch a Terminal in the Rails Container

```bash
# Get a bash shell in the Rails container
docker-compose exec web bash
```

### 3. Set Up the App Scaffold


```bash
# Inside the container
# Install rails
gem install rails

# Now create a new Rails application
rails new blog_app --database=mysql --skip-test --skip-system-test
cd blog_app

# Install dependencies
bundle install

# Create the database
rails db:create

# Start the Rails server
rails server -b 0.0.0.0 -p 3000
```

### 4. Access Your Application

- Open your browser to `http://localhost:3000`
- You should see the Rails welcome page

## Environment Details

### Services

- **web**: Rails development container with Ruby 3.4.5
- **db**: MySQL 8.0 database server

### Ports

- **3000**: Rails development server
- **3306**: MySQL database

### Volumes

- **./app**: Your Rails application code (mounted to `/app` in container)
- **bundle_cache**: Gem cache for faster bundle installs
- **mysql_data**: Persistent MySQL data

## Common Commands

### Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f web
docker-compose logs -f db

# Restart services
docker-compose restart

# Remove everything (including volumes)
docker-compose down -v
```

### Rails Development Commands

```bash
# Create new Rails app
rails new myapp --database=mysql

# Generate components
# Gemerate a new model for a User
rails generate model User name:string email:string
# Generate a new controller for interacting with Users
rails generate controller Users index show

# Database operations
rails db:create
rails db:migrate
rails db:drop
rails db:seed
rails db:rollback

# Development server
rails server -b 0.0.0.0 -p 3000

# Interactive console
rails console

# Run tests
rails test

# Check routes
rails routes
```

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs web

# Rebuild the containers
docker-compose build --no-cache
docker-compose up -d
```

### Database Connection Issues

```bash
# Check if database is running
docker-compose ps db

# Restart database
docker-compose restart db

# Wait for database to be ready
docker-compose exec web bash
# Inside container:
rails db:create
```

### Port Already in Use

If port 3000 is already in use:

```bash
# Stop other services using port 3000
lsof -ti:3000 | xargs kill -9

# Or change the port in docker-compose.yml
# ports:
#   - "3001:3000"  # Use port 3001 instead
```

### MySQL DB Connection

See docker-compose file for passwords

```bash
# Connection as root user
mysql -h db --skip-ssl -u root -p

# Connecting as rails user
mysql -h db --skip-ssl -u rails_user -p
```

## Cleanup

When you're done:

```bash
# Stop and remove containers
docker-compose down

# Remove everything including volumes (this will delete your database)
docker-compose down -v

# Remove Docker images (optional)
docker rmi rails_intro_web
docker rmi mysql:8.0
```
