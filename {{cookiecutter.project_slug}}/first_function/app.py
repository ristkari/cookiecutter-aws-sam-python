import boto3
import json
{%- if cookiecutter.include_xray == "y" %}
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all 

patch_all()
{% endif -%}

session = boto3.Session()

{% if cookiecutter.include_xray == "y" %}
# Decorator for sync function
@xray_recorder.capture('## my_function')
def my_function():
    pass
{% endif %}

def lambda_handler(event, context):
{% if cookiecutter.include_apigw == "y" %}
    return {
        "statusCode": 200,
        "body": json.dumps({'hello': 'world'})
    }
{% else %}
    return {
        "hello": "world"
    }
{% endif %}
