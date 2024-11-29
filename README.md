# Python to EXE Converter | Python转EXE工具

## Introduction | 简介
这是一个使用PyInstaller将Python脚本转换为可执行文件（.exe）的用户友好型GUI工具。为不想处理命令行操作的用户提供了直观的界面。

This is a user-friendly GUI tool designed to convert Python scripts into executable (.exe) files using PyInstaller. It provides an intuitive interface for users who want to convert their Python programs without dealing with command-line operations.

## Features | 功能特点

### 1. User Interface | 用户界面
- 简洁清晰的图形界面 | Clean and clear graphical interface
- 所有选项一目了然 | All options are visible at a glance
- 实时转换状态显示 | Real-time conversion status display

### 2. File Management | 文件管理
- 支持选择Python源文件(.py) | Support for selecting Python source files (.py)
- 可自定义输出目录 | Customizable output directory
- 支持自定义程序图标(.ico) | Custom program icon support (.ico)

### 3. Conversion Options | 转换选项
- 显示/隐藏控制台窗口 | Show/hide console window
- 生成单文件/文件夹模式 | Single-file/folder generation mode
- 管理员权限运行选项 | Run as administrator option
- 自动清理临时文件 | Automatic cleanup of temporary files

### 4. Advanced Features | 高级特性
- 自动包含tkinter依赖 | Automatic inclusion of tkinter dependencies
- 详细的错误提示 | Detailed error messages
- 转换过程状态反馈 | Conversion process status feedback

## How to Use | 使用方法

1. **选择源文件 | Select Source File**
   - 点击"浏览"选择.py文件 | Click "Browse" to select .py file
   
2. **设置输出目录 | Set Output Directory**
   - 选择生成的exe文件保存位置 | Choose where to save the generated exe file
   
3. **配置选项 | Configure Options**
   - 根据需要设置转换选项 | Set conversion options as needed
   - 可选择是否添加自定义图标 | Optionally add a custom icon

4. **开始转换 | Start Conversion**
   - 点击"开始转换"按钮 | Click "Start Conversion" button
   - 等待转换完成 | Wait for conversion to complete

## Notes | 注意事项

- 转换过程中程序可能会暂时无响应，这是正常现象 | The program may become unresponsive during conversion, which is normal
- 确保系统已安装PyInstaller | Ensure PyInstaller is installed on your system
- 建议在转换前保存所有工作 | Save all work before conversion
- 转换大型项目可能需要较长时间 | Converting large projects may take longer

## Requirements | 系统要求

- Python 3.x
- PyInstaller
- tkinter (通常随Python一起安装 | Usually comes with Python)
- Windows操作系统 | Windows Operating System

## Error Handling | 错误处理

程序会显示详细的错误信息，包括：
The program will display detailed error messages, including:

- 文件选择错误 | File selection errors
- 转换过程错误 | Conversion process errors
- 权限相关问题 | Permission-related issues
- 依赖缺失提示 | Missing dependency notifications
