# Shelfie

Shelfie is an application for tracking out-of-stock products on retail shelves. It utilizes a YOLO-based object detection model to monitor shelves in real time and logs the number of products that are out of stock. The app provides a web interface for easy tracking and management.

## Features

- Real-time shelf monitoring.
- Detection and logging of the number of out-of-stock products.
- Web interface to display stock status and log history.

## Model

The YOLO model was trained and fine-tuned to detect product stock status on shelves. You can find the model training process and experiment details in the following Google Colab link:

- [Model Training Colab](https://colab.research.google.com/drive/1q5XeDS474WXO92r_30IlxboLU39F4XqX?usp=sharing)
- [Uploaded Model](https://huggingface.co/wiwiewei18/smart-shelf-tracker)

## Dataset

The dataset used for training the model consists of labeled shelf images, capturing both stocked and out-of-stock conditions. You can access the dataset here:

- [Download Dataset](https://universe.roboflow.com/fyp-ormnr/supermarket-empty-shelf-detector)

## Installation

Follow the instructions below to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- pip

### Installation Guide

#### Windows

1. Clone the repository:

   ```bash
   git clone https://github.com/wiwiewei18/shelfie-smart-empty-shelf-tracker.git
   cd shelfie-smart-empty-shelf-tracker
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

#### macOS/Linux

1. Clone the repository:

   ```bash
   git clone https://github.com/wiwiewei18/shelfie-smart-empty-shelf-tracker.git
   cd shelfie
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. Start the web interface:

   ```bash
   streamlit run streamlit_app.py
   ```

2. Navigate to the provided local URL in your browser.

3. Use the camera feature to monitor shelves, and the app will automatically log the number of out-of-stock products.
