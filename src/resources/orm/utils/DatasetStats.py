from typing import TypedDict, Optional


class DatasetStats(TypedDict):
    number_documents: Optional[int]
    number_tokens: Optional[int]
    number_chars: Optional[int]
