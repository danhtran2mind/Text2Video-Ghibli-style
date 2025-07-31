import os
import gradio as gr
from gradio_app.inference import run_inference, run_setup_script

def create_app():
    # Run setup script at startup
    setup_output = run_setup_script()
    # Load CSS file
    CSS = open("apps/gradio_app/static/styles.css", "r").read()
    
    with gr.Blocks(css=CSS) as app:
        gr.HTML('<script src="file=apps/gradio_app/static/scripts.js"></script>')
        gr.Markdown(
            """
            # Text to Video Ghibli style
            Generate videos using the `zeroscope_v2_576w` model with Studio Ghibli style LoRA.
            """
        )

        with gr.Row(elem_classes="row-container"):
            with gr.Column(elem_classes="column-container"):
                model_path = gr.Dropdown(
                    label="Base Model", 
                    choices=["./ckpts/zeroscope_v2_576w"],
                    value="./ckpts/zeroscope_v2_576w"
                )
                checkpoint_folder = gr.Dropdown(
                    label="LoRA folder", 
                    choices=["./ckpts/zeroscope_v2_576w-Ghibli-LoRA"],
                    value="./ckpts/zeroscope_v2_576w-Ghibli-LoRA"
                )
                prompt = gr.Textbox(
                    label="Prompt", 
                    value="Studio Ghibli style. Two women walk down coastal village path toward sea, passing colorful houses, sailboats visible."
                )
                negative_prompt = gr.Textbox(
                    label="Negative Prompt", 
                    value="ugly, noise, fragment, blur, static video"
                )
                
                # Video Dimensions & Timing
                with gr.Row(elem_classes="slider-row"):
                    with gr.Group(elem_classes="slider-group"):
                        gr.Markdown("### Video Dimensions & Timing")
                        width = gr.Slider(label="Width", minimum=256, maximum=1024, step=8, value=512)
                        height = gr.Slider(label="Height", minimum=256, maximum=1024, step=8, value=512)
                        num_frames = gr.Slider(label="Number of Frames", minimum=8, maximum=64, step=1, value=16)
                        fps = gr.Slider(label="FPS", minimum=10, maximum=60, step=1, value=16)
                        seed = gr.Number(label="Seed", value=100)
                
                generate_btn = gr.Button("Generate Video", elem_classes="generate-btn")

            with gr.Column(elem_classes="column-container"):
                video_output = gr.Video(label="Generated Video")
                log_output = gr.Textbox(label="Logs", lines=3, max_lines=20)
                
                # Model Parameters
                with gr.Row(elem_classes="slider-row"):
                    with gr.Group(elem_classes="slider-group"):
                        gr.Markdown("### Model Parameters")
                        num_steps = gr.Slider(label="Number of Steps", minimum=10, maximum=100, step=1, value=50)
                        guidance_scale = gr.Slider(label="Guidance Scale", minimum=1.0, maximum=50.0, step=0.1, value=30.0)
                        lora_rank = gr.Slider(label="LoRA Rank", minimum=16, maximum=128, step=8, value=96)
                        lora_scale = gr.Slider(label="LoRA Scale", minimum=0.1, maximum=1.0, step=0.1, value=0.7)
                        noise_prior = gr.Slider(label="Noise Prior", minimum=0.0, maximum=1.0, step=0.01, value=0.1)

        generate_btn.click(
            fn=run_inference,
            inputs=[
                model_path, checkpoint_folder, prompt, negative_prompt,
                width, height, num_frames, num_steps, guidance_scale,
                fps, lora_rank, lora_scale, noise_prior, seed
            ],
            outputs=[video_output, log_output]
        )

        # Example Videos Section
        gr.Markdown("## Example Videos")
        examples = []
        example_base_path = "apps/assets/examples/zeroscope_v2_576w-Ghibli-LoRA"
        for i in range(1, 5):
            example_dir = os.path.join(example_base_path, str(i))
            config_path = os.path.join(example_dir, "config.json")
            if os.path.exists(config_path):
                with open(config_path, "r") as f:
                    import json
                    config = json.load(f)
                video_path = os.path.join(example_dir, config["video"])
                if os.path.exists(video_path):
                    caption = f"Prompt: {config['prompt']}\n"
                    caption += f"Settings: {json.dumps({k: v for k, v in config.items() if k != 'video' and k != 'prompt'}, indent=2)}"
                    examples.append((video_path, caption))

        gr.Gallery(
            value=examples,
            label="Example Outputs",
            columns=2,
            height="auto",
            allow_preview=True,
            object_fit="contain"
        )

        gr.Markdown("""
                    This repository is trained from [![GitHub Repo](https://img.shields.io/badge/GitHub-danhtran2mind%2FMotionDirector-blue?style=flat)](https://github.com/danhtran2mind/MotionDirector), a fork of [![GitHub Repo](https://img.shields.io/badge/GitHub-showlab%2FMotionDirector-blue?style=flat)](https://github.com/showlab/MotionDirector), with numerous bug fixes and rewritten code for improved performance and stability.
                    """)
    return app

if __name__ == "__main__":
    app = create_app()
    app.launch()