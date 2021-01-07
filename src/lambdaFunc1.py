import json
   

def helloFunction(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Welcome')
    }
   
