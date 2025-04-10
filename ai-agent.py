import requests
import json
import subprocess


API_URL = "http://127.0.0.1:1234"

def ask_ai(task):
    url = "http://127.0.0.1:1234"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "local-model",  
        "messages": [
            {"role": "system", "content": "You are a helpful AI agent that converts tasks into plans and shell commands."},
            {"role": "user", "content": task}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()
    except Exception as e:
        print("❌ Failed to parse JSON:", e)
        print("Raw response:", response.text)
        return None

    if "choices" not in result:
        print("❌ Unexpected response format:")
        print(result)
        return None

    return result["choices"][0]["message"]["content"]


def execute_command(command):
    try:
        print(f"Running command: {command}")
        output = subprocess.check_output(command, shell=True, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("❌ Error executing command:", e.output)

def main():
    task = input("🧠 Enter your task: ")
    plan = ask_ai(task)
    print("\n📝 PLAN FROM AI:\n", plan)

    approval = input("\n✅ Approve? (y/n): ").strip().lower()
    if approval == "y":
        for line in plan.split('\n'):
            if line.strip().startswith("$"):
                command = line.strip().lstrip("$ ")
                execute_command(command)

        success = input("✅ Was the task successful? (y/n): ").strip().lower()
        if success == "y":
            print("🎉 Task completed!")
        else:
            reason = input("❌ Reason for failure: ")
            new_task = f"{task}\nThe previous attempt failed because: {reason}. Try again."
            refined_plan = ask_ai(new_task)
            print("\n🔁 NEW PLAN:\n", refined_plan)
    else:
        print("❌ Task not approved. Exiting.")

if __name__ == "__main__":
    main()
