import sys
import os
import subprocess
from pathlib import Path
import uuid
import torch

# Append the current directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_inference(
    model_path="./ckpts/zeroscope_v2_576w",
    checkpoint_folder="./ckpts/zeroscope_v2_576w-Ghibli-LoRA",
    prompt="Studio Ghibli style. Two women walk down coastal village path toward sea, passing colorful houses, sailboats visible.",
    negative_prompt="ugly, noise, fragment, blur, static video",
    width=256,
    height=256,
    num_frames=8,
    num_steps=30,
    guidance_scale=30.0,
    fps=8,
    lora_rank=32,
    lora_scale=0.7,
    noise_prior=0.1,
    device="cuda",
    seed=100
):
    print("Start Inference")
    output_dir = "apps/gradio_app/temp_data"
    os.makedirs(output_dir, exist_ok=True)

    # Get list of files in output_dir
    for file_name in os.listdir(output_dir):
        # Check if file ends with .mp4
        if file_name.endswith(".mp4"):
            # Remove the file
            os.remove(os.path.join(output_dir, file_name))

    command = [
        "python", "third_party/MotionDirector/main_inference.py",
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
        "--output_dir", output_dir,
        "--no-prompt-name"
    ]

    # Use Popen to execute the command
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # Line buffering
    )

    # Read output line-by-line in real-time
    output_lines = []
    try:
        for line in process.stdout:
            output_lines.append(line.strip())
    except Exception as e:
        return None, f"Error reading output: {str(e)}"

    # Capture stderr and wait for process to complete
    stderr_output = process.communicate()[1]
    if process.returncode != 0:
        return None, f"Error: {stderr_output.strip()}"

    # Check for MP4 files in output directory
    output_file = [f for f in os.listdir(output_dir) if f.lower().endswith('.mp4')]
    if output_file:
        output_path = os.path.join(output_dir, output_file[-1])
        if os.path.exists(output_path):
            return output_path, "\n".join(output_lines)
        else:
            return None, f"Video file not found at {output_path}\nLogs:\n" + "\n".join(output_lines)
    return None, f"No MP4 files found in {output_dir}\nLogs:\n" + "\n".join(output_lines)

if __name__ == "__main__":
    # Example usage
    video_path, logs = run_inference(device="cpu" if not torch.cuda.is_available() else "cuda")
    print(f"Generated Video: {video_path}")
    print(f"Logs: {logs}")