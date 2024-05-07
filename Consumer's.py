from confluent_kafka import Consumer, KafkaError
import json

def consume_inventory_data():
    # Configuration for Kafka consumer
    kafka_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'inventory_group'}

    # Initialize Kafka consumer
    consumer = Consumer(kafka_config)
    consumer.subscribe(['inventory_orders'])

    # Process messages from Kafka
    while True:
        msg = consumer.poll(timeout=1.0)  # Check for new messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Reached the end of the partition
                continue
            else:
                print(f"Error in consumer: {msg.error()}")
                break
        # Decode and process the inventory message
        inventory_info = json.loads(msg.value().decode('utf-8'))
        print("Processed inventory data:", inventory_info)
        # Additional processing logic can be added here

def consume_delivery_data():
    # Configuration for Kafka consumer
    kafka_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'delivery_group'}

    # Initialize Kafka consumer
    consumer = Consumer(kafka_config)
    consumer.subscribe(['delivery_orders'])

    # Process messages from Kafka
    while True:
        msg = consumer.poll(timeout=1.0)  # Check for new messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Reached the end of the partition
                continue
            else:
                print(f"Error in consumer: {msg.error()}")
                break
        # Decode and process the delivery message
        delivery_info = json.loads(msg.value().decode('utf-8'))
        print("Processed delivery data:", delivery_info)
        # Additional processing logic can be added here

# Start consuming data from inventory and delivery topics
consume_inventory_data()
consume_delivery_data()