📰 Fake News Headline Generator 📰

The Fake News Headline Generator is a fun Python project that uses a dataset of subjects, actions, objects, and places to generate random, humorous, and imaginative fake news headlines. This project is built with Streamlit to provide a simple and interactive web interface.

-> Features

Generates random fake headlines using a custom dataset (CSV).

Supports two formats of headlines:

- Subject + Action + Object

- Subject + Action + Place

Streamlit-powered UI with buttons to:

Generate a single headline.

Generate multiple headlines at once (configurable with a slider).

Lightweight and easy to run locally.

-> Tech Stack

Python 3

Streamlit – for the interactive UI.

CSV Dataset – for structured input data.

-> Dataset Format

The project expects a CSV file (Dataset_FNH.csv) with the following columns:

-subjects

- act_with_objects

- act_with_places

- objects

- places

Example row in the dataset:
A Bollywood Actor argues inside a local train at midnight

-> How to Run

- Install the required packages:

  pip install -r requirements.txt


- Run the Streamlit app:

  streamlit run aFake_News_Headlines.py


The app will open in your browser at:

http://localhost:8501

-> Use Cases

- Creative writing inspiration.

- Casual fun project for generating humorous fake headlines.

- Demonstration of random text generation and Streamlit UI development.

-> Future Improvements

- Add support for live “Breaking News” ticker-style output.

- Allow users to upload their own dataset via the UI.

- Improve grammar handling for more natural headlines.
