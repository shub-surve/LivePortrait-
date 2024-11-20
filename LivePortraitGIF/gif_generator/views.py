import os
import logging
import base64
import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from PIL import Image

# Create a logger
logger = logging.getLogger(__name__)

def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES['image']
        return generate_gif(request, uploaded_file)  # Pass the uploaded file directly
    return render(request, 'upload.html')

def create_animated_gif(images):
    gif_path = os.path.join(settings.MEDIA_ROOT, 'gifs', 'generated.gif')
    os.makedirs(os.path.dirname(gif_path), exist_ok=True)
    images[0].save(gif_path, save_all=True, append_images=images[1:], loop=0, duration=100)
    return gif_path

def generate_gif(request):
    try:
        uploaded_file = request.FILES.get('image')
        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        images = []
        img = Image.open(uploaded_file)
        for i in range(10):  # Create 10 frames for demonstration
            img_frame = img.copy()
            img_frame = img_frame.rotate(i * 10)  # Rotate the image for each frame
            images.append(img_frame)

        # Create the animated GIF
        gif_path = create_animated_gif(images)

        # Return the URL of the generated GIF
        gif_url = os.path.join(settings.MEDIA_URL, 'gifs', 'generated.gif')
        
        # Optionally, send the GIF to the external API
        api_response = send_to_api(gif_path)

        return JsonResponse({
            'message': 'GIF generated successfully!',
            'gif_url': gif_url,
            'api_response': api_response  # This can now safely include base64 content
        }, status=200)
    except Exception as e:
        logger.exception("Exception occurred: %s", str(e))
        return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
import base64

def send_to_api(gif_path):
    api_key = "SG_efd201000bc39364"
    url = "https://api.segmind.com/v1/live-portrait"

    # Convert the GIF to base64
    gif_base64 = image_file_to_base64(gif_path)

    # Request payload
    data = {
        "face_image": gif_base64,  # Use the generated GIF
        "driving_video": "https://segmind-sd-models.s3.amazonaws.com/display_images/liveportrait-video.mp4",
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

    # Log the response status code and content type
    logger.info(f"API Response Status Code: {response.status_code}")
    logger.info(f"API Response Content Type: {response.headers.get('Content-Type')}")

    try:
       
        if response.headers.get('Content-Type') == 'application/json':
            return response.json()  
        else:
          
            return {
                'error': 'Invalid response from API',
                'content': base64.b64encode(response.content).decode('utf-8')  # Encode bytes to base64 string
            }
    except ValueError:
        logger.error("Failed to decode JSON from API response")
        return {'error': 'Failed to decode JSON', 'content': base64.b64encode(response.content).decode('utf-8')}
def image_file_to_base64(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return base64.b64encode(image_data).decode('utf-8')