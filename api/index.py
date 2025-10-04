from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import numpy as np
import json
from fastapi.middleware.cors import CORSMiddleware

# Define the data model for the POST request body
class TelemetryRequest(BaseModel):
    regions: List[str]
    threshold_ms: int

# Create FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


# Simulate getting telemetry data for the regions
def get_telemetry_data_for_region(region: str) -> List[Dict]:
    sample_data = json.load("q-vercel-latency.json")
    return sample_data.get(region, [])

# Calculate per-region metrics
def calculate_metrics(data: List[Dict], threshold_ms: int):
    latencies = [entry['latency_ms'] for entry in data]
    uptimes = [entry['uptime_percent'] for entry in data]
    
    avg_latency = np.mean(latencies)
    p95_latency = np.percentile(latencies, 95)
    avg_uptime = np.mean(uptimes)
    breaches = sum(1 for latency in latencies if latency > threshold_ms)
    
    return {
        "avg_latency": avg_latency,
        "p95_latency": p95_latency,
        "avg_uptime": avg_uptime,
        "breaches": breaches
    }

# Define POST endpoint to receive telemetry data and return metrics
@app.post("/metrics")
async def get_metrics(request: TelemetryRequest):
    metrics_per_region = {}

    # For each region, get the telemetry data and calculate metrics
    for region in request.regions:
        data = get_telemetry_data_for_region(region)
        if not data:
            raise HTTPException(status_code=404, detail=f"No data found for region {region}")
        metrics_per_region[region] = calculate_metrics(data, request.threshold_ms)
    
    return metrics_per_region
