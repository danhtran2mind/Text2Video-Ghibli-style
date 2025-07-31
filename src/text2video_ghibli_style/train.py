import subprocess
import os
import argparse

def run_training(config_path, pytorch_cuda_alloc_conf="expandable_segments:True"):
    # Set the environment variable
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = pytorch_cuda_alloc_conf
    
    # Command to execute
    command = ["python", "main_train.py", "--config", config_path]
    
    try:
        # Run the command using subprocess.Popen
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy()
        )
        
        # Stream output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                
        # Get any remaining output and errors
        stdout, stderr = process.communicate()
        
        # Print any errors
        if stderr:
            print("Errors:", stderr)
            
        # Check the return code
        if process.returncode == 0:
            print("Training completed successfully")
        else:
            print(f"Training failed with return code: {process.returncode}")
            
    except subprocess.SubprocessError as e:
        print(f"Error running training: {e}")
    except FileNotFoundError:
        print("Error: main_train.py or config file not found")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run training script with specified config")
    parser.add_argument(
        "--config",
        type=str,
        default="./configs/config_multi_videos.yaml",
        help="Path to the config file"
    )
    parser.add_argument(
        "--pytorch-cuda-alloc",
        type=str,
        default="expandable_segments:True",
        help="Value for PYTORCH_CUDA_ALLOC_CONF environment variable"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run training with provided arguments
    run_training(args.config, args.pytorch_cuda_alloc)