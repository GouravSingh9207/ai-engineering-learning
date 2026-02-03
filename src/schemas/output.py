from typing import TypedDict


class LogAnalysisResult(TypedDict):
    error: str
    category: str   # infra | data | code
    root_cause: str
    suggested_fix: str
