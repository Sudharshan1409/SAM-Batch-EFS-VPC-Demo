import os

def lambda_handler(event, context):
    print("Hello World")
    # there is an efs mounted at /mnt/efs to this lambda. just ls in it to test
    # it
    print("ls on /mnt/efs:", os.listdir("/mnt/efs"))
    print("ls on /mnt/efs/_dist:", os.listdir("/mnt/efs/_dist"))
    return {
        'statusCode': 200,
        'body': "Successfully executed"
    }
