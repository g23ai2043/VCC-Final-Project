# FlaskScale: Dynamic Web Application Management

<p align="center">
  <img src="images\main.png">
</p>

---
## Index

- [Description and Objective](#description-and-objective)
- [Technologies](#technologies)
- [Data Architecture](#data-architecture)
- [Replication of the project](#replication-of-the-project)

---

## Description and Objective

**FlaskScale** is a scalable web application framework built on Flask, designed to seamlessly manage and optimize web resources. By leveraging Docker for containerization and Google Cloud Platform for cloud infrastructure, FlaskScale provides a highly efficient environment that adjusts to varying user demands. The application ensures high availability and responsiveness through dynamic resource management, making it ideal for businesses and developers looking to optimize performance in real-time.

- **Usage**

  - **E-Commerce Platforms**: Automatically scales resources during high-traffic sales events to ensure smooth transactions.
  - **SaaS Applications**: Dynamically allocates resources for consistent performance across multiple clients.
  - **Social Media Applications**: Efficiently manages fluctuating traffic during trending events to maintain quick response times.
  - **Content Management Systems (CMS)**: Handles traffic bursts during content releases, ensuring seamless delivery to users.
  - **Real-Time Data Processing**: Adjusts resources based on live data processing demands for timely analysis without bottlenecks.
  - **Educational Platforms**: Accommodates surges in users during course launches or exam periods for a smooth learning experience.
  - **API Services**: Ensures API endpoints remain responsive under variable traffic conditions by scaling resources as needed.
  - **Event-Driven Applications**: Automatically adjusts infrastructure to handle unpredictable spikes in user-generated events, ensuring timely processing.

- **Objective**

  **FlaskScale** aims to provide a robust solution for deploying Flask applications that automatically scale based on user demand, intelligently managing resource allocation to maintain optimal performance and minimize costs.The key goals include:

  - Automatically adjusts resources in real-time based on traffic fluctuations.
  - Ensures applications remain responsive during heavy load.
  - Reduces operational costs during low traffic periods.
  - Eliminates the need for manual intervention in resource management.
  - Supports seamless scaling to accommodate varying user demands.

---

## Technologies

- **Flask**  
  [Flask](https://flask.palletsprojects.com/) is a lightweight WSGI web application framework in Python that is easy to use and suitable for building both simple and complex applications.

- **Docker**  
  [Docker](https://docs.docker.com/) is a platform that enables developers to package applications and their dependencies into containers, ensuring consistency across development, testing, and production environments.

- **Google Compute Engine**  
  [Google Compute Engine](https://cloud.google.com/compute/docs) provides scalable and flexible virtual machine (VM) instances on Google Cloud, allowing users to run applications in a cloud environment.

- **Instance Groups**  
  [Instance Groups](https://cloud.google.com/compute/docs/instance-groups) in Google Cloud allow you to manage collections of virtual machine instances, enabling auto-scaling and load balancing to handle varying workloads efficiently.

- **Load Balancing**  
  [Load Balancing](https://cloud.google.com/load-balancing/docs) is a cloud service that distributes incoming traffic across multiple backend instances, enhancing application availability and reliability.

- **Google Domains**  
  [Google Domains](https://domains.google/) is a domain registration service by Google that allows users to purchase and manage domain names for their web applications, providing an easy way to connect to Google Cloud services.

---

## Data Architecture

<p align="center">
  <img src="images\architecture.png">
</p>

---

### Replication of the Project

Replication steps are given in accordance with Windows OS and Google Cloud Platform.

**Steps to be followed:**

1. **Create a project on Google Cloud console**
   - Create a new project in Google cloud.
   - Enable compute engine API, container API and load balancing API.

2. **Set up a virtual machine for creating Docker images and other related tasks.**
   - Create a new e2.medium instance. Change the configuration as required. Allow HTTP and HTTPS traffic.
   - ssh into the instance using the console and authenticate.
   - Update package lists:
     ```bash
     sudo apt-get update
     ```
   - Install Docker:
     ```bash
     sudo apt-get install -y docker.io
     ```
   - Add your user to the Docker group:
     ```bash
     sudo usermod -aG docker $USER
     ```
   - Log out and log back in to refresh group membership.
