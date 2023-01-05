# python_starter_lambda_function
Basic Example for python Lambda function

## Steps for creating new project

- You must have Node.js installed on your system to implement the Serverless framework. 
- To install Serverless, run this command from the command line.
```zsh
 npm i -g serverless
```
- Initialize your project by running this command.

```zsh
 serverless
```
- Provide the required details and proceed with the setup.

- Create function in yml file with relevant names
```yml
functions:
  firstLambda: // function name
    handler: starterLambda/firstLambda.handler //handler path
```

- To invoke lambda locally, run the below command
```zsh
serverless invoke local -f {functionName}
```
or if you want to provide aws profile and stage
```zsh
serverless invoke local --stage dev --aws-profile abc -f {functionName}
```
for data you can pass payload directly

```zsh
serverless invoke --function --data '{ "queryStringParameters": {"id":"P50WXIl6PUlonrSH"}}'
```

or path to file

```zsh
serverless invoke --function {function_name} --path event_data.json
```