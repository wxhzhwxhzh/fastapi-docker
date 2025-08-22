# FastAPI 静态文件服务 Docker 部署指南

本文档介绍如何使用 Docker 部署一个提供静态文件服务的 FastAPI 应用。

## 前提条件

- 已安装 Docker 环境
- 基本的 Docker 命令操作知识
- 项目目录下存在有效的 Dockerfile

## 构建 Docker 镜像

使用以下命令构建 Docker 镜像：

```bash
sudo docker build -t fastapi-static .
```

- `docker build`：Docker 构建镜像的命令
- `-t fastapi-static`：为镜像指定标签（名称）为 `fastapi-static`
- `.`：指定 Dockerfile 所在的当前目录

## 查看运行中的容器

构建完成后，可以使用以下命令查看当前运行的容器：

```bash
sudo docker ps
```

该命令会显示所有正在运行的容器信息，包括容器ID、名称、使用的镜像、端口映射等。

## 运行容器

使用以下命令启动一个基于构建好的镜像的容器：

```bash
sudo docker run -d --name fa33  -v $(pwd)/html:/app/web -e INDEX_DIR=/app/web -p 8099:80 fastapi-static
```

参数说明：
- `-d`：后台运行容器
- `--name fa33`：指定容器名称为 `fa33`
- `-v $(pwd)/html:/app/web`：将宿主机当前目录下的 `html` 文件夹挂载到容器内的 `/app/web` 目录
- `-e INDEX_DIR=/app/web`：设置环境变量 `INDEX_DIR`，值为 `/app/web`
- `-p 8099:80`：端口映射，将宿主机的 8099 端口映射到容器的 80 端口
- `fastapi-static`：使用的镜像名称

## 访问服务

容器启动后，可以通过以下地址访问服务：
```
http://localhost:8099
```

## 其他常用命令

### 停止容器
```bash
sudo docker stop fa33
```

### 启动已停止的容器
```bash
sudo docker start fa33
```

### 删除容器
```bash
sudo docker rm fa33
```

### 查看容器日志
```bash
sudo docker logs fa33
```

### 进入容器内部
```bash
sudo docker exec -it fa33 /bin/bash
```