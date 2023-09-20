from flask import Flask
import os
from kubernetes import client, config
from kubernetes.client.rest import ApiException

app = Flask(__name__)


@app.route('/')
def create_kubernetes_job():
    # Load the Kubernetes configuration from the default location or provide your own kubeconfig file path.
    try:
        config.load_kube_config()
    except config.config_exception.ConfigException:
        config.load_incluster_config()  # Use in-cluster configuration if available

    # Initialize the Kubernetes API client.
    api_instance = client.BatchV1Api()

    # Define the Job specification.
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name="trigger-job"),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="my-container",
                            image="your-image",
                            # Add any other container configuration as needed
                        )
                    ],
                    restart_policy="Never",
                )
            )
        ),
    )

    # Create the Job.
    try:
        api_response = api_instance.create_namespaced_job(namespace="default", body=job)
        print("Job created. Status='%s'" % str(api_response.status))
    except ApiException as e:
        print("Error creating the Job: %s" % e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)