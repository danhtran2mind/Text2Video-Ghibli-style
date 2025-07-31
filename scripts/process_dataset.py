import os
import shutil
import random
import argparse
from huggingface_hub import snapshot_download
import zipfile

def copy_file_pairs(source_dir, dest_dir, max_pairs=20, seed=None):
    if seed is not None:
        random.seed(seed)
    os.makedirs(dest_dir, exist_ok=True)
    mp4_files = [f for f in os.listdir(source_dir) if f.endswith('.mp4')]
    selected_mp4_files = random.sample(mp4_files, min(len(mp4_files), max_pairs))
    for mp4 in selected_mp4_files:
        base = os.path.splitext(mp4)[0]
        txt = f"{base}.txt"
        if os.path.exists(os.path.join(source_dir, txt)):
            shutil.copy2(os.path.join(source_dir, mp4), os.path.join(dest_dir, mp4))
            shutil.copy2(os.path.join(source_dir, txt), os.path.join(dest_dir, txt))
    return len(selected_mp4_files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Studio Ghibli dataset by downloading, extracting, and copying file pairs.")
    parser.add_argument("--source_dir", default="data/ghibli/raw/videos/1920x1040", help="Source directory containing video and text files")
    parser.add_argument("--dest_dir", default="data/ghibli/videos", help="Destination directory for copied file pairs")
    parser.add_argument("--max_pairs", type=int, default=240, help="Maximum number of file pairs to copy")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--repo_id", default="raymondt/ghibi_t2v", help="Hugging Face dataset repository ID")
    parser.add_argument("--local_dir", default="data/ghibli/raw", help="Local directory to download the dataset")
    parser.add_argument("--zip_path", default="data/ghibli/raw/studio_ghibli_wan14b_t2v_v01_dataset.zip", help="Path to the downloaded zip file")
    
    args = parser.parse_args()

    # Create directory if it doesn't exist
    os.makedirs(args.local_dir, exist_ok=True)

    # Download the dataset using snapshot_download
    snapshot_download(repo_id=args.repo_id, 
                     local_dir=args.local_dir, 
                     repo_type="dataset")

    # Unzip the dataset
    with zipfile.ZipFile(args.zip_path, 'r') as zip_ref:
        zip_ref.extractall(args.local_dir)

    # Copy file pairs
    copied = copy_file_pairs(args.source_dir, args.dest_dir, max_pairs=args.max_pairs, seed=args.seed)
    print(f"Copied {copied} pairs to {args.dest_dir}")