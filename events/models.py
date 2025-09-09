from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, AwareDatetime, ConfigDict

EventType = Literal["lead_found", "scrape_progress", "run_started", "run_completed", "error"]

class LeadData(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = Field(None, description="E.164 format, e.g., +27XXXXXXXXX")
    employment: Optional[str] = None
    vehicle: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    extra: Dict[str, Any] = Field(default_factory=dict)

class StatsData(BaseModel):
    processed: Optional[int] = 0
    success: Optional[int] = 0
    failed: Optional[int] = 0
    valid_mobile: Optional[int] = 0
    hlr_passed: Optional[int] = 0
    hlr_failed: Optional[int] = 0
    leads_extracted: Optional[int] = 0

class EventPayload(BaseModel):
    model_config = ConfigDict(extra="allow")
    event: EventType
    timestamp: AwareDatetime
    source: str
    data: Optional[LeadData] = None
    stats: Optional[StatsData] = None
    meta: Dict[str, Any] = Field(default_factory=dict)
