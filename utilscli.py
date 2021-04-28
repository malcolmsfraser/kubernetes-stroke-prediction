#!/usr/bin/env python
import click
import mlib
import json
import requests
from predict import create_payload

@click.group()
@click.version_option("1.0")
def cli():
    """Machine Learning Utility Belt"""


@cli.command("retrain")
@click.option("--tsize", default=0.1, help="Test Size")
def retrain(tsize):
    """
    Retrain Model
    """

    click.echo(click.style("Retraining Model", bg="green", fg="white"))
    accuracy, model_name = mlib.retrain(tsize=tsize)
    click.echo(
        click.style(f"Retrained Model Accuracy: {accuracy}", bg="blue", fg="white")
    )
    click.echo(click.style(f"Retrained Model Name: {model_name}", bg="red", fg="white"))


@cli.command("predict")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")
def mkrequest(host):
    """
    Prompt user to patient info to create payload
    Sends payload to ML Endpoint for prediction
    """
    
    payload = create_payload()
    click.echo(click.style(f"Querying host {host+'/predict'} with payload: \n{payload}",
        bg="green", fg="white"))
    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"Predicted probability of patient stroke: {result.text}", bg="red", fg="white"))

@cli.command("payload-predict")
@click.option("--payload", default="payload.json", help="json payload")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")
def mk_payloadrequest(payload, host):
    """
    Sends preformatted json payload to ML Endpoint for prediction
    """
    
    inputs = ['age','hypertension','heart_disease','avg_glucose_level', 'bmi',
    'gender_Female', 'gender_Male', 'gender_Other',
    'ever_married_No','ever_married_Yes',
    'work_type_Govt_job','work_type_Never_worked','work_type_Private','work_type_Self-employed','work_type_children',
    'Residence_type_Rural','Residence_type_Urban',
    'smoking_status_Unknown','smoking_status_formerly smoked','smoking_status_never smoked','smoking_status_smokes']
    
    with open(payload) as f:
        payload = json.load(f)
    if all([x in payload for x in inputs]):
        click.echo(click.style(f"Querying host {host+'/predict'} with payload: \n{payload}",
            bg="green", fg="white"))
        result = requests.post(url=host, json=payload)
        click.echo(click.style(f"Predicted probability of patient stroke: {result.text}", bg="red", fg="white"))
    else: 
        click.echo(click.style("Incorrect or Empty Payload", bg="red", fg="white"))


if __name__ == "__main__":
    cli()
