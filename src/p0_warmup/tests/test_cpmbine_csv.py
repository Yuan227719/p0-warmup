from p0_warmup.csv_combine import combine_operator
from pathlib import Path

# 锚点：从本文件出发往上走 4 级到仓库根，再进 data/
# __file__ = .../src/p0_warmup/tests/test_cpmbine_csv.py
DATA_DIR = Path(__file__).resolve().parents[3] / "data"
OUT_CSV  = DATA_DIR.parent / "combined_data" / "out.csv"

def test_wrong_headers(caplog):
    combine_operator(str(DATA_DIR),["city", "amount"])
    assert "错误：当前文件表头不一致" in caplog.text

def test_only_headers(caplog):
    combine_operator(str(DATA_DIR),["city", "amount"])
    assert "错误：文件为空或只有表头" in caplog.text    

def test_columns_equal(caplog):
    combine_operator(str(DATA_DIR),["city", "amount"])
    assert "行数相等" in caplog.text


