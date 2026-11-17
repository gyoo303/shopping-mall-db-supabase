-- =========================================
-- 의류 쇼핑몰 테이블 생성 SQL
-- Supabase 대시보드 > SQL Editor 에 붙여넣고 실행하세요.
-- =========================================

-- 혹시 이미 있으면 지우고 다시 만들기 (주문 -> 상품/회원 순서로 삭제)
drop table if exists orders;
drop table if exists products;
drop table if exists members;

-- 1. 회원 테이블
create table members (
    member_id   bigint generated always as identity primary key,  -- PK
    email       varchar(100) not null unique,                     -- 로그인 이메일 (중복 X)
    name        varchar(50)  not null,                            -- 이름
    phone       varchar(20),                                      -- 전화번호
    address     varchar(200),                                     -- 배송 주소
    created_at  timestamptz  default now()                        -- 가입일
);

-- 2. 상품 테이블
create table products (
    product_id  bigint generated always as identity primary key,  -- PK
    name        varchar(100) not null,                            -- 상품명
    category    varchar(30)  not null,                            -- 카테고리 (상의, 하의, 아우터 ...)
    size        varchar(10)  not null,                            -- 사이즈 (S, M, L, XL)
    color       varchar(20),                                      -- 색상
    price       integer      not null check (price >= 0),         -- 가격
    stock       integer      not null default 0 check (stock >= 0), -- 재고 수량
    created_at  timestamptz  default now()                        -- 등록일
);

-- 3. 주문 테이블
create table orders (
    order_id    bigint generated always as identity primary key,  -- PK
    member_id   bigint not null references members(member_id) on delete cascade,   -- FK -> members
    product_id  bigint not null references products(product_id) on delete cascade, -- FK -> products
    quantity    integer not null check (quantity > 0),            -- 주문 수량
    total_price integer not null,                                 -- 총 결제 금액
    status      varchar(20) not null default '주문완료',            -- 주문완료 / 배송중 / 배송완료 / 취소
    ordered_at  timestamptz default now()                         -- 주문일
);

-- =========================================
-- 테스트용 샘플 데이터
-- =========================================
insert into members (email, name, phone, address) values
('hong@example.com', '홍길동', '010-1111-2222', '서울시 강남구'),
('kim@example.com',  '김철수', '010-3333-4444', '부산시 해운대구');

insert into products (name, category, size, color, price, stock) values
('기본 반팔 티셔츠', '상의',   'M', '화이트', 15000, 100),
('와이드 데님 팬츠', '하의',   'L', '블루',   39000, 50),
('오버핏 후드 집업', '아우터', 'XL', '그레이', 59000, 30);

insert into orders (member_id, product_id, quantity, total_price) values
(1, 1, 2, 30000),
(2, 3, 1, 59000);

-- =========================================
-- (참고) 실습용이라 RLS(Row Level Security)를 끕니다.
-- 실제 서비스에서는 RLS 정책을 꼭 설정해야 합니다!
-- =========================================
alter table members  disable row level security;
alter table products disable row level security;
alter table orders   disable row level security;
