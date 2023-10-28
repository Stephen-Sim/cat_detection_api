# Cat Detection API using MobileNetV2

This is a simple Flask-based API that uses the MobileNetV2 pre-trained model to determine whether an input image contains a cat or not. It provides a straightforward and easy-to-use endpoint for cat detection.

## How it Works

1. The API listens on the `/predict` endpoint for POST requests.
2. The client sends a JSON payload with a base64-encoded image to be analyzed.
3. The API decodes the base64 image data and processes it using the MobileNetV2 model.
4. If the model predicts the presence of a cat (specifically, a "tabby" or "tiger cat"), it returns `true`. Otherwise, it returns `false`.
5. Any errors that occur during the process are also handled and appropriate responses are sent back to the client.

## API Endpoints

### 1. `POST /predict`

- **Request**: This endpoint expects a POST request with a JSON payload containing the base64-encoded image data.
- **Response**: The API will respond with a JSON object containing the result of the cat detection.

### 2. `GET /`

- **Request**: A simple GET request to test the API.
- **Response**: The API will respond with the message "Cat Detection API."

## Installation

Before running the application, you need to install the necessary dependencies. Here are the steps:

1. Ensure that you have Python 3.11.6 installed on your machine.

2. Clone the repository.

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This command will read the `requirements.txt` file and install all the listed packages. Please make sure you have this file in your current directory before running the command.

4. After successful installation of the dependencies, you can run the application:

```bash
python app.py
```

The API will start running locally on your computer, and you can access it at `http://localhost:5000`.

## Example Usage

You can use any API testing tool, such as `curl` or Postman, to test the API. Here's an example of how to use `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"image": "base64_encoded_image_data"}' http://localhost:5000/predict
```

Replace `"base64_encoded_image_data"` with the actual base64-encoded image data.

## Important Notes

1. This example uses the MobileNetV2 model for simplicity. For more accurate and specialized image classification tasks, you may want to consider training your own model or using a more advanced pre-trained model.

2. Ensure that you have the necessary libraries and dependencies installed, as specified in the code.

3. This is a basic example for educational purposes and may require improvements for production use, such as error handling and scalability.

4. Be aware of potential security risks related to handling image data from untrusted sources, especially in a production environment.

5. Always follow best practices for deploying Flask applications, such as using a production-ready web server like Gunicorn.

Feel free to modify and extend this API to suit your specific use case or integrate it into your own applications.

## License
This project is licensed under the MIT License - see the LICENSE file for details.