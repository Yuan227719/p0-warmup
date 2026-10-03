from p0_warmup.csv_combine import combine_operator

def test_wrong_headers(caplog):
    combine_operator(r"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/data",["city", "amount"])
    assert "错误：当前文件表头不一致" in caplog.text

def test_only_headers(caplog):
    combine_operator(r"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/data",["city", "amount"])
    assert "错误：文件为空或只有表头" in caplog.text    

def test_columns_equal(caplog):
    combine_operator(r"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/data",["city", "amount"])
    assert "行数相等" in caplog.text


