# 상품(products) 테이블 CRUD
from db import supabase

TABLE = "products"


# C - 상품 등록
def create_product(name, category, size, color, price, stock):
    data = {
        "name": name,
        "category": category,
        "size": size,
        "color": color,
        "price": price,
        "stock": stock,
    }
    response = supabase.table(TABLE).insert(data).execute()
    return response.data


# R - 전체 상품 조회
def get_all_products():
    response = supabase.table(TABLE).select("*").order("product_id").execute()
    return response.data


# R - 카테고리별 상품 조회
def get_products_by_category(category):
    response = supabase.table(TABLE).select("*").eq("category", category).execute()
    return response.data


# R - 상품 하나 조회
def get_product(product_id):
    response = supabase.table(TABLE).select("*").eq("product_id", product_id).execute()
    return response.data


# U - 상품 가격, 재고 수정
def update_product(product_id, price, stock):
    data = {
        "price": price,
        "stock": stock,
    }
    response = supabase.table(TABLE).update(data).eq("product_id", product_id).execute()
    return response.data


# D - 상품 삭제
def delete_product(product_id):
    response = supabase.table(TABLE).delete().eq("product_id", product_id).execute()
    return response.data
