# api/index.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import numpy as np

app = FastAPI()

# Define the request body format using Pydantic
class MetricsRequest(BaseModel):
    regions: List[str]
    threshold_ms: int

# Function to load telemetry data (from the api/ folder)
def load_telemetry_data(file_name="q-vercel-latency.json"):
    with open(file_name, "r") as file:
        telemetry_data = json.load(file)
    
    return telemetry_data

# Function to compute metrics
def compute_metrics(data, threshold_ms):
    # Compute average latency
    latencies = [entry["latency"] for entry in data]
    avg_latency = np.mean(latencies)

    # Compute p95 latency (95th percentile)
    p95_latency = np.percentile(latencies, 95)

    # Compute average uptime
    uptimes = [entry["uptime"] for entry in data]
    avg_uptime = np.mean(uptimes)

    # Count breaches (latency above the threshold)
    breaches = sum(1 for latency in latencies if latency > threshold_ms)

    return {
        "avg_latency": avg_latency,
        "p95_latency": p95_latency,
        "avg_uptime": avg_uptime,
        "breaches": breaches
    }

# Endpoint to process the POST request
@app.post("/metrics")
async def get_metrics(request: MetricsRequest):
    try:
        # Load telemetry data
        telemetry_data = load_telemetry_data()

        # Prepare the result
        result = {}
        for region in request.regions:
            if region not in telemetry_data:
                raise HTTPException(status_code=404, detail=f"Region {region} not found")
            region_data = telemetry_data[region]
            region_metrics = compute_metrics(region_data, request.threshold_ms)
            result[region] = region_metrics

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Optional: Enable CORS if testing from the browser
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
