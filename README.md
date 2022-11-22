[![<hajians>](https://circleci.com/gh/hajians/testing_exercises.svg?style=svg&circle-token=c808e77c338178a4eda399f2efe648a723b9c972)]()

# Requirments
In order to have a smooth workshop, please follow the instructions below and prepare your environment.

* Install `docker`, e.g., for Ubuntu follow instructions here https://docs.docker.com/engine/install/ubuntu/
* Install Anaconda3, e.g., follow instructions here https://www.anaconda.com/products/distribution#linux
* Create a `python3.8`:
    ```
     conda create python=3.8 -n MY_ENV_NAME 
    ```
    change `MY_ENV_NAME` to your desired name.
* Enter your environment using
    ```
    conda activate MY_ENV_NAME
    ```
* Install requirements
    ```
    pip install -r requirements.txt
    ```
* Run tests
    ```
    pytest -vv
    ```
    (First run might take some time, since it download a docker image for Postgres)