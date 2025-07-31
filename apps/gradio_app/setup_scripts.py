import os
import sys
import subprocess
from pathlib import Path
import uuid

# Append the current directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_setup_script():
    setup_script = os.path.join(os.path.dirname(__file__), "setup_scripts.py")
    try:
        result = subprocess.run(["python", setup_script], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Setup script failed: {e.stderr}"

def run_inference(
    model_path="./ckpts/zeroscope_v2_576w",
    checkpoint_folder="./ckpts/zeroscope_v2_576w-Ghibli-LoRA",
    prompt="Studio Ghibli style. Two women walk down coastal village path toward sea, passing colorful houses, sailboats visible.",
    negative_prompt="ugly, noise, fragment, blur, static video",
    width=512,
    height=512,
    num_frames=16,
    num_steps=50,
    guidance_scale=30.0,
    fps=16,
    lora_rank=96,
    lora_scale=0.7,
    noise_prior=0.1,
    device="cuda",
    seed=100
):
    output_dir = "apps/gradi_app/temp_data"
    os.makedirs(output_dir, exist_ok=True)

    command = [
        "python", "src/third_party/MotionDirector/main_inference.py",
        "--model", model_path,
        "--checkpoint_folder", checkpoint_folder,
        "--prompt", prompt,
        "--negative-prompt", negative_prompt,
        "--width", str(width),
        "--height", str(height),
        "--num-frames", str(num_frames),
        "--num-steps", str(num_steps),
        "--guidance-scale", str(guidance_scale),
        "--fps", str(fps),
        "--lora_rank", str(lora_rank),
        "--lora_scale", str(lora_scale),
        "--noise_prior", str(noise_prior),
        "--device", device,
        "--seed", str(seed),
        "--out_dir", output_dir,
        "--no_prompt_name"
    ]

    output_file = [f for f in os.listdir(output_dir) if f.lower().endswith('.mp4')]
    print(os.path.join(output_dir, output_file[0]) if output_file else "No MP4 files found.")

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return str(output_file), result.stdout
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.stderr}"