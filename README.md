# pyviewgui 项目详细文档

## 项目概述

pyviewgui 是一个使用 Rust 编写的 Python 库，用于创建基于 Web 技术的桌面应用程序。它利用 Rust 的高性能和安全性，结合 Web 技术的灵活性，为开发者提供一个简单易用的完全开源免费的桌面 GUI 开发方案。

### 核心特性

- 使用 Rust 编写，性能优异且内存安全
- 通过 WebView 技术在桌面应用中嵌入 Web 内容
- 支持加载本地 HTML 文件或远程 URL
- 可自定义窗口标题、尺寸、装饰等属性
- 支持自定义窗口图标
- 可选择是否启用开发者工具

## 技术架构

### 技术栈

- **Rust**: 核心逻辑和性能关键部分
- **Python**: 提供高级接口
- **PyO3**: Rust 和 Python 之间的绑定
- **tao**: 跨平台窗口管理
- **wry**: WebView 渲染引擎
- **image**: 图标处理

### 项目结构

```
pyviewgui/
├── src/                    # Rust 源代码
│   └── lib.rs             # 核心实现
├── pyviewgui/             # Python 包
│   └── __init__.py        # Python 接口
├── static/                # 静态资源
├── test/                  # 测试文件
├── Cargo.toml             # Rust 依赖管理
├── pyproject.toml         # Python 依赖管理
└── README.md
```

## 安装与配置

### 环境要求

- Python 3.11 或更高版本（同时支持3.13.0及以上 free-threading 版本 Python）

### 安装方法

```bash
pip install pyviewgui
```

或从源码安装：

```bash
git clone https://github.com/xzp-hub/pyviewgui.git
cd pyviewgui
pip install .
```

## API 参考

### 主要函数

#### `create_window`

创建并显示一个桌面窗口。

**函数签名:**
```python
def create_window(
    win_title: str = "pyviewgui app",
    win_width: int = 1200,
    win_height: int = 800,
    win_content: str = None,
    win_icon_path: str = None,
    win_is_decorations: bool = True,
    win_is_resizable: bool = True,
    win_is_devtools: bool = True
)
```

**参数说明:**

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| win_title | str | "pyviewgui app" | 窗口标题 |
| win_width | int | 1200 | 窗口宽度（像素） |
| win_height | int | 800 | 窗口高度（像素） |
| win_content | str | None | 窗口内容（HTML文件路径或URL） |
| win_icon_path | str | None | 图标文件路径 |
| win_is_decorations | bool | True | 是否显示窗口装饰（边框、标题栏等） |
| win_is_resizable | bool | True | 窗口是否可调整大小 |
| win_is_devtools | bool | True | 是否启用开发者工具 |

**功能说明:**

- 当 `win_content` 为 `None` 时，加载内置的默认 HTML 页面
- 当 `win_icon_path` 为 `None` 时，使用内置的默认图标
- 支持加载本地 HTML 文件或远程 URL

### 使用示例

#### 基本用法

```python
import pyviewgui

# 创建一个简单的窗口，默认加载内置的 HTML
pyviewgui.create_window()
```

#### 自定义窗口

```python
import pyviewgui

# 创建自定义窗口
pyviewgui.create_window(
    win_title="我的应用",
    win_width=1200,
    win_height=800,
    win_decorations=True,
    win_resizable=True,
    win_devtools=False
)
```

#### 加载自定义内容

```python
import pyviewgui

# 加载自定义 HTML 文件
pyviewgui.create_window(
    win_title="自定义应用",
    win_width=1000,
    win_height=700,
    win_content="path/to/your/file.html",
    win_icon_path="path/to/your/icon.png"
)
```

## 内部实现

### Rust 实现 (src/lib.rs)

Rust 部分负责底层的窗口管理和 WebView 渲染：

- **窗口管理**: 使用 tao 库创建和管理窗口
- **WebView 渲染**: 使用 wry 库嵌入 Web 内容
- **图标处理**: 使用 image 库加载和处理图标
- **跨平台支持**: 包含 Windows 特定的 App User Model ID 设置

#### 核心函数

- `py_create_window`: Python 函数的 Rust 实现
- `create_window`: 创建和运行窗口事件循环
- `load_icon_from_path`: 从路径加载图标

### Python 实现 (pyviewgui/__init__.py)

Python 部分提供高级接口：

- **参数处理**: 处理默认值和路径
- **接口封装**: 封装 Rust 函数为 Python 函数
- **模块导出**: 导出公共 API

## 构建与开发

### 构建依赖

- `maturin`: 用于构建 Python 扩展
- `cargo`: Rust 包管理器（rust版本1.92.0及以上））

### 构建命令

```bash
# 开发模式安装
maturin develop

# 构建发布版本
maturin build --release（如若需要3.15 free-threading Python版本，请自行在3.15 free-threading Python版本下构建）

# 构建 Python 包
maturin build
```

### 开发流程

1. 修改 Rust 代码
2. 运行 `maturin develop` 重新编译
3. 测试 Python 接口

## 测试

### 测试文件

- `test/test.py`: 基本功能测试
- `test/check_gil_status.py`: GIL 状态检查

### 运行测试

```bash
python test/test.py
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request 来改进项目。

## 作者

- **作者**: xzp
- **邮箱**: x-z-p@foxmail.com