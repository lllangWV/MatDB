import sys




import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(['git'] + command.split(), 
                                check=True, 
                                capture_output=True, 
                                text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return e.stderr
    
def bash_command(command):
    try:
        result = subprocess.run(command.split(), 
                                check=True, 
                                capture_output=True, 
                                text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return e.stderr



# def main(version, commit_log):
#     print(f"Current Version: {version}")
#     print("Commit Messages since the last version:")
#     print(commit_log)

if __name__ == "__main__":
    # Example usage:
    bash_command('git fetch --all --tags')
    current_version = bash_command('git tag -l --sort=v:refname')
    print(f"Current Version: {current_version}")

    commit_log=bash_command(f'git log --pretty=format:"%h-%s" {current_version}..')

    print("Commit Messages since the last version:")
    print(commit_log)