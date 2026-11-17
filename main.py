# 의류 쇼핑몰 관리 프로그램 (콘솔 메뉴)
# 실행 방법: uv run main.py
import member
import product
import order


# 조회 결과(리스트)를 한 줄씩 출력하는 함수
def print_rows(rows):
    if len(rows) == 0:
        print("데이터가 없습니다.")
        return
    for row in rows:
        print(row)


# 숫자를 입력받는 함수 (숫자가 아니면 다시 입력)
def input_number(message):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        print("숫자만 입력해주세요.")


# ---------------- 회원 메뉴 ----------------
def member_menu():
    while True:
        print("\n===== 회원 관리 =====")
        print("1. 회원 등록")
        print("2. 전체 회원 조회")
        print("3. 회원 정보 수정")
        print("4. 회원 삭제")
        print("0. 뒤로가기")
        choice = input("선택 >> ")

        if choice == "1":
            email = input("이메일: ")
            name = input("이름: ")
            phone = input("전화번호: ")
            address = input("주소: ")
            result = member.create_member(email, name, phone, address)
            print("회원이 등록되었습니다.")
            print_rows(result)

        elif choice == "2":
            print_rows(member.get_all_members())

        elif choice == "3":
            member_id = input_number("수정할 회원 번호: ")
            phone = input("새 전화번호: ")
            address = input("새 주소: ")
            result = member.update_member(member_id, phone, address)
            if result:
                print("회원 정보가 수정되었습니다.")
                print_rows(result)
            else:
                print("해당 회원이 없습니다.")

        elif choice == "4":
            member_id = input_number("삭제할 회원 번호: ")
            result = member.delete_member(member_id)
            if result:
                print("회원이 삭제되었습니다. (해당 회원의 주문도 함께 삭제됩니다)")
            else:
                print("해당 회원이 없습니다.")

        elif choice == "0":
            break
        else:
            print("잘못된 입력입니다.")


# ---------------- 상품 메뉴 ----------------
def product_menu():
    while True:
        print("\n===== 상품 관리 =====")
        print("1. 상품 등록")
        print("2. 전체 상품 조회")
        print("3. 카테고리별 상품 조회")
        print("4. 상품 가격/재고 수정")
        print("5. 상품 삭제")
        print("0. 뒤로가기")
        choice = input("선택 >> ")

        if choice == "1":
            name = input("상품명: ")
            category = input("카테고리(상의/하의/아우터 등): ")
            size = input("사이즈(S/M/L/XL): ")
            color = input("색상: ")
            price = input_number("가격: ")
            stock = input_number("재고: ")
            result = product.create_product(name, category, size, color, price, stock)
            print("상품이 등록되었습니다.")
            print_rows(result)

        elif choice == "2":
            print_rows(product.get_all_products())

        elif choice == "3":
            category = input("카테고리: ")
            print_rows(product.get_products_by_category(category))

        elif choice == "4":
            product_id = input_number("수정할 상품 번호: ")
            price = input_number("새 가격: ")
            stock = input_number("새 재고: ")
            result = product.update_product(product_id, price, stock)
            if result:
                print("상품 정보가 수정되었습니다.")
                print_rows(result)
            else:
                print("해당 상품이 없습니다.")

        elif choice == "5":
            product_id = input_number("삭제할 상품 번호: ")
            result = product.delete_product(product_id)
            if result:
                print("상품이 삭제되었습니다.")
            else:
                print("해당 상품이 없습니다.")

        elif choice == "0":
            break
        else:
            print("잘못된 입력입니다.")


# ---------------- 주문 메뉴 ----------------
def order_menu():
    while True:
        print("\n===== 주문 관리 =====")
        print("1. 주문 등록")
        print("2. 전체 주문 조회")
        print("3. 회원별 주문 조회")
        print("4. 주문 상태 변경")
        print("5. 주문 삭제")
        print("0. 뒤로가기")
        choice = input("선택 >> ")

        if choice == "1":
            member_id = input_number("회원 번호: ")
            product_id = input_number("상품 번호: ")
            quantity = input_number("수량: ")
            result = order.create_order(member_id, product_id, quantity)
            if result:
                print("주문이 완료되었습니다.")
                print_rows(result)

        elif choice == "2":
            print_rows(order.get_all_orders())

        elif choice == "3":
            member_id = input_number("회원 번호: ")
            print_rows(order.get_orders_by_member(member_id))

        elif choice == "4":
            order_id = input_number("주문 번호: ")
            status = input("변경할 상태(주문완료/배송중/배송완료/취소): ")
            result = order.update_order_status(order_id, status)
            if result:
                print("주문 상태가 변경되었습니다.")
                print_rows(result)
            else:
                print("해당 주문이 없습니다.")

        elif choice == "5":
            order_id = input_number("삭제할 주문 번호: ")
            result = order.delete_order(order_id)
            if result:
                print("주문이 삭제되었습니다.")
            else:
                print("해당 주문이 없습니다.")

        elif choice == "0":
            break
        else:
            print("잘못된 입력입니다.")


# ---------------- 메인 메뉴 ----------------
def main():
    while True:
        print("\n======= 의류 쇼핑몰 관리 프로그램 =======")
        print("1. 회원 관리")
        print("2. 상품 관리")
        print("3. 주문 관리")
        print("0. 종료")
        choice = input("선택 >> ")

        try:
            if choice == "1":
                member_menu()
            elif choice == "2":
                product_menu()
            elif choice == "3":
                order_menu()
            elif choice == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")
        except Exception as e:
            # Supabase 연결 오류, 중복 이메일 등 에러가 나면 여기로 온다
            print(f"[에러 발생] {e}")


if __name__ == "__main__":
    main()
