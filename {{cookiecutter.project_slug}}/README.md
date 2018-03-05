# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

Reach out to [{{ cookiecutter.full_name }}](https://twitter.com/{{ cookiecutter.twitter_username }}) if you need a hand here.

## Requirements

* AWS CLI already configured with at least PowerUser permission
* Python 3.6 installed

## Packaging

AWS Lambda Python runtime requires a flat folder with all dependencies including the application. To facilitate this process, the pre-made SAM template expects this structure to be under `<src>/dev/`:

```yaml
...
    FirstFunction:
        Type: AWS::Serverless::Function
        Properties:
            CodeUri: first_function/dev/
            ...
```

With that in mind, we will install all dependencies using `pip` into `dev` before we call AWS CLI to package it all up to Amazon S3:

```bash
pip install -r first_function/requirements.txt -t first_function/dev/
cp first_function/app.py first_function/dev/
```

Repeat the process for the `second_function`:

```bash
pip install -r second_function/requirements.txt -t second_function/dev/
cp second_function/app.py second_function/dev/
```

Now, run the following command to have SAM package your source code to a S3 Bucket prior to deployment:

```bash
aws cloudformation package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```

**NOTE**: If you don't have a S3 bucket and want to create one using the AWS CLI you can use the following snippet

```bash
aws s3 mb s3://YOUR_UNIQUE_BUCKET_NAME 
```

## Deployment

The following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
aws cloudformation deploy \
    --template-file packaged.yaml \
    --stack-name {{ cookiecutter.project_slug }} \
    --capabilities CAPABILITY_IAM
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) for more details in how to get started.**

{% if cookiecutter.include_apigw == "y" %}
After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name {{ cookiecutter.project_slug }} \
    --query 'Stacks[].Outputs'
``` 
{% endif %}

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [Bruno Alla's Lambda function template](https://github.com/browniebroke/cookiecutter-lambda-function)
* [Heitor Lessa's SAM for Python 3.6 template](https://github.com/heitorlessa/cookiecutter-aws-sam-python)


# TODO

* [ ] Create Unit tests sample
* [ ] Create Functional tests sample
* [ ] Write Testing instructions


Made with :heart: by {{ cookiecutter.full_name }}
