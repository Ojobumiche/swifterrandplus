#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine("sqlite:///agent.db", echo=True)

Base = declarative_base()

# Define the Agent class model


class Agent(Base):
    __tablename__ = 'agents'

    agent_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(Numeric, nullable=False)
    availability = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"agent_id:{self.agent_id}, name:{self.name}, email:{self.email}, phone_number:{self.phone_number}, availability:{self.availability}, created_at:{self.created_at}"


# Create the table for agents in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define the Task class model


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(Integer, nullable=False)
    client_name = Column(String(255), nullable=False)
    delivery_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"task_id:{self.task_id}, agent_id:{self.agent_id}, client_name:{self.client_name}, delivery_time:{self.delivery_time}"


# Create the table for tasks in the database
Base.metadata.create_all(engine)

# Function to create a task for an agent to deliver groceries to a client at a specified time


def create_task(agent_id, client_name, delivery_time):
    task = Task(agent_id=agent_id, client_name=client_name,
                delivery_time=delivery_time)
    session.add(task)
    session.commit()
    return task


# Example usage:
if __name__ == "__main__":
    agent1 = Agent(name="Agent 1", email="agent1@example.com",
                   phone_number="1234567890", availability="Available")
    agent2 = Agent(name="Agent 2", email="agent2@example.com",
                   phone_number="9876543210", availability="Not Available")
    session.add_all([agent1, agent2])
    session.commit()

    task1 = create_task(agent1.agent_id, "Client A",
                        datetime(2023, 9, 21, 14, 30))
    task2 = create_task(agent2.agent_id, "Client B",
                        datetime(2023, 9, 23, 17, 45))

    tasks = session.query(Task).all()

    for task in tasks:
        agent = session.query(Agent).filter_by(agent_id=task.agent_id).first()
        print(f"Task ID: {task.task_id}, Agent Name: {agent.name}, Client Name: {task.client_name}, Delivery Time: {task.delivery_time}, Agent Email: {agent.email}")

    session.close()
