
import boto3

sqs = boto3.client('sqs', region_name='us-east-1') 

# Cria a fila SQS
response = sqs.create_queue(
    QueueName='Ak_Fila_Ada',
    Attributes={
        'DelaySeconds': '5'  # Atraso opcional para as mensagens
    }
)

# Obtém a URL da fila criada
queue_url = response['QueueUrl']
print("Fila criada com sucesso. URL da Fila:", queue_url)