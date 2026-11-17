# 주문(orders) 테이블 CRUD
from db import supabase
from product import get_product, update_product

TABLE = "orders"


# C - 주문 등록
def create_order(member_id, product_id, quantity):
    # 1. 주문할 상품이 있는지 확인
    products = get_product(product_id)
    if len(products) == 0:
        print("존재하지 않는 상품입니다.")
        return []

    product = products[0]

    # 2. 재고가 충분한지 확인
    if product["stock"] < quantity:
        print(f"재고가 부족합니다. (현재 재고: {product['stock']}개)")
        return []

    # 3. 주문 저장 (총 금액 = 가격 x 수량)
    data = {
        "member_id": member_id,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product["price"] * quantity,
    }
    response = supabase.table(TABLE).insert(data).execute()

    # 4. 주문한 만큼 재고 줄이기
    update_product(product_id, product["price"], product["stock"] - quantity)

    return response.data


# R - 전체 주문 조회 (회원 이름, 상품 이름도 같이 가져오기)
#     orders 테이블의 FK(member_id, product_id) 덕분에 join 처럼 가져올 수 있다
def get_all_orders():
    response = (
        supabase.table(TABLE)
        .select("*, members(name), products(name)")
        .order("order_id")
        .execute()
    )
    return response.data


# R - 특정 회원의 주문 조회
def get_orders_by_member(member_id):
    response = (
        supabase.table(TABLE)
        .select("*, products(name)")
        .eq("member_id", member_id)
        .execute()
    )
    return response.data


# U - 주문 상태 변경 (주문완료 -> 배송중 -> 배송완료 / 취소)
def update_order_status(order_id, status):
    response = (
        supabase.table(TABLE)
        .update({"status": status})
        .eq("order_id", order_id)
        .execute()
    )
    return response.data


# D - 주문 삭제
def delete_order(order_id):
    response = supabase.table(TABLE).delete().eq("order_id", order_id).execute()
    return response.data
