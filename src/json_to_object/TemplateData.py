from dataclasses import dataclass


@dataclass
class TemplateData:
    to_name: str
    to_address: str
    from_name: str
    from_org: str

