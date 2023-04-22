# Flask Web App

This is a simple Flask web app that retrieves and displays data from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API. The app has three routes:

1. `/`: Returns the "main page" of the app.
2. `/json`: Returns all the data from the JSONPlaceholder API in JSON format.
3. `/json/user/<user_id>`: Returns the data of a specific user ID from the JSONPlaceholder API in JSON format. <br>
If the user ID does not exist, it returns an error message.
4. Additionally, it has an error page that handles 404 errors.
<br>

# Running the app

## Runing the app locally:

1. Make sure you have Python 3.9 installed on your computer. You can download it from the [official website](https://www.python.org/downloads/).
2. Open a terminal or command prompt and navigate to the directory where the `flask-webapp.py` script is located.
3. Install the required dependencies by running the following command:  `pip install -r requirements.txt`
4. Run the script by running the following command: `python flask-webapp.py`
5. The Flask app should now be running on your local machine at `http://localhost:5000/`. You can access it using your web browser.
6. You can navigate bteween the app pages using the app routes. <br>
For example, the route `http://localhost:5000/json/user/1` will show you the data for the user whose ID number is 1.
6. To stop the app press `CTRL+C` in your local terminal.

## Building and Running the app using Docker Image

To build and run the Docker image for this web app, follow these steps:

1. Clone this Git repository to your local machine.
2. Navigate to the repository directory in your terminal.
3. Build the Docker image using the following command:  `docker build -t flask-web-app .`. <br>
This command will build a Docker image called `flask-web-app` using the Dockerfile in the repository directory.
4. Run the Docker container using the following command:  `docker run -p 5000:5000 flask-web-app`. <br>
This command will start a Docker container running the Flask web app, which is accessible at `http://localhost:5000`.


# Git repo Git-Actions Flow

This Git repository is configured with a Git Actions workflow that automatically builds and pushes a Docker image of the Flask web app to a Docker registry on each merge to the `main` branch. <br> 
The workflow is triggered by a `push` event to the `main` branch and has the following steps:

1. Checkout the code from the repository.
2. Build and tag the Docker image.
3. Log in to the Docker registry using the Docker username and password stored as secrets in the Git repository.
4. Push the Docker image to the Docker registry.

To use this Git Actions workflow, you will need to create a Docker registry and store the Docker username and password as secrets in your Git repository. <br>
You will also need to modify the workflow file to include the correct Docker registry URL and image tag. <br>
The workflow file is located in the `.github/workflows` directory of the Git repository.

Note: <br>
The docker images which will be created by GitHub action will have the following tag patteren: `yisca/flask-web-app:${git-action-run-number}`. <br>
Therefore, in order to use the image created by the git action, run number 11, you will need to run the following command: `docker run -p 5000:5000 yisca/flask-web-app:11`.