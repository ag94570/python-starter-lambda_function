import json
import re
 
 
def validate(event, context):
    # print(type(event)) // dict
    event_body = event['body']
    email_regex = re.compile('^(([^<>()[].,;:s@"]+(.[^<>()[].,;:s@"]+)*)|(".+"))@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}])|(([a-zA-Z-0-9]+.)+[a-zA-Z]{2,}))$')
    matches = email_regex.match(event_body['email']) != None
 
    response = {
        'statusCode': 200,
        'body': json.dumps({ 'result': matches })
    }
 
    return response


'''

request : '{"body": "{"email": "test@example.com"}"}'

command for running locally : serverless invoke local --data '{"body": {"email": "test@example.com"}}' --function validateEmail

'''