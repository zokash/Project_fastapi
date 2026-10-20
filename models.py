from pydantic import BaseModel

class ContactTemplate(BaseModel):
    company_id: int
    poc_name: str
    phone: str
    email: str
    designation: str | None = None


class CompanyTemplate(BaseModel):
    company_name: str
    service_type : str
    address : str | None = None
