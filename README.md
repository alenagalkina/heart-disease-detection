# heart-disease-detection

[train_model.ipynb](./notebooks/train_model.ipynb) demonstrates training simple classification model for this dataset https://www.kaggle.com/ronitf/heart-disease-uci.

The aim is to create a FastAPI application for the classification model and deploy this application locally using Docker.

You can test get requests (example in [get_example.json](./data/get_example.json)) and get a response as a target variable (I used Postman).

Clone this repo and run the folliwong commands to start the application:

  `docker build . -t heart_disease_service`
  
  `docker run --rm -it -p 80:80 heart_disease_service`

## Technologies
- Python (pandas, sklearn)
- FastAPI
- Docker
- Postman
