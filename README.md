Function的调用时Agent实现很重要的一步，只有了解了这个原理才可以更好的创建Agent。

此代码从零构建了Agent中最重要的function call。

# 场景

Agent的目标：可以回答用户关于天气的问题。

流程：

1. 思考： 用户输入问题，先进行分析

2. 行动： 如果问到了天气问题，则分析出需要调用的function以及function要传入的参数

3. 响应：function返回后，将答案整理好回复给用户。

# 流程如下

![image](https://github.com/user-attachments/assets/5a8c510c-fd35-46c2-956c-95ad1fc4f98e)

# 运行逻辑

1. 提问让模型进行思考
```
    question="北京天气怎么样"
    messages = [{"role": "system", "content": system_prompt},
        {"role": "user", "content": question}]
    message = send_messages(messages)
    print(f"Model-1th>\n {message.content}")
```

2. 如果找到了json则说明有工具可以调用
```
   抽取文本返回中的json
  """
  {
          "function_name":"get_weather",
          "function_params":{
                  "location":"北京"
          }
  }
  """
```
  
3. 调用工具
```
  tianqi = get_weather("北京")
```

4.将调用工具的结果返回给模型进行回答
```
  messages.append({"role": "assistant",  "content": f"调用Action的结果:{tianqi}"})
  message = send_messages(messages)
  print(f"Model-second>\2 {message.content}")
```

# 运行结果
```
  Model-1th>
   thought：我应该调用工具查询北京的天气情况
  Action：
  {
          "function_name":"get_weather",
          "function_params":{
                  "location":"北京"
          }
  }

  Model-second> 北京今天的天气晴朗。
```
