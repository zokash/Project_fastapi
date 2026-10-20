

from fastapi import Depends, FastAPI, HTTPException, status

from auth import verify_key
from db import get_conn
from models import CompanyTemplate, ContactTemplate

app = FastAPI(dependencies  = [Depends(verify_key)])

@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM contacts WHERE contact_id = %s", (contact_id,)).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail = f"Contact {contact_id} not found")
    
    return row

@app.get("/contacts")
def all_contacts(company_id: int | None = None, limit:int | None=None):
    query = "SELECT * FROM contacts"
    params = []

    if company_id is not None:
       query+= " WHERE company_id = %s"
       params.append(company_id)

    query+=" ORDER BY contact_id"
    

    if limit is not None:
        query+=" LIMIT %s"
        params.append(limit)

    with get_conn() as conn:
        res = conn.execute(query, params).fetchall()

    return res       

@app.post("/contacts", status_code=status.HTTP_201_CREATED)
def create_contact(item: ContactTemplate):
    
    params = []
    res = item.model_dump()
    params.append(res["company_id"])
    params.append(res["poc_name"])
    params.append(res["phone"])
    params.append(res["email"])   
    params.append(res["designation"])

    query = 'INSERT INTO contacts ("company_id", "poc_name", "phone","email", "designation") VALUES (%s, %s, %s, %s, %s) RETURNING *'
    

    with get_conn() as conn:
        ans = conn.execute(query, params).fetchone()
        
    return ans

@app.delete("/contacts/{contact_id}",status_code=204)
def delete_contact(contact_id:int ):
    with get_conn() as conn:
        ans = conn.execute("DELETE FROM contacts WHERE contact_id = %s RETURNING *", (contact_id,)).fetchone()
        if ans is None:
            raise HTTPException(status_code=404, detail=f"Contact id {contact_id} not found")
    return None#not to return ans since 204 has no body


@app.put("/contacts/{contact_id}")
def replace_contact(contact_id:int, item: ContactTemplate):
    
    params = []
    res = item.model_dump()
    params.append(res["company_id"])
    params.append(res["poc_name"])
    params.append(res["phone"])
    params.append(res["email"])   
    params.append(res["designation"])
    params.append(contact_id)

    query = """UPDATE contacts 
    SET 
    company_id = %s, 
    poc_name = %s,
    phone = %s, 
    email = %s, 
    designation = %s 
    WHERE contact_id = %s RETURNING *"""
    

    with get_conn() as conn:
        ans = conn.execute(query, params).fetchone()
    if ans is None:
        raise HTTPException(status_code=404, detail=f"Contact ID {contact_id} not found")    
    return ans


@app.get("/companies/{company_id}")
def get_company(company_id: int):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM companies WHERE company_id = %s", (company_id,)).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail = f"Company {company_id} not found")
    
    return row

@app.get("/companies")
def all_companies( limit:int | None=None):
    query = "SELECT * FROM companies ORDER BY company_id"
    params = []

    if limit is not None:
        query+=" LIMIT %s"
        params.append(limit)
    
    with get_conn() as conn:
        res = conn.execute(query, params).fetchall()

    return res       


@app.post("/companies", status_code=status.HTTP_201_CREATED)
def create_company(item: CompanyTemplate):
    
    params = []
    res = item.model_dump()
    params.append(res["company_name"])
    params.append(res["service_type"])
    params.append(res["address"])
  

    query = 'INSERT INTO companies ("company_name", "service_type", "address") VALUES (%s, %s, %s) RETURNING *'
    

    with get_conn() as conn:
        ans = conn.execute(query, params).fetchone()
        
    return ans