import json
import requests
import pandas as pd

# Step 1: Load test data
with open("test_data.json", "r") as f:
    test_data = json.load(f)

results = []

for test in test_data:
    payload = {"input": test["input"]}
    try:
        response = requests.post("http://127.0.0.1:8000/chatbot/invoke", json=payload)
        result = response.json()

        output_data = result.get("output", "")
        if isinstance(output_data, dict):
            output = output_data.get("content", "")
        else:
            output = str(output_data)

        # ✅ Loose matching
        is_correct = test["expected"].lower() in output.lower()

        results.append({
            "id": test["id"],
            "input": test["input"],
            "expected": test["expected"],
            "got": output,
            "correct": is_correct
        })
    except Exception as e:
        results.append({
            "id": test["id"],
            "input": test["input"],
            "expected": test["expected"],
            "got": f"Error: {str(e)}",
            "correct": False
        })

# Step 2: Save results to CSV
df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)

# Step 3: Print Accuracy
accuracy = df["correct"].mean() * 100
print(df)
print(f"\nModel Accuracy: {accuracy:.2f}%")
