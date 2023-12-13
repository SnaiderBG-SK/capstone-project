
# Task Summarizer and Breakdown App

## Overview
Task Summarizer and Breakdown App is a Python application designed to interact with the OpenAI GPT model. It takes a task description as input, summarizes it into a concise title (no more than 8 words), and breaks it down into simpler, actionable sub-tasks. This tool aims to streamline project management and task delegation processes.

## Features
- **Task Summarization**: Condenses detailed task descriptions into brief, manageable titles.
- **Task Breakdown**: Splits complex tasks into smaller, more manageable sub-tasks.
- **OpenAI GPT Integration**: Leverages the advanced natural language processing capabilities of OpenAI's GPT models.
- **User-Friendly Interface**: Simple and intuitive UI for easy interaction.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or later installed on your system.
- An active OpenAI API key.

## Installation
To install Task Summarizer and Breakdown App, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-summarizer-and-breakdown-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd task-summarizer-and-breakdown-app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `.env` file in the root of your project.
2. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Ensure `.env` is listed in your `.gitignore` file to keep your API key secure.

## Usage
To use Task Summarizer and Breakdown App, follow these steps:

1. Run the application:
   ```bash
   python main.py
   ```
2. Enter your task description in the provided text field.
3. Click the "Submit" button to receive the summarized task and its breakdown.

## Contributing to Task Summarizer and Breakdown App
To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors
Thanks to the following people who have contributed to this project:

- [@Snaider-BG-SK](https://github.com/Snaider-BG-SK)

## Contact
If you want to contact me, you can reach me at `<sny.abg@gmail.com>`.

## License
This project uses the following license: [MIT License](<link-to-license>).
