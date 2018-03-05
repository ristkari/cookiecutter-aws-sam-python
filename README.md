# Cookiecutter SAM for Python Lambda functions

A cookiecutter template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.6

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter` or `brew install cookiecutter` using Homebrew

## Usage

Generate a new SAM based Serverless App: `cookiecutter gh:heitorlessa/cookiecutter-aws-sam-python` 

It's recommended to install this in a virtualenv, and the modern way to do it
is to use [pipenv](https://docs.pipenv.org/) for that.

Your serverless application should declare its dependencies in the generated `requirements.txt`.

Options
-------

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`include_apigw` | Includes sample code for API Gateway Proxy integration for Lambda and a Catch All method in SAM as a starting point
`include_xray` | Includes both sample code for getting started with AWS X-Ray and adds necessary permission and `Tracing` to your function
`include_safe_deployment` | Sends by default 10% of traffic for every 1 minute to a newly deployed function using [CodeDeploy + SAM integration](https://github.com/awslabs/serverless-application-model/blob/master/docs/safe_lambda_deployments.rst) - Linear10PercentEvery1Minute

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [Bruno Alla's Lambda function template](https://github.com/browniebroke/cookiecutter-lambda-function)


License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)
