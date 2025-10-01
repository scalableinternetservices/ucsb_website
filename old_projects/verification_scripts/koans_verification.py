import os
import re
import subprocess
import sys
import urllib.parse

# Given the path to a directroy in a github repository, return the path used to clone the repository
# Example:
# Input: "https://github.com/huangderful/CS291a-project1/tree/main"
# Output: "https://github.com/huangderful/CS291a-project1"
def clone_path(url):
    if url.endswith('/tree/main'):
        url = url.replace('/tree/main', '')
    parsed_url = urllib.parse.urlparse(url)
    repo_path = parsed_url.path
    github_user = repo_path.split('/')[1]
    repo_name = repo_path.split('/')[2]
    return f"{parsed_url.scheme}://{parsed_url.netloc}/{github_user}/{repo_name}"


def clone_repo(url, path):
    return os.system(f"git clone {url} {path}")

# cd into the directory and run the ruby koans
# return the numbe of tests passed and number of tests remaining
# return to the original directory
def run_ruby_koans(path):
    try:
        original_path = os.getcwd()
        os.chdir(path)
        # Find the location of path_to_enlightenment.rb
        koans_root = None
        for root, dirs, files in os.walk(path):
            if "path_to_enlightenment.rb" in files:
                koans_root = root
                break
        os.chdir(koans_root)
        # dir_contents = os.listdir(path)
        # for item in ['.git', 'README.md']:
        #     if item in dir_contents:
        #         dir_contents.remove(item)
        # if len(dir_contents) == 1:
        #     os.chdir(dir_contents[0])
        result = subprocess.run(["rake"], capture_output=True, text=True)
        output = result.stdout
        # Parse the output of the koans and return the number of tests passed and the number of tests remaining
        # Example output: "your path thus far [.X________________________________________________] 3/284 (1%)"
        if "Mountains are again merely mountains" in output:
            return 100
        pct_complete = re.search(r"\((\d+)%\)", output).group(1)
        return int(pct_complete)
    finally:
        os.chdir(original_path)


if __name__ == "__main__":
    path = sys.argv[1]
    input_path = os.path.join(path, "submissions.csv")
    results = {}
    with open(input_path, 'r') as submissions:
        for submission in submissions:
            email,repo = submission.split(',')
            user_path = os.path.join(path, email)
            os.mkdir(user_path)
            git_repo_path = clone_path(repo)
            if clone_repo(git_repo_path, user_path):
                results[email] = "Error cloning repository"
                continue
            try:
                pct_complete = run_ruby_koans(user_path)
                results[email] = pct_complete
            except Exception as e:
                results[email] = f"Error running koans: {e}"
                continue
    print(results)
    # write a csv file with the results
    output_path = os.path.join(path, "results.csv")
    with open(output_path, 'w') as results_file:
        for email, result in results.items():
            results_file.write(f"{email},{result}\n")

