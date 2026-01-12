# pyviewgui

pyviewgui 是一个使用 Rust 编写的 Python 库，用于创建基于 Web 技术的桌面应用程序。它利用 Rust 的高性能和安全性，结合 Web 技术的灵活性，为开发者提供一个简单易用的桌面 GUI 开发方案。

## 功能特性

- 使用 Rust 编写，性能优异且内存安全
- 通过 WebView 技术在桌面应用中嵌入 Web 内容
- 支持加载本地 HTML 文件或远程 URL
- 可自定义窗口标题、尺寸、装饰等属性
- 支持自定义窗口图标
- 可选择是否启用开发者工具

## 安装

```bash
pip install pyviewgui
```

## 使用方法

### 基本用法

```python
import pyviewgui

# 创建一个简单的窗口，默认加载内置的 HTML
pyviewgui.create_window()
```

### 自定义窗口

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

### 加载自定义内容

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

## API 参考

### `create_window()`

创建并显示一个桌面窗口。

#### 参数

- `win_title` (str): 窗口标题，默认为 "pyviewgui app"
- `win_width` (int): 窗口宽度，默认为 1200 像素
- `win_height` (int): 窗口高度，默认为 800 像素
- `win_content` (str): 窗口内容，可以是本地 HTML 文件路径或 URL，默认使用内置 HTML
- `win_icon_path` (str): 窗口图标路径，默认使用内置图标
- `win_decorations` (bool): 是否显示窗口装饰（边框、标题栏等），默认为 True
- `win_resizable` (bool): 窗口是否可调整大小，默认为 True
- `win_devtools` (bool): 是否启用开发者工具，默认为 True

## 技术栈

- **Rust**: 核心逻辑和性能关键部分
- **PyO3**: Rust 与 Python 之间的绑定
- **tao**: 跨平台窗口管理
- **wry**: WebView 渲染引擎
- **maturin**: 构建和发布 Python 包

## 开发

### 构建

```bash
# 构建 Python 包
maturin build

# 构建发布版本
maturin build --release
```

### 安装开发版本

```bash
# 安装开发版本
maturin develop

# 或者直接安装
pip install -e .
```

## 许可证

MIT License