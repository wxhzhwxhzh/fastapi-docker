我可以帮您创建一个包含Chrome浏览器的Docker镜像，并以无头模式运行，开放9222调试端口。现在我再为您创建一个docker-compose.yml文件和构建脚本，方便您使用：## 使用说明

1. **保存文件**：将上述三个文件保存到同一个目录中：
   - `Dockerfile`
   - `docker-compose.yml` 
   - `build.sh`（构建脚本）

2. **设置权限**：
   ```bash
   chmod +x build.sh
   ```

3. **构建并运行**：
   ```bash
   ./build.sh
   ```

4. **验证运行**：
   - 访问 `http://localhost:9222` 查看Chrome调试界面
   - 访问 `http://localhost:9222/json` 查看可用的调试会话列表

## 主要特性

- **无头模式**：Chrome以无头模式运行，不需要图形界面
- **远程调试**：开放9222端口用于远程调试
- **安全运行**：使用非root用户运行Chrome
- **数据持久化**：Chrome用户数据通过Docker卷持久化
- **资源优化**：配置了适当的共享内存大小

## 常用操作命令

```bash
# 查看容器状态
docker-compose ps

# 查看容器日志
docker logs chrome-headless

# 停止容器
docker-compose down

# 重启容器
docker-compose restart

# 进入容器
docker exec -it chrome-headless /bin/bash
```

## 连接调试

您可以使用各种工具连接到Chrome调试端口：
- Chrome DevTools
- Puppeteer
- Selenium
- 或任何支持Chrome DevTools Protocol的工具

连接地址：`ws://localhost:9222/devtools/browser`

这个配置提供了一个完整的、生产就绪的Chrome无头模式Docker环境！