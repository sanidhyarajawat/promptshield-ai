import json
import argparse
from detector import analyze_prompt_security

def main():
    parser = argparse.ArgumentParser(description="PromptShield CLI — Analyze prompt vulnerability.")
    parser.add_argument("session_file", help="Path to a JSON file containing system prompt and messages.")
    args = parser.parse_args()

    with open(args.session_file, 'r') as f:
        session = json.load(f)

    print("🔍 Analyzing prompt session...\n")
    result = analyze_prompt_security(session['system_prompt'], session['messages'])

    if "error" in result:
        print("❌ Error:", result["error"])
    else:
        print("🛡️ PromptShield Analysis")
        print("=======================")
        print(f"Risk Score: {result.get('Risk Score', 'N/A')}")
        print("\n🚨 Issues Detected:")
        for issue in result.get("Detected Issues", []):
            print(f" - {issue}")
        print("\n✅ Recommendations:")
        for rec in result.get("Recommendations", []):
            print(f" - {rec}")
        print("=======================")

if __name__ == "__main__":
    main()