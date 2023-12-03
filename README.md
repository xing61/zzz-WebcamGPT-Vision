Demo体验，简单两步：<br>
第1步：用手机号登录智增增，获取复制出key，地址：http://gpt.zhizengzeng.com/#/login <br>
第2步：打开：https://app.zhizengzeng.com:51668/, 将上一步复制的key填入，即可正常使用。 <br>
![image](https://github.com/xing61/zzz-WebcamGPT-Vision/assets/38256442/a96fa31c-908d-4a48-ab31-e46705a0f4b1)

# WebcamGPT-Vision

WebcamGPT-Vision is a lightweight web application that enables users to process images from their webcam using OpenAI's GPT-4 Vision API. The application captures images from the user's webcam, sends them to the GPT-4 Vision API, and displays the descriptive results. 

There are three versions of this project: PHP, Node.js, and Python / Flask.

https://github.com/bdekraker/WebcamGPT-Vision/assets/81277770/9e5ed14b-bb8e-4475-9921-471b9d42d009

## Features

- Webcam integration for live image capture.
- Processing of images with OpenAI's GPT-4 Vision API.
- Display of AI-generated image descriptions.
- Simple and intuitive user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a modern web browser.
- For the PHP version: You have a server with PHP support and cURL enabled.
- For the Node.js version: You have Node.js and npm installed.
- For the Python/Flask version: You have Python and Flask installed.
- You have obtained an API key from OpenAI for GPT-4 Vision API usage.

## Installation

To install WebcamGPT-Vision, follow these steps for the correct version (all are included):

### PHP Version

1. Clone the repository to your local machine or server:
   ```sh
   git clone https://github.com/bdekraker/webcamgpt-vision.git
   ```
2. Navigate to the `php-version` directory.
3. Replace `YOUR_DEFAULT_API_KEY` in the `process_image.php` file with your actual OpenAI API key.
4. Upload the code to your PHP-enabled server.
5. Open the `index.html` in your web browser to start using the application.

### Node.js Version

1. Clone the repository:
   ```sh
   git clone https://github.com/bdekraker/webcamgpt-vision.git
   ```
2. Navigate to the `js-version` directory.
3. Run `npm install` to install the dependencies.
4. Create a `.env` file in the root of `js-version` directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=YOUR_DEFAULT_API_KEY
   ```
5. Start the server with `node server.js`.
6. Access the application through your web browser at `http://localhost:3000` (or the port you configured).

   
### Python/Flask Version

1. Clone the repository:
   ```sh
   git clone https://github.com/bdekraker/webcamgpt-vision.git
   ```
2. Navigate to the `python-version` directory.
3. Run `pip install -r requirements.txt` to install the dependencies.
4. Set your OpenAI API key as an environment variable:
   ```sh
   export YOUR_DEFAULT_API_KEY='your_actual_api_key_here'
   ```
5. Start the Flask server with `python process_image.py`.
6. Access the application through your web browser at `http://localhost:5000`.

## Usage

For both versions, the usage is as follows:

1. Ensure that you have a working webcam connected and allowed for use by the browser.
2. Open the `index.html` page in your web browser.
3. Click the "Capture" button to take a snapshot from your webcam.
4. The application will process the image and display the description below the webcam feed.

## Contributing

Contributions to WebcamGPT-Vision are welcome. Please adhere to the following guidelines:

- Fork the repository and create a new branch for your feature or fix.
- Write clear and concise commit messages.
- Ensure your code adheres to the existing style.
- Open a pull request with a detailed description of your changes.

## Support

If you have any questions or feedback, please open an issue in the repository, and a maintainer will get back to you.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the `LICENSE.md` file for details.

## Acknowledgements

- Thanks to OpenAI for providing the GPT-4 Vision API.
- This project was inspired by the capabilities of AI in image processing and understanding.

## Contact

If you need to contact the maintainer of this project, please reach out to [Benjamin De Kraker](https://twitter.com/BenjaminDEKR).

## Disclaimer

This application is not affiliated with OpenAI, and the GPT-4 Vision API usage is subject to OpenAI's terms and conditions. Ensure that you follow OpenAI's usage guidelines and have appropriate permissions to use the API.
