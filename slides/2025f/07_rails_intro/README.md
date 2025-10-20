# Rails Development Environment

This directory contains a Docker-based development environment for learning Ruby on Rails.

## Quick Start

### 1. Start the Environment

```bash
# Navigate to the Rails intro directory
cd slides/2025f/07_rails_intro/

# Start the development environment
docker-compose up -d

# Check that services are running
docker-compose ps
```

### 2. Get a Terminal in the Rails Container

```bash
# Get a bash shell in the Rails container
docker-compose exec web bash
```

### 3. Create Your First Rails App

```bash
# Inside the container, create a new Rails application
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

### Rails Commands (inside container)

```bash
# Get a shell in the container
docker-compose exec web bash

# Run Rails commands directly
docker-compose exec web rails console
docker-compose exec web rails generate model Post title:string
docker-compose exec web rails db:migrate
docker-compose exec web rails test
```

### Rails Development Commands

```bash
# Create new Rails app
rails new myapp --database=mysql

# Generate components
rails generate model User name:string email:string
rails generate controller Users index show
rails generate scaffold Post title:string content:text

# Database operations
rails db:create
rails db:migrate
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

## Database Configuration

The environment is pre-configured with:

- **Database**: `rails_development`
- **Username**: `rails_user`
- **Password**: `password`
- **Host**: `db` (Docker service name)
- **Port**: `3306`

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs web

# Rebuild the container
docker-compose build --no-cache web
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

### Permission Issues

```bash
# Fix file permissions
sudo chown -R $USER:$USER .
```

## Learning Resources

- **Ruby Documentation**: https://www.ruby-lang.org/en/documentation/
- **Ruby Koans**: https://www.rubykoans.com/ (Interactive Ruby learning)
- **Ruby on Rails Tutorial**: https://learning.oreilly.com/library/view/ruby-on-rails/9780138050061/
- **Rails Guides**: https://guides.rubyonrails.org/

## Next Steps

1. Follow the hands-on walkthrough in the slides
2. Try the Ruby Koans for Ruby syntax practice
3. Work through the Rails Tutorial book
4. Experiment with different Rails generators
5. Add features like user authentication, file uploads, or API endpoints

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
