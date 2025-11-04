from flask import Flask, render_template
from datetime import datetime
import requests



app = Flask(__name__)

@app.route("/")
def home():
    # Current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Example: keep weather for fun, or remove if not needed
    lat, lon = 22.3193, 114.1694
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    response = requests.get(url).json()
    temp = response.get("current", {}).get("temperature_2m")

    # Fun facts about Azure Local, AKS, and CI/CD
    facts = [
        "Azure Local lets you run AKS clusters on-premises, managed through Azure Arc.",
        "AKS supports GitOps with Flux, so your cluster state is driven directly from a Git repo.",
        "CI/CD pipelines with GitHub Actions or Azure Pipelines can build, test, and deploy containers to AKS automatically.",
        "AKS integrates with Azure Container Registry (ACR) for secure image storage and fast pulls.",
        "Blue‑green and canary deployments are common strategies in AKS CI/CD to reduce downtime and risk."
    ]

    return render_template("index.html", now=now, temp=temp, facts=facts)

if __name__ == "__main__":
    app.run(debug=True)