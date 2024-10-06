# FILEPATH: /cloudide/workspace/UT/ut_generator.py
from openai import OpenAI
from dotenv import load_dotenv
import os
# 加载.env文件中的环境变量
load_dotenv()

# 设置 OpenAI API 密钥
# 获取环境变量中的API_KEY，如果是本地环境，请使用自己的API_KEY
api_key = os.getenv("API_KEY")
# 设置大模型服务的地址，如果是本地服务，请使用自己的base_url
base_url = "https://api.siliconflow.cn/v1"

# 指定源文件地址
source_dir = "examples/python_tests/app.py"
# 指定测试文件路径
test_dir = "examples/python_tests/test_app.py"


prompt_dir = "prompt.txt"

client = OpenAI(
    api_key=api_key,  # 从https://cloud.siliconflow.cn/account/ak获取
    base_url=base_url
)

def read_file_contents(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

source_file = read_file_contents(source_dir)
print("Read source file successfully")
test_file = read_file_contents(test_dir)
print("Read test file successfully")
prompt = read_file_contents(prompt_dir)
print("Read prompt successfully")
prompt = prompt.format(source_file=source_file, test_file=test_file)
print("Format prompt successfully")
# 定义系统消息和用户消息
system_message = {"role": "system", "content": "你是一个编程语言的单元测试用例生成专家"}

user_message = {
    "role": "user",
    # "content": "Please generate test cases based on the instructions and source code."
    "content": prompt,
}

# 创建一个包含系统消息和用户消息的消息列表
messages = [system_message, user_message]

print("----- Start to generate test cases ----- ")
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2-Chat",
    messages=messages,
    # response_format={"type": "json_object"}
)

generated_test_cases = response.choices[0].message.content

markdown_string = generated_test_cases

# 使用splitlines()方法将字符串分割成多行
lines = markdown_string.splitlines()

# 去掉首尾两行
stripped_lines = lines[1:-1]

# 将剩余的行拼接回字符串
stripped_markdown = "\n".join(stripped_lines)

print("----- Writing back to the test file -----")
with open(test_dir, "a") as file:
    file.write(stripped_markdown)
