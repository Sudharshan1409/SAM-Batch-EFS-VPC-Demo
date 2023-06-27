import os

def lambda_handler(event, context):
    print("Hello World")
    # there is an efs mounted at /mnt/efs to this lambda. just do ls into it
    print(os.listdir("/mnt/efs"))
    return {
        'statusCode': 200,
        'body': "Successfully executed"
    }
