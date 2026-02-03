import json
import re
from src.llm.client import LLMClient
from src.schemas.output import LogAnalysisResult


class LogClassifier:
    def __init__(self):
        self.llm = LLMClient()

    def classify(self, log_text: str) -> LogAnalysisResult:
        prompt = f"""
Analyze the following data pipeline log.

Return ONLY valid JSON with:
- error
- category (infra | data | code)
- root_cause
- suggested_fix

Log:
{log_text}
"""
        raw = self.llm.run(prompt)

        # 🔹 Remove markdown code fences if present
        cleaned = re.sub(r"```json|```", "", raw).strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {
                "error": "Unparseable LLM response",
                "category": "unknown",
                "root_cause": raw,
                "suggested_fix": "Inspect logs manually"
            }
