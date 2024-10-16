from openai import OpenAI

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    return response.choices[0].message

client = OpenAI(
    api_key="xxx",
    base_url="https://api.deepseek.com",
)

def get_weather(location):
		return "天气晴朗"


system_prompt="""
你在运行一个“思考”，“工具调用”，“响应”循环。每次只运行一个阶段

1.“思考”阶段：你要仔细思考用户的问题
2.“工具调用阶段”：选择可以调用的工具，并且输出对应工具需要的参数
3.“响应”阶段：根据工具调用返回的结果，回复用户问题。

已有的工具如下：
get_weather：
e.g. get_weather:天津
返回天津的天气情况

Example：
question：天津的天气怎么样？
thought：我应该调用工具查询天津的天气情况
Action：
{
	"function_name":"get_response_time"
	"function_params":{
		"location":"天津"
	}
}
调用Action的结果：“天气晴朗”
Answer:天津的天气晴朗
"""

#1.提问让模型进行思考
question="北京天气怎么样"
messages = [{"role": "system", "content": system_prompt},
    {"role": "user", "content": question}]
message = send_messages(messages)
print(f"Model-1th>\n {message.content}")

# 2.如果找到了json则说明有工具可以调用
# 抽取文本返回中的json
"""
{
        "function_name":"get_weather",
        "function_params":{
                "location":"北京"
        }
}
"""
# 3.调用工具
tianqi = get_weather("北京")

# 4.将调用工具的结果返回给模型进行回答
messages.append({"role": "assistant",  "content": f"调用Action的结果:{tianqi}"})
message = send_messages(messages)
print(f"Model-second>\2 {message.content}")


