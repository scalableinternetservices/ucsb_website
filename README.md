# Dependency Installation

In order to build and update the website you will need two tools:

### jekyll

Jekyll is a ruby gem that generates websites from markdown. To install it run:

    gem install jekyll

### ghp-import

ghp-import is a tool that will in a single step copy the contents of a
directory on the current branch into the gh-pages branch of a repository. To
install it run:

    pip install ghp-import

# Publishing the website

After making the desired changes you must build the website:

    jekyll build

If you would like to inspect the site prior to publishing you can run:

    jekyll serve

Once satisfied, ensure all outstanding changes are committed to your current
branch where the markdown sources live. Then use the ghp-import tool to publish
the site.

    ghp-import _site -pm "COMMIT MESSAGE"

---

Site theme originally based on
[jekyll-clean](https://github.com/scotte/jekyll-clean) by Scott
Emmons. jekyll-clean was released under the Creative Commons Attribution.
