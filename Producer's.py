from confluent_kafka import Producer
import json

def produce_inventory_order():
    # Configuration for Kafka producer
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Initialize Kafka producer
    producer = Producer(kafka_config)

    # Example data for inventory events (replace with real data as needed)
    inventory_events = [
        {"type": "inventory", "item_id": "123", "quantity": 10},
        {"type": "inventory", "item_id": "456", "quantity": 20}
    ]

    # Publish inventory events to Kafka topic
    for event in inventory_events:
        producer.produce('inventory_orders', json.dumps(event).encode('utf-8'))

    # Ensure all messages are sent
    producer.flush()

def produce_delivery_order():
    # Configuration for Kafka producer
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Initialize Kafka producer
    producer = Producer(kafka_config)

    # Example data for delivery events (replace with real data as needed)
    delivery_events = [
        {"type": "delivery", "order_id": "1001", "status": "pending"},
        {"type": "delivery", "order_id": "1002", "status": "shipped"}
    ]

    # Publish delivery events to Kafka topic
    for event in delivery_events:
        producer.produce('delivery_orders', json.dumps(event).encode('utf-8'))

    # Ensure all messages are sent
    producer.flush()

# Trigger production of inventory and delivery orders
produce_inventory_order()
produce_delivery_order()