import os

import requests
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='src', static_url_path='/')

# Replace 'YOUR_DEFAULT_API_KEY' with the name of the environment variable
#DEFAULT_API_KEY = os.environ.get('YOUR_DEFAULT_API_KEY', 'YOUR_DEFAULT_API_KEY')
DEFAULT_API_KEY = "";

@app.route('/')
def index():
    """Return the index.html page."""
    return app.send_static_file('index.html')


@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.json
    base64_image = data.get('image', '')
    api_key = data.get('key', DEFAULT_API_KEY)

    if base64_image:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What’s in this image? Be descriptive. For each significant item recognized, wrap this word in <b> tags. Example: The image shows a <b>man</b> in front of a neutral-colored <b>wall</b>. He has short hair, wears <b>glasses</b>, and is donning a pair of over-ear <b>headphones</b>. ... Also output an itemized list of objects recognized, wrapped in <br> and <b> tags with label <br><b>Objects:."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post(
            "https://flag.smarttrot.com/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            return jsonify({'error': 'Failed to process the image.'}), 500
        return response.content

    else:
        return jsonify({'error': 'No image data received.'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=51668,
            ssl_context=('/usr/local/nginx/cert/app.zhizengzeng.com.pem',
                         '/usr/local/nginx/cert/app.zhizengzeng.com.key'))
