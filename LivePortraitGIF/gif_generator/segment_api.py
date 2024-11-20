import requests
import base64


def image_file_to_base64(image_path):
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        return base64.b64encode(image_data).decode('utf-8')
    except FileNotFoundError:
        raise ValueError(f"File at {image_path} not found.")


def image_url_to_base64(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        return base64.b64encode(image_data).decode('utf-8')
    else:
        raise ValueError(f"Failed to fetch image from URL: {image_url}")


def generate_live_portrait(face_image_path, driving_video_url, api_key):
    url = "https://api.segmind.com/v1/live-portrait"

  
    data = {
        "face_image": image_file_to_base64(face_image_path),
        "driving_video": driving_video_url,
        "live_portrait_dsize": 512,
        "live_portrait_scale": 2.3,
        "video_frame_load_cap": 128,
        "live_portrait_lip_zero": True,
        "live_portrait_relative": True,
        "live_portrait_vx_ratio": 0,
        "live_portrait_vy_ratio": -0.12,
        "live_portrait_stitching": True,
        "video_select_every_n_frames": 1,
        "live_portrait_eye_retargeting": False,
        "live_portrait_lip_retargeting": False,
        "live_portrait_lip_retargeting_multiplier": 1,
        "live_portrait_eyes_retargeting_multiplier": 1
    }

    headers = {'x-api-key': api_key}

 
    response = requests.post(url, json=data, headers=headers)


    if response.status_code == 200:
        return response.json() 
    else:
        raise ValueError(f"API Request failed with status code {response.status_code}: {response.text}")
