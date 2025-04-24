import boto3
from botocore.exceptions import ClientError

# AWS Resources
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

# --- PART 1: List files in S3 bucket ---
def list_s3_objects(bucket_name):
    print(f"Listing objects in bucket: {bucket_name}")
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f" - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print("Bucket is empty.")
    except ClientError as e:
        print(f"Error listing S3 objects: {e}")

# --- PART 2: Create DynamoDB table ---
def create_dynamodb_table(table_name):
    print(f"Creating DynamoDB table: {table_name}")
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'UserID', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'UserID', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        print("Table created successfully!")
    except dynamodb.exceptions.ResourceInUseException:
        print("Table already exists.")
    except ClientError as e:
        print(f"Error creating DynamoDB table: {e}")

# --- PART 3: Insert an item into the table ---
def insert_dynamodb_item(table_name):
    print(f"Inserting item into table: {table_name}")
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item={
                'UserID': {'S': 'user123'},
                'Name': {'S': 'Prathyusha'},
                'Email': {'S': 'prathyusha@example.com'},
                'LoginTime': {'N': '1713988800'}  # UNIX timestamp
            }
        )
        print("Item inserted successfully!")
    except ClientError as e:
        print(f"Error inserting item: {e}")

# --- Run All ---
if __name__ == "__main__":
    BUCKET_NAME = "cf-templates-fbwg4osaf6s1-us-east-1"        # Replace with your bucket
    DYNAMO_TABLE = "UserLoginTable"      # Replace or customize table name

    list_s3_objects(BUCKET_NAME)
    create_dynamodb_table(DYNAMO_TABLE)
    insert_dynamodb_item(DYNAMO_TABLE)
