import sys

def main(version, commit_log):
    print(f"Current Version: {version}")
    print("Commit Messages since the last version:")
    print(commit_log)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <version> <commit_log>")
        sys.exit(1)
    
    version = sys.argv[1]
    commit_log = sys.argv[2]
    main(version, commit_log)