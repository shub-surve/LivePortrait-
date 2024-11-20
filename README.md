

## **Project Overview**

The **Live Portrait Generator** is a web-based application that allows users to upload an image of a face, use a driving video, and generate a live portrait GIF using the Segmind API. The project integrates a Django backend to handle image uploads, process requests, and interact with the API.

---

## **Features**

1. **Image Upload**: Users can upload a face image via a user-friendly interface.
2. **GIF Generation**: The app uses the Segmind API to generate animated GIFs.
3. **Preview**: Uploaded images are previewed before submission.
4. **Downloadable Output**: Users can download the generated GIF.

---

## **Tech Stack**

1. **Frontend**: HTML, CSS, JavaScript
2. **Backend**: Django
3. **API**: Segmind Live Portrait API
4. **Testing**: Postman
5. **Storage**: Django's file storage system

---

## **System Requirements**

1. **Operating System**: Windows/Linux/Mac
2. **Python**: 3.8 or later
3. **Django**: 4.x or later
4. **Node.js** (for frontend dependencies, optional)

---

## **Installation and Setup**

### **Step 1: Clone the Repository**
```bash
git clone <repository_url>
cd live_portrait
```

### **Step 2: Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Set Up Django**
1. Migrate the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

### **Step 4: Configure API Key**
Add your Segmind API key in the `settings.py` file or create an `.env` file:
```python
SEGMIND_API_KEY = "YOUR_SEGMIND_API_KEY"
```

### **Step 5: Run the Server**
```bash
python manage.py runserver
```
Access the app at: `http://127.0.0.1:8000/`

---

## **Usage Instructions**

1. Open the app in a web browser.
2. Upload a face image.
3. Click "Generate GIF" to start the process.
4. View the result in the output section and download the GIF.

---

## **Django Backend Architecture**

### **1. URL Configuration**
- `/generate-gif/`: Endpoint to handle image uploads and GIF generation.

### **2. File Upload Handling**
- Uploaded images are saved temporarily in the `media/` directory for processing.

### **3. API Integration**
- The backend sends a POST request to the Segmind API with the following payload:
  ```json
  {
    "face_image": "<base64-encoded image>",
    "driving_video": "<driving video URL>",
    "live_portrait_dsize": 512
  }
  ```

### **4. Response Handling**
- On success: The API responds with a `gif_url`, which is displayed to the user.
- On failure: The backend returns an error message.

---

## **Testing**

### **Postman Setup**
1. **Endpoint**: `http://127.0.0.1:8000/generate-gif/`
2. **Method**: POST
3. **Headers**:
   - Content-Type: `multipart/form-data`
4. **Body**:
   - Key: `image` (Type: File)
   - Value: Upload an image file.

---

## **Screenshots**

![image](https://github.com/user-attachments/assets/1bc78580-c0be-46c1-a8c1-05624e3a1b64)
![image](https://github.com/user-attachments/assets/21d31557-3577-47e3-a539-b2b1d2010e90)



---

## **Known Issues**
1. Large images might take longer to process.
2. Ensure driving video URLs are valid.

---

## **Future Enhancements**
1. Allow users to upload custom driving videos.
2. Improve responsiveness for mobile devices.
3. Add more animation options.

---

## **Contact**
- **Developer**: Shubham Vinod Surve
- **Email**: [Shubhamsurve30803@gmail.com](mailto:Shubhamsurve30803@gmail.com)

---

Let me know if you need help refining this further!
