import pyviewgui
print("pyviewgui imported successfully")
print(f"pyviewgui version: {pyviewgui.__version__}")

# 检查函数是否存在
print(f"create_window function exists: {hasattr(pyviewgui, 'create_window')}")