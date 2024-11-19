import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/774157233171/Ak_Fila_Ada'

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluno Achilles entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])