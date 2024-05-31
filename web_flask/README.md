# AirBnB clone - Web framework

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Project Description

The **AirBnB clone - Web framework** project is part of the ALX Software Engineering curriculum. This project is an extension of the AirBnB clone series, focusing on the development of a web framework to handle dynamic content, templating, and routing. The goal is to create a simple yet functional web framework that mimics some of the features of popular web frameworks like Flask.

## Features

- **Dynamic Content Rendering:** Utilize Jinja2 templating to render dynamic HTML pages.
- **Routing System:** Handle HTTP requests with a custom routing system.
- **Static File Serving:** Serve static files such as CSS, JavaScript, and images.
- **Error Handling:** Custom error pages for common HTTP errors.
- **Template Inheritance:** Use Jinja2 template inheritance for modular and maintainable templates.

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Clone the Repository

```sh
git clone https://github.com/yourusername/AirBnB_clone_web_framework.git
cd AirBnB_clone_web_framework
```

### Create a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

#### Requirements.txt:

- Flask==2.0.2
- SQLAlchemy==1.4.31
- Jinja2==3.0.2
- Werkzeug==2.0.2
- mysql-connector-python==8.0.28

## Usage

### Running the Development Server

```sh
python3 -m app
```

Navigate to http://127.0.0.1:5000 in your web browser to see the application running.

## Routes

The web framework handles various routes. Below is a list of available routes and their functionalities:

- '/': Home page
- '/hbnb': AirBnB clone page
- '/hbnb/<dynamic>': Dynamic page rendering based on URL parameters
- '/static/<path:filename>': Serve static files

### Example Routes

- 'GET /' - Renders the home page.
- 'GET /hbnb' - Renders the AirBnB clone page.
- 'GET /hbnb/<dynamic>' - Renders pages dynamically based on the URL parameter <dynamic>.

## Tests

### Running Tests

To run the tests, use the following command:

```sh
python3 -m unittest discover tests
```

The tests cover various aspects of the web framework, including route handling, template rendering, and static file serving.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.

## Authors

Naoufal Hadra - Initial work - Naoufalhdr

Feel free to customize the `Authors` and `Contributing` sections according to your project's specifics. Additionally, if you have a license file or more detailed contribution guidelines, ensure they are included in the repository.
