# FlaskScale: Dynamic Web Application Management

## Project Overview

**FlaskScale** is a robust and scalable web application built using Flask and containerized with Docker. It leverages the power of Google Cloud Platform for dynamic resource management, automatically adjusting its infrastructure based on real-time CPU utilization to ensure optimal performance and responsiveness under varying traffic loads.

## Features

- **Auto-Scaling**: Automatically adds or removes instances based on CPU utilization for efficient resource management.
- **Load Balancing**: A cloud-based load balancer intelligently distributes incoming traffic across available instances, providing high availability and reduced response times.
- **Custom Domain**: Easily accessible via a custom domain name for a professional appearance and enhanced user experience.
- **Monitoring & Logging**: Built-in capabilities for performance metrics tracking, facilitating ongoing optimization.

## Architecture

- **Flask Web Application**: Stateless application design ensuring scalability.
- **Docker Containers**: Defined environment for consistent deployments.
- **Google Cloud Platform**: Utilizes instance groups and load balancers for dynamic scaling and traffic management.

## Getting Started

### Prerequisites

- Docker
- Google Cloud SDK
- A Google Cloud Platform account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flaskscale.git
   cd flaskscale
