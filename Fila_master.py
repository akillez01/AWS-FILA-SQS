import boto3

# Nome da fila. Deve ser único na sua conta da AWS.
queue_name = 'Ak_Fila_Ada'
region_name = 'us-east-1'

sqs = boto3.client('sqs', region_name=region_name)

try:
    # Tenta criar a fila.
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes={
            'DelaySeconds': '5'  # Atraso opcional para as mensagens em segundos.
        }
    )

    # Obtém a URL da fila criada.
    queue_url = response['QueueUrl']
    print(f"Fila '{queue_name}' criada com sucesso. URL da Fila: {queue_url}")

    # Envia uma mensagem para a fila.
    message_response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Aluno Achilles entregou o projeto'
    )
    print(f"Mensagem enviada com sucesso. ID da mensagem: {message_response['MessageId']}")

    # Exclui a fila (descomente se quiser excluir a fila após o uso).
    sqs.delete_queue(QueueUrl=queue_url)
    print("Fila excluída com sucesso.")

except sqs.exceptions.QueueAlreadyExists:
    # Lida com o caso em que a fila já existe.
    print(f"Fila '{queue_name}' já existe.")

    # Se a fila já existir, obtém a URL dela.
    response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']
    print(f"URL da Fila: {queue_url}")

    # Envia uma mensagem para a fila (mesmo se ela já existir)
    message_response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Aluno Achilles entregou o projeto'
    )
    print(f"Mensagem enviada com sucesso. ID da mensagem: {message_response['MessageId']}")


except Exception as e:
    # Lida com outros erros.
    print(f"Erro ao criar ou usar a fila: {e}")

