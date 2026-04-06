# 🚀 ChatOps Deployment Automation Bot

## 📌 Overview
This project implements a ChatOps-based deployment automation system using Slack and AWS.

Instead of manually logging into servers, deployment and rollback operations can be triggered using Slack commands.

---

## 🧠 Architecture

Slack → API Gateway → Lambda → SSM → EC2 → Shell Scripts

---

## ⚙️ Features

- 🔹 Deploy application using `/deploy webapp`
- 🔹 Rollback using `/rollback webapp`
- 🔹 Remote execution using AWS Systems Manager
- 🔹 Slack-based infrastructure control

---

## 🛠 Technologies Used

- Slack
- AWS Lambda
- API Gateway
- AWS Systems Manager (SSM)
- EC2 (Amazon Linux)

---

## 🔄 Deployment Flow

1. User sends command in Slack
2. API Gateway receives request
3. Lambda processes command
4. SSM executes script on EC2
5. Deployment result returned to Slack

---

## ⚠️ Note

Kubernetes functionality is simulated due to instance limitations. Shell scripts mimic kubectl operations.

---

## 🎯 Author

Dhanwa
