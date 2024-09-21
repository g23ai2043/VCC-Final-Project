# app.py
from flask import Flask, render_template,Response
import socket,requests,subprocess
from google.cloud import compute_v1
import os

PROJECT_ID = 'vcc-main-project'
INSTANCE_GROUP_NAME = 'vcc-web-app-group'
ZONE = 'us-central1-c'

app = Flask(__name__)

@app.route('/test-access', methods=['GET'])
def test_access():
    try:
        instances_client = compute_v1.InstancesClient()
        instances = instances_client.list(project=PROJECT_ID, zone=ZONE)
        return Response("Access successful!", mimetype='text/plain')
    except Exception as e:
        return Response(f"Access failed: {str(e)}", mimetype='text/plain')

@app.route('/instances')
def get_instances():
    try:
        instances_client = compute_v1.InstancesClient()
        instances = instances_client.list(project=PROJECT_ID, zone=ZONE)

        instance_info = []
        for instance in instances:
            # Get the internal IP address from the first network interface
            internal_ip = instance.network_interfaces[0].network_i_p if instance.network_interfaces else "N/A"
            
            # Get the external IP address if available
            external_ip = "N/A"
            if instance.network_interfaces:
                for access_config in instance.network_interfaces[0].access_configs:
                    if access_config.name == "External NAT":
                        external_ip = access_config.nat_i_p
            
            instance_info.append(f"Name: {instance.name}, Status: {instance.status}, Internal IP: {internal_ip}, External IP: {external_ip}")
        
        return "\n".join(instance_info), 200  # Moved outside of the loop
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/external-ip')
def get_external_ip():
    try:
        response = requests.get('http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip',
                                 headers={'Metadata-Flavor': 'Google'})
        external_ip = response.text
        return external_ip
    except Exception as e:
        return str(e)

@app.route('/internal-ip')
def get_internal_ip():
    try:
        response = requests.get('http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/ip',
                                 headers={'Metadata-Flavor': 'Google'})
        internal_ip = response.text
        return internal_ip
    except Exception as e:
        return str(e)

@app.route('/health', methods=['GET'])
def health_check():
    return Response("status: healthy", status=200, mimetype='text/plain')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
