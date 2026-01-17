# API Health Monitoring System

## Overview

This project is a self-hosted API health monitoring system built as part of a DevOps internship assignment.

The system periodically checks the health of user-defined API endpoints, detects meaningful state changes (Healthy → Unhealthy or vice versa), and sends notifications when such changes occur.

The focus of this project is on system design, reliability, and infrastructure, not UI or dashboards.

---

## What the System Does

- Monitors multiple API endpoints
- Health checks are configurable per API
  - Expected HTTP status code
  - Timeout threshold
- Tracks previous health state
- Sends notifications only when health status changes
- Runs without using any third-party or managed monitoring services

---

## High-Level Architecture

- EC2  
  Runs the health check worker

- DynamoDB  
  - api_config table → stores API configurations  
  - api_state table → stores last known health state  

- SNS  
  Sends alerts when an API’s health status changes

The monitoring logic runs on the EC2 instance and interacts directly with DynamoDB and SNS using IAM roles.

---


---

## How Health Checking Works

1. API configurations are read from the api_config DynamoDB table
2. Each API is called using an HTTP GET request
3. Health is evaluated based on:
   - HTTP status code
   - Response time
4. Current health state is compared with the previous state
5. If the state has changed:
   - A notification is sent via SNS
6. Latest state is stored in api_state

This approach avoids alert noise by notifying only on real state changes.

---

## Infrastructure Deployment

### Prerequisites

- AWS account
- Terraform installed
- AWS credentials configured locally

### Steps

cd terraform  
terraform init  
terraform apply  

After apply completes, Terraform outputs:
- EC2 public IP
- SNS topic ARN

---

## IAM & Security

- EC2 uses an IAM role with least privilege
- Permissions are limited to:
  - DynamoDB read/write
  - SNS publish
- No credentials are stored in code

---

## Assumptions & Trade-offs

- DynamoDB Scan is used for simplicity  
  In production, this would be optimized using pagination or indexed queries.
- Health checks are run by a single worker  
  The system can scale horizontally by adding more workers.
- No UI or dashboard is included, as it is out of scope for this assignment.

---

## Scalability Considerations

In a production setup, this system can scale by:
- Running multiple EC2 instances or scheduled workers
- Partitioning APIs across workers
- Leveraging DynamoDB on-demand scaling
- Adding retries and backoff for failed API checks

---

## Conclusion

This project demonstrates backend system design, infrastructure-as-code, and operational thinking around reliability and alerting.

The emphasis is on simplicity, correctness, and clear design decisions.

