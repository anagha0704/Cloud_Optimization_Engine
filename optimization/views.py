from rest_framework.views import APIView
from rest_framework.response import Response
from .aws_connector import AWSMetricFetcher
from .llm_processor import get_llm_recommendation
from .models import EC2Instance, Recommendation

class OptimizeInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        instance_id = request.data.get('instance_id')

        if not instance_id:
            return Response({'error': 'Instance ID is required'}, status=400)

        # Step 1: Fetch metrics from AWS
        fetcher = AWSMetricFetcher(region_name='us-east-1')
        metric_data = fetcher.fetch_cpu_utilization(instance_id)

        # Step 2: Get recommendation from LLM
        recommendation_text = get_llm_recommendation(instance_id, metric_data)

        # Step 3: Save recommendation to the database
        instance, _ = EC2Instance.objects.get_or_create(instance_id=instance_id)
        Recommendation.objects.create(
            instance=instance,
            metric_name='CPUUtilization',
            suggestion=recommendation_text
        )

        return Response({'recommendation': recommendation_text})