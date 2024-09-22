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

3. **Git clone this repository.**
   - Clone this repository to the VM using command:
     ```bash
     git clone https://github.com/abhi-kr12/de-zoomcamp-playstore.git
     ```
   - `cd` into `VCC_Final-Project`.
   - Check if all the directories are present which are `static`, `templates`, and the files `.gitignore`,`app.py`,`dockerfile` and `requirements.txt`.

4. **Download the service account key and paste it in the VCC-Final-Project folder**
   - Navigate to service accounts under IAM in GCP and create a new key for the service account used for this project.
   - Transfer the json file downloaded to VCC-Final-Project in the VM created in step 2 and rename it as `vcc-main-project`.

5. **Test if the code is working fine**
   - `cd` into `VCC-Final-Project` in the instance created.
   - Build a docker image using the following command
     ```bash
     docker build -t vcc-web-app:latest .
     ```
   - Run the docker image using the following command
     ```bash
     docker run -p 5000:5000 vcc-web-app
     ```
   - The docker container will start running and you should see something like this:
     <p align="center">
      <img src="images\docker_run.png">
     </p>
   - Now get the external IP for the instance from the console. Open your web browser and navigate to `http://VM_EXTERNAL_IP:5000`. If the website is displayed, it means all the files are correct, and you can proceed 
     further.

6. **Push the docker image created to the container registry.**
   - Tag the docker image.
      ```bash
       docker tag vcc-web-app gcr.io/YOUR_PROJECT_ID/vcc-web-app
      ```
   - Push the docker image to the container registry.
     ```bash
       docker build gcr.io/YOUR_PROJECT_ID/vcc-web-app
     ```
    <p align="center">
      <img src="images\docker_container.png">
     </p>
     
7. **Create an instance template for the instance group**
   - Navigate to `Instance templates` under `Compute Engine` in the console.
   - Choose the machine type, storage, etc.
   - Under container click on deploy container and enter `gcr.io/YOUR_PROJECT_ID/vcc-web-app` as the docker image and create the template.
   - You can also use the below shell script to achieve this.
     ### Script

    ```bash
    #!/bin/bash
    
    # Set variables
    PROJECT_ID="your-project-id"
    ZONE="us-central1-a"  # Change to your desired zone
    TEMPLATE_NAME="my-instance-template"
    MACHINE_TYPE="e2-medium"  # Change as needed
    IMAGE_FAMILY="debian-10"   # Change to your desired image family
    IMAGE_PROJECT="debian-cloud" # Change to your desired image project
    CONTAINER_IMAGE="gcr.io/YOUR_PROJECT_ID/vcc-web-app"  # Change to your container image
    
    # Create the instance template
    gcloud compute instance-templates create "$TEMPLATE_NAME" \
      --project="$PROJECT_ID" \
      --machine-type="$MACHINE_TYPE" \
      --image-family="$IMAGE_FAMILY" \
      --image-project="$IMAGE_PROJECT" \
      --tags=http-server,https-server \
      --container-image="$CONTAINER_IMAGE" \
      --zone="$ZONE"
    
    echo "Instance template '$TEMPLATE_NAME' created successfully with container deployment."
    ```
    <p align="center">
      <img src="images\instance_template.png">
     </p>

8. **Create an instance group using the instance template created in the previous step**
   - Navigate to `Instance groups` under `Compute Engine` in the console.
   - Fill in the required fields:
     - **Name**: Enter a name for your instance group (e.g., `my-instance-group`).
     - **Zone**: Select the zone where you want to create the instance group.
     - **Instance template**: Select the instance template created in the previous step.
     - **Auto scaling**: Set the autoscaling mode, minimum number of instances, maximum number of instances and the autoscaling signal. For this project we have selected `On: add and remove instances to the group`, `2`,         `6` and `CPU Utilization : 50%`.
  - Create a health check on port 5000 under path /health.
  - Create the instance group. You can also use the below shell script to achieve this.
    ### Script

    ```bash
    #!/bin/bash

    # Set variables
    INSTANCE_GROUP_NAME="my-instance-group"
    ZONE="us-central1-a"  # Change to your desired zone
    TEMPLATE_NAME="my-instance-template"  # Use the name of your instance template
    
    # Create the instance group
    gcloud compute instance-groups managed create "$INSTANCE_GROUP_NAME" \
      --base-instance-name="$INSTANCE_GROUP_NAME" \
      --size=1 \
      --template="$TEMPLATE_NAME" \
      --zone="$ZONE"
    
    echo "Instance group '$INSTANCE_GROUP_NAME' created successfully."
    ```
    <p align="center">
      <img src="images\instance_group.png">
     </p>

9. **Create a load balancer to point at the instance group**
   - Navigate to `Load balancing` under `Network Services` in the console.
   - Choose `Application Load Balancer`, `Public facing` and `Global deployment`.
   - Select `HTTP` and port 80 as the Frontend configuration.
   - Select the instance group created in the previous step as the backend configuration. Add health checks for port 5000.
   - Add routing rules if required, name the load balancer and create it.
   - You can also use the below shell script to achieve this.
     ### Script

    ```bash
    #!/bin/bash

    # Set variables
    PROJECT_ID="your-project-id"
    REGION="us-central1"  # Change to your desired region
    LOAD_BALANCER_NAME="my-load-balancer"
    INSTANCE_GROUP_NAME="my-instance-group"  # Name of your managed instance group
    HEALTH_CHECK_NAME="my-health-check"
    BACKEND_SERVICE_NAME="my-backend-service"
    FRONTEND_IP_NAME="my-frontend-ip"
    
    # Create a health check
    gcloud compute health-checks create http "$HEALTH_CHECK_NAME" \
      --port=80 \
      --request-path="/" \
      --project="$PROJECT_ID"
    
    # Create a backend service
    gcloud compute backend-services create "$BACKEND_SERVICE_NAME" \
      --load-balancing-scheme=EXTERNAL \
      --protocol=HTTP \
      --health-checks="$HEALTH_CHECK_NAME" \
      --global \
      --project="$PROJECT_ID"
    
    # Add the instance group to the backend service
    gcloud compute backend-services add-backend "$BACKEND_SERVICE_NAME" \
      --instance-group="$INSTANCE_GROUP_NAME" \
      --instance-group-zone="us-central1-a" \  # Change to your instance group zone
      --global \
      --project="$PROJECT_ID"
    
    # Create a global forwarding rule
    gcloud compute forwarding-rules create "$LOAD_BALANCER_NAME" \
      --global \
      --target-http-proxy="$LOAD_BALANCER_NAME-proxy" \
      --ports=80 \
      --address="$FRONTEND_IP_NAME" \
      --project="$PROJECT_ID"
    
    # Create a URL map
    gcloud compute url-maps create "$LOAD_BALANCER_NAME-proxy" \
      --default-service="$BACKEND_SERVICE_NAME" \
      --project="$PROJECT_ID"
    
    echo "Load balancer '$LOAD_BALANCER_NAME' created successfully."
    ```
   <p align="center">
      <img src="images\load_balancer.png">
     </p>

10. **Create a domain name (Optional)**
    - If required, create a domain name under Google domains.
    - Add the load balancer IP address under the DNS records as an A record.
    - This step is optional, we can as well just use the load balancer IP address to visit the website.
