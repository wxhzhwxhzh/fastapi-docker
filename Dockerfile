FROM dockerpull.cn/library/python:3.11-slim

#设置工作目录

WORKDIR /app

# 安装 FastAPI 和 Uvicorn
RUN pip install fastapi uvicorn  -i  https://pypi.tuna.tsinghua.edu.cn/simple/

# 复制代码
COPY main.py /app/main.py


# 默认启动 uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]






