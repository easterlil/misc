import os
import shutil
from huggingface_hub import hf_hub_download, login, logout
import subprocess

def create_directories():
    directories = ["/workspace/vocal_separator", "/workspace/vocal_separator/audio", "/workspace/vocal_separator/audio/input_audio", "/workspace/vocal_separator/audio/vocals_only", "/workspace/vocal_separator/audio/no_reverb", "/workspace/vocal_separator/audio/no_backing_vocals", "/workspace/vocal_separator/models"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def define_paths():
    separator_dir = "/workspace/vocal_separator"
    models_dir = os.path.join(separator_dir, "models")
    audio_dir = os.path.join(separator_dir, "audio")
    input_dir = os.path.join(audio_dir, "input_audio")
    vocals_dir = os.path.join(audio_dir, "vocals_only")
    no_reverb_dir = os.path.join(audio_dir, "no_reverb")
    no_backing_vocals_dir = os.path.join(audio_dir, "no_backing_vocals")
    return separator_dir, models_dir, audio_dir, input_dir, vocals_dir, no_reverb_dir, no_backing_vocals_dir

def get_hf_token():
    token = os.getenv('HF_TOKEN')
    if not token:
        token = input("Please enter your Hugging Face token: ")
        os.environ['HF_TOKEN'] = token
    return token

def download_files():
    hf_token = get_hf_token()
    os.chdir(separator_dir)
    subprocess.run([
        "wget", 
        "--header", f"Authorization: Bearer {hf_token}", 
        "https://huggingface.co/datasets/ronao/audio-sep-personal/resolve/main/files/stem_processor.py", 
        "-P", separator_dir
    ])
    subprocess.run([
        "wget", 
        "--header", f"Authorization: Bearer {hf_token}", 
        "https://huggingface.co/datasets/ronao/audio-sep-personal/resolve/main/files/requirements.txt", 
        "-P", separator_dir
    ])

def download_models():
    models = [
        "Kim_Vocal_2.onnx",
        "Reverb_HQ_By_FoxJoy.onnx",
        "UVR_MDXNET_KARA_2.onnx"
    ]
    
    base_url = "https://huggingface.co/seanghay/uvr_models/resolve/main/"

    for model in models:
        url = base_url + model
        destination = os.path.join(models_dir, model)
        os.system(f"wget {url} -O {destination}")
