# CS291A Scripts

## Obtaining python package requirements

For simplicity, it is prefered that you use Docker to run these scripts. That
way you need not worry about setting up a local python environment. However,
you're free to also try a direct installation.

__Step 1__ Clone this repository:

```sh
git clone https://github.com/scalableinternetservices/ucsb_website.git
```

Note: If you'd like to fetch updates to these scripts then run `git pull` from
the `ucsb_website` directory at a later time.

__Step 2__ Change into the scripts directory:

```sh
cd ucsb_website/scripts
```

### Installation via Docker

__Step 3__ Build the docker container which will take care of installing the dependencies:

```sh
docker build -t cs291_scripts .
```

Note: Re-run this command to rebuild the container image when any of the files change.

Side Note: If you don't want to rebuild the container you can also expose a directory as a volume in docker. Can do so by modifying the run command as

```sh
docker run -v /home/exampleusername/ucsb_website/scripts:/app --rm -it cs291_scripts ./PROJECT_SCRIPT.py ADDITIONAL_ARGUMENTS
```

This allows any changes made in the scripts (that are in the script directory) to be automatically reflected instead of rebuilding the docker image. 

(Also find out more about volumes here: https://www.baeldung.com/ops/docker-volumes)

### Direct Installation

__Step 3__ Install python dependencies:

```sh
pip install -r requirements.txt
```

 Note: Run-run this command when the `requirements.txt` file changes.

## Running the scripts

The below instructions are for running the scripts from inside docker. If you'd
like to run them directly simply exclude the `docker run -it cs291_scripts`
part of the command.

### Run Project 0 Verification Script

Usage:

```sh
docker run -it --rm cs291_scripts ./project0.py GITHUB_WEBSITE_URL
```

### Project 1 Verification Script

Usage:

```sh
docker run -it --rm cs291_scripts ./project1.py LAMBDA_APP_URL
```

### Project 2 Verification Script

Usage:

```sh
docker run -it --rm cs291_scripts ./project2.py GOOGLE_CLOUD_RUN_URL
```

### Project 3 Server-Side Partial Verification Script

In order to run these scripts via a container and talk to your container you'll
need to set up a user defined network. Run this one time:

```sh
docker network create cs291

```

Run the error-case tests:

```sh
docker run -it --rm --net cs291 cs291_scripts ./project3.py test http://server:3000/
```

Connect to the stream:

```sh
docker run -it --rm --net cs291 cs291_scripts ./project3.py stream http://server:3000/
```

Verify stream re-connect behavior by copying an event ID, and then run:

```sh
docker run -it --rm --net cs291 cs291_scripts ./project3.py stream http://server:3000/ --last-event-id LASTID
```
