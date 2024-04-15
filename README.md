# How to create and activate python virtual environment.

- Navigate to your project directory

`cd path/to/your/project`

- Create a virtual environment named 'venv' (or any name you prefer)

`python -m venv test_env`

- Activate the virtual environment On Windows

`.\venv\Scripts\activate`

- Activate the virtual environment On macOS and Linux

`source venv/bin/activate`

## Your virtual environment is now active

## When you're done working in the virtual environment, deactivate it

`deactivate`

**Ensure your virtual environment is active then you can install dependencies**

## Recommend tools and libraries that can enhance the UI testing framework:

`pip install playwright`
`pip install pytest`

- to integrate Playwright more seamlessly with pytest, providing fixtures and test functions specifically tailored for Playwright. It simplifies the process of writing tests by managing browser contexts

`pip install pytest-playwright`

- for running tests in parallel, which can significantly reduce the time it takes to run extensive test suites.

`pip install pytest-xdist`

- generating HTML reports of your pytest test sessions.

`pip install pytest-html`

- For more comprehensive reporting

`pip install allure-pytest`

- maintain code quality by checking for style issues, programming errors, and other potential bugs in your Python scripts.

`pip install flake8`

**or**

`pip install pylint`

_#_ auto-formatters that help keep your codebase consistent

`pip install black`

## After you clone the project from : [GITHUB] (https://github.com/automagiq/Odessa_Auto)

- you can set up your own virtual environment and install the required dependencies by running

`python -m venv test_env`
`source test_env/bin/activate`
`pip install -r requirements.txt`
