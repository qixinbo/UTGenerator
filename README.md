修改`ut_generator.py`文件中的如下地方，将之改写为适配本地服务。
# 配置大模型服务
## 配置模型服务的秘钥
```py
api_key = "<your-api-key>"
```
## 配置模型服务的地址
```py
base_url = "<your-base-url>"
```
# 配置源文件和测试文件的路径
## 源文件路径
```py
source_dir = "<your-source-dir>"
```
## 测试文件路径
```py
test_dir = "<your-test-dir>"
```

# 运行脚本
```py
python ut_generator.py
```