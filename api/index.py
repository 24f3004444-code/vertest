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
    telemetry_data = json.loads('''[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 107.18,
    "uptime_pct": 98.744,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 186.35,
    "uptime_pct": 98.651,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 118.68,
    "uptime_pct": 98.551,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 139.15,
    "uptime_pct": 97.918,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 220.44,
    "uptime_pct": 97.491,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 133.99,
    "uptime_pct": 97.125,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 168.27,
    "uptime_pct": 98.106,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 198.05,
    "uptime_pct": 97.437,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 143.98,
    "uptime_pct": 99.053,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 127.34,
    "uptime_pct": 98.294,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 205.84,
    "uptime_pct": 98.342,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 202.79,
    "uptime_pct": 99.36,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 186.94,
    "uptime_pct": 99.289,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 173.41,
    "uptime_pct": 97.118,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 217.81,
    "uptime_pct": 99.213,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 169.09,
    "uptime_pct": 99.244,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 178.75,
    "uptime_pct": 98.652,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 132.07,
    "uptime_pct": 98.585,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 179.54,
    "uptime_pct": 97.305,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 122.36,
    "uptime_pct": 97.448,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 140.12,
    "uptime_pct": 98.197,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 194.71,
    "uptime_pct": 98.933,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 180.41,
    "uptime_pct": 98.87,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 176.48,
    "uptime_pct": 99.462,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 220.36,
    "uptime_pct": 98.738,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 206.76,
    "uptime_pct": 98.706,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 179.83,
    "uptime_pct": 97.313,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 223.42,
    "uptime_pct": 98.781,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 224.3,
    "uptime_pct": 97.638,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 171.35,
    "uptime_pct": 97.436,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 153.55,
    "uptime_pct": 98.336,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 207.46,
    "uptime_pct": 99.123,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 110.44,
    "uptime_pct": 99.045,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 111.25,
    "uptime_pct": 98.594,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 202.23,
    "uptime_pct": 97.913,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 180.15,
    "uptime_pct": 99.167,
    "timestamp": 20250312
  }
]''')
    
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
