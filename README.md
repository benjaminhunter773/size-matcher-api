# Size Matcher API

The **Size Matcher API** is a Flask-based web application designed to help users find equivalent clothing sizes across various brands. By leveraging OpenAI's GPT-3.5 model, the API allows users to input their known size in one brand (e.g., "Nike Medium") and receive recommendations for equivalent sizes in another brand. This API is ideal for integration into e-commerce platforms, fashion websites, or mobile apps.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Endpoint: `/size-match`](#endpoint-size-match)
  - [Example Usage with `curl`](#example-usage-with-curl)
- [File Structure](#file-structure)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- **Cross-Brand Size Matching**: Converts clothing sizes across different brands based on user input.
- **Interactive Chat Interface**: A simple front-end chat interface allows users to interact with the API directly.
- **AI-Powered Responses**: Utilizes OpenAI’s GPT-3.5 model for intelligent and contextual size recommendations.
- **Easy Integration**: Can be deployed as an API and integrated into other applications or websites.

---

## Technologies Used

- **Python**: Programming language used for back-end logic.
- **Flask**: A lightweight framework to build and manage API routes and requests.
- **OpenAI API**: Used to access GPT-3.5 for size matching intelligence.
- **HTML/CSS/JavaScript**: Simple front-end technologies for the user interface.

---

## Requirements

To run this project, ensure you have:

1. **Python 3.x** installed.
2. An **OpenAI API Key** (Sign up at [OpenAI](https://platform.openai.com/) to get one).
3. Flask and OpenAI Python libraries (install using `requirements.txt`).

---

## Installation

### Step 1: Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/your-username/size-matcher-api.git
cd size-matcher-api


