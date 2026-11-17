# 회원(members) 테이블 CRUD
from db import supabase

TABLE = "members"


# C - 회원 등록
def create_member(email, name, phone, address):
    data = {
        "email": email,
        "name": name,
        "phone": phone,
        "address": address,
    }
    response = supabase.table(TABLE).insert(data).execute()
    return response.data


# R - 전체 회원 조회
def get_all_members():
    response = supabase.table(TABLE).select("*").order("member_id").execute()
    return response.data


# R - 회원 한 명 조회
def get_member(member_id):
    response = supabase.table(TABLE).select("*").eq("member_id", member_id).execute()
    return response.data


# U - 회원 정보 수정 (전화번호, 주소)
def update_member(member_id, phone, address):
    data = {
        "phone": phone,
        "address": address,
    }
    response = supabase.table(TABLE).update(data).eq("member_id", member_id).execute()
    return response.data


# D - 회원 삭제
def delete_member(member_id):
    response = supabase.table(TABLE).delete().eq("member_id", member_id).execute()
    return response.data
