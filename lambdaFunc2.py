import json
   

def helloWorld(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Ragu!!!!!!!!!!')
    }
   