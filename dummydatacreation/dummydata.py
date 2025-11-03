import pandas as pd
from datetime import datetime, timedelta
import random

# Generate Orders
orders = pd.DataFrame({
    'order_id': [f'O{i}' for i in range(1, 301)],
    'customer_id': [f'C{random.randint(1, 100)}' for _ in range(300)],
    'order_date': pd.date_range(start='2025-01-01', periods=300, freq='D')
})
orders.to_csv('orders.csv', index=False)

from faker import Faker

# Generate Customers
fake = Faker()

names = [fake.name() for _ in range(100)]

emails = [f"{name.lower().replace(' ', '.')}@example.com" for name in names]


customers = pd.DataFrame({
    'customer_id': [f'C{i}' for i in range(1, 101)],
    'name': names,
    'email': emails
})
customers.to_csv('customers.csv', index=False)

# Generate Shipments
order_ids = orders['order_id'].tolist()

statuses = ['shipped', 'delivered']
shipments = pd.DataFrame({
     'shipment_id': [f'S{i}' for i in range(1, 301)],
    
    'order_id': random.sample(order_ids, 300),
    'status': [random.choice(statuses) for _ in range(300)],
    'shipped_at': pd.date_range(start='2025-01-02', periods=300, freq='D'),
    'delivered_at': pd.date_range(start='2025-01-03', periods=300, freq='D')
})

shipments.to_csv('shipments.csv', index=False)
