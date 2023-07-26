# Data Engineer Study Case

This project implements an intelligent system designed to gather, process, and provide insights about a company based on the information available on its website. It employs web scraping, data storage, data processing, and AI-powered analysis techniques to deliver comprehensive information about a company in a question-answer chatbot format.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Project Structure](#project-structure)

## Introduction

This project's main goal is to create a deep and automated understanding of a company's brand, style, and voice through their website content. It involves multiple steps such as web scraping using Scrapy, data storage in MinIO and MongoDB, data processing using Natural Language Processing techniques, and interacting with the chatbot interface via Gradio. It also uses the power of OpenAI's API to provide the chatbot with the ability to answer questions about the company.

## Getting Started

### Prerequisites

- Python 3.9 or later
- Poetry
- Docker
- A OpenAI API Key

### Installation

1. Clone the repo: `git clone https://github.com/allegretti-felipe/de-study-case.git`
2. Enter the project's Poetry shell: `poetry shell`
3. Install Python packages: `poetry install`
4. Create a new `.env` file: `cp .env.example .env`
5. Set up your environment variables for the OpenAI API Key in `.env`
6. (optional) Change the crawler settings as necessary in `crawler/settings.py`

### Running for Superside

Scrape data from website
````bash
scrapy crawl Superside
````

Proccess the data and load to MongoDB
````bash
python processing/superside.py --full-load --debug
````

Start the chatbot
````bash
python chatbot/chatbot.py -- Superside
````


## Project Structure

- `aws/`: Contains utility scripts to interact with AWS S3.
- `chatbot/`: Contains scripts for the chatbot interface and its integration with the OpenAI API.
- `crawler/`: Contains the Scrapy spider used for web scraping.
- `processing/`: Contains scripts for processing and cleaning the scraped data.
- `tests/`: Contains the project's unit tests.
