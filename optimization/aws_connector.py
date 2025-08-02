import boto3
from datetime import datetime, timedelta

class AWSMetricFetcher:
    def __init__(self, region_name):
        self.cloudwatch_client = boto3.client('cloudwatch', region_name=region_name)
        self.ec2_client = boto3.client('ec2', region_name=region_name)

    def get_instance_ids(self):
        # A function to get a list of all EC2 instance IDs
        instance_ids = []
        reservations = self.ec2_client.describe_instances()
        for reservation in reservations['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])
        return instance_ids

    def fetch_cpu_utilization(self, instance_id, hours=24):
        # A function to get CPU utilization for a specific instance
        response = self.cloudwatch_client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'cpu_utilization',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/EC2',
                            'MetricName': 'CPUUtilization',
                            'Dimensions': [
                                {'Name': 'InstanceId', 'Value': instance_id},
                            ]
                        },
                        'Period': 3600,  # 1-hour period
                        'Stat': 'Average',
                    },
                    'ReturnData': True,
                },
            ],
            StartTime=datetime.utcnow() - timedelta(hours=hours),
            EndTime=datetime.utcnow(),
        )
        return response['MetricDataResults'][0]['Values']