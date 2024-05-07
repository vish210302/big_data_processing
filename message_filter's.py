import json

def is_inventory_message(message):
    """
    Checks if the message pertains to inventory based on its 'type' attribute.
    
    Args:
        message (str): A string containing JSON data.
        
    Returns:
        bool: Returns True if the 'type' of the message is 'inventory', False otherwise.
    """
    try:
        message_data = json.loads(message)
        return message_data.get('type') == 'inventory'
    except json.JSONDecodeError:
        return False

def is_delivery_message(message):
    """
    Determines if the message relates to delivery by examining the 'type' attribute.
    
    Args:
        message (str): A string containing JSON data.
        
    Returns:
        bool: Returns True if the 'type' of the message is 'delivery', False otherwise.
    """
    try:
        message_data = json.loads(message)
        return message_data.get('type') == 'delivery'
    except json.JSONDecodeError:
        return False