import os
import subprocess
import argparse
import sys

def clone_repository(repo_url, target_dir, branch="main"):
    """Clone a git repository to the specified directory with specific branch."""
    if os.path.exists(target_dir):
        print(f"Directory {target_dir} already exists. Skipping clone.")
        return
    
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    
    try:
        subprocess.run(
            ["git", "clone", "-b", branch, repo_url, target_dir],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully cloned {repo_url} (branch: {branch}) to {target_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e.stderr}")
        sys.exit(1)

def main(motiondirector_url="https://github.com/danhtran2mind/MotionDirector", branch="main"):
    # Define target directory
    target_dir = os.path.join("src", "third_party", "MotionDirector")
    
    # Clone MotionDirector repository
    clone_repository(motiondirector_url, target_dir, branch)

if __name__ == "__main__":
    # Set arguments directly
    main(
        motiondirector_url="https://github.com/danhtran2mind/MotionDirector",
        branch="main"
    )