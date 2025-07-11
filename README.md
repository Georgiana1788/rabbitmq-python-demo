# RabbitMQ Python Demo

## Descriere
Acest proiect demonstrează folosirea RabbitMQ cu Python pentru a trimite și a primi mesaje JSON într-o coadă (`queue`).

## Tehnologii
- RabbitMQ (container Docker)
- Python `pika`

## Cum rulezi

1. Rulează RabbitMQ cu Docker:
   ```
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```

2. Instalează dependențele Python:
   ```
   pip install -r requirements.txt
   ```

3. Rulează `consumer.py` într-un terminal:
   ```
   python consumer.py
   ```

4. Rulează `producer.py` într-alt terminal:
   ```
   python producer.py
   ```

5. Vezi rezultatul în consolă și în UI-ul RabbitMQ (http://localhost:15672).

## Autori
Georgiana Mangiuchi
