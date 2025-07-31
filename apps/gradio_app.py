import gradio as gr
from apps.gradio_app.inference import run_inference, run_setup_script

def create_app():
    # Run setup script at startup
    setup_output = run_setup_script()
    
    with gr.Blocks(css="static/styles.css", js="static/scripts.js") as app:
        gr.Markdown(
            """
            # MotionDirector Video Generation
            Generate high-quality videos using the MotionDirector model with Studio Ghibli style LoRA.
            """
        )
        # Display setup script output
        gr.Markdown(f"**Setup Script Output:** {setup_output}")

        with gr.Row():
            with gr.Column(scale=1):
                model_path = gr.Textbox(label="Model Path", value="./ckpts/zeroscope_v2_576w")
                checkpoint_folder = gr.Textbox(label="Checkpoint Folder", value="./ckpts/zeroscope_v2_576w-Ghibli-LoRA")
                prompt = gr.Textbox(label="Prompt", value="Studio Ghibli style. Two women walk down coastal village path toward sea, passing colorful houses, sailboats visible.")
                negative_prompt = gr.Textbox(label="Negative Prompt", value="ugly, noise, fragment, blur, static video")
                width = gr.Slider(label="Width", minimum=256, maximum=1024, step=8, value=512)
                height = gr.Slider(label="Height", minimum=256, maximum=1024, step=8, value=512)
                num_frames = gr.Slider(label="Number of Frames", minimum=8, maximum=64, step=1, value=16)
                num_steps = gr.Slider(label="Number of Steps", minimum=10, maximum=100, step=1, value=50)
                guidance_scale = gr.Slider(label="Guidance Scale", minimum=1.0, maximum=50.0, step=0.1, value=30.0)
                fps = gr.Slider(label="FPS", minimum=10, maximum=60, step=1, value=16)
                lora_rank = gr.Slider(label="LoRA Rank", minimum=16, maximum=128, step=8, value=96)
                lora_scale = gr.Slider(label="LoRA Scale", minimum=0.1, maximum=1.0, step=0.1, value=0.7)
                noise_prior = gr.Slider(label="Noise Prior", minimum=0.0, maximum=1.0, step=0.01, value=0.1)
                device = gr.Dropdown(label="Device", choices=["cuda", "cpu"], value="cuda")
                seed = gr.Number(label="Seed", value=100)
                generate_btn = gr.Button("Generate Video", elem_classes="generate-btn")

            with gr.Column(scale=1):
                video_output = gr.Video(label="Generated Video")
                log_output = gr.Textbox(label="Logs", lines=10, max_lines=20)

        generate_btn.click(
            fn=run_inference,
            inputs=[
                model_path, checkpoint_folder, prompt, negative_prompt,
                width, height, num_frames, num_steps, guidance_scale,
                fps, lora_rank, lora_scale, noise_prior, device, seed
            ],
            outputs=[video_output, log_output]
        )

    return app

if __name__ == "__main__":
    app = create_app()
    app.launch()