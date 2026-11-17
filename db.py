# Supabase 연결을 담당하는 파일
import os

from dotenv import load_dotenv
from supabase import create_client

# .env 파일에 적어둔 값들을 불러온다
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("[오류] .env 파일에 SUPABASE_URL, SUPABASE_KEY 를 먼저 적어주세요!")
    exit()

# 다른 파일에서 from db import supabase 로 가져다 쓴다
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
