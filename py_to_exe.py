import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import sys

class PyToExeConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python转EXE工具")
        self.window.geometry("700x500")
        
        # 创建主容器
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # 文件选择框
        self.file_frame = tk.Frame(main_frame)
        self.file_frame.pack(pady=10, fill=tk.X)
        
        self.file_label = tk.Label(self.file_frame, text="Python文件:", width=10)
        self.file_label.pack(side=tk.LEFT)
        
        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(self.file_frame, textvariable=self.file_path, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=5)
        
        self.browse_button = tk.Button(self.file_frame, text="浏览", width=8, command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        # 输出目录选择框
        self.output_frame = tk.Frame(main_frame)
        self.output_frame.pack(pady=10, fill=tk.X)
        
        self.output_label = tk.Label(self.output_frame, text="输出目录:", width=10)
        self.output_label.pack(side=tk.LEFT)
        
        self.output_path = tk.StringVar()
        self.output_entry = tk.Entry(self.output_frame, textvariable=self.output_path, width=50)
        self.output_entry.pack(side=tk.LEFT, padx=5)
        
        self.output_button = tk.Button(self.output_frame, text="浏览", width=8, command=self.browse_output)
        self.output_button.pack(side=tk.LEFT)
        
        # 选项框
        self.options_frame = tk.LabelFrame(main_frame, text="转换选项", padx=20, pady=10)
        self.options_frame.pack(pady=10, fill=tk.X)
        
        # 使用Grid布局管理器，并配置列权重使其居中
        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_columnconfigure(1, weight=1)
        
        # 基本选项
        self.console_var = tk.BooleanVar(value=True)
        self.console_check = tk.Checkbutton(self.options_frame, text="显示控制台窗口", 
                                          variable=self.console_var)
        self.console_check.grid(row=0, column=0, sticky=tk.W, padx=10)
        
        self.onefile_var = tk.BooleanVar(value=True)
        self.onefile_check = tk.Checkbutton(self.options_frame, text="生成单个文件", 
                                          variable=self.onefile_var)
        self.onefile_check.grid(row=0, column=1, sticky=tk.W, padx=10)
        
        self.admin_var = tk.BooleanVar(value=False)
        self.admin_check = tk.Checkbutton(self.options_frame, text="以管理员身份运行", 
                                        variable=self.admin_var)
        self.admin_check.grid(row=1, column=0, sticky=tk.W, padx=10)
        
        self.clean_var = tk.BooleanVar(value=True)
        self.clean_check = tk.Checkbutton(self.options_frame, text="清理临时文件", 
                                        variable=self.clean_var)
        self.clean_check.grid(row=1, column=1, sticky=tk.W, padx=10)

        # 图标选择框
        self.icon_frame = tk.Frame(main_frame)
        self.icon_frame.pack(pady=10, fill=tk.X)
        
        self.icon_label = tk.Label(self.icon_frame, text="图标文件:", width=10)
        self.icon_label.pack(side=tk.LEFT)
        
        self.icon_path = tk.StringVar()
        self.icon_entry = tk.Entry(self.icon_frame, textvariable=self.icon_path, width=50)
        self.icon_entry.pack(side=tk.LEFT, padx=5)
        
        self.icon_button = tk.Button(self.icon_frame, text="浏览", width=8, command=self.browse_icon)
        self.icon_button.pack(side=tk.LEFT)
        
        # 转换按钮和状态标签的容器
        button_frame = tk.Frame(main_frame)
        button_frame.pack(expand=True, fill=tk.BOTH)
        
        # 转换按钮
        self.convert_button = tk.Button(button_frame, text="开始转换", command=self.convert,
                                      width=20, height=2)
        self.convert_button.pack(pady=20)
        
        # 状态标签
        self.status_label = tk.Label(button_frame, text="")
        self.status_label.pack(pady=10)
        
    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filename:
            self.file_path.set(filename)
    
    def browse_output(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_path.set(directory)
    
    def browse_icon(self):
        filename = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if filename:
            self.icon_path.set(filename)
    
    def convert(self):
        if not self.file_path.get():
            messagebox.showerror("错误", "请选择Python文件！")
            return
            
        try:
            # 构建PyInstaller命令
            cmd = ["pyinstaller"]
            
            # 添加 --add-data 选项来包含 tkinter 数据文件
            tk_path = os.path.join(os.path.dirname(sys.executable), 'tcl', 'tk*')
            tcl_path = os.path.join(os.path.dirname(sys.executable), 'tcl', 'tcl*')
            cmd.extend(['--add-data', f'{tk_path};tk'])
            cmd.extend(['--add-data', f'{tcl_path};tcl'])
            
            # 基本选项
            if self.onefile_var.get():
                cmd.append("--onefile")
            if not self.console_var.get():
                cmd.append("--noconsole")
            if self.clean_var.get():
                cmd.append("--clean")
            if self.admin_var.get():
                cmd.append("--uac-admin")
                
            # 图标
            if self.icon_path.get():
                cmd.extend(["--icon", self.icon_path.get()])
                
            # 输出目录
            if self.output_path.get():
                cmd.extend(["--distpath", self.output_path.get()])
            
            # 源文件
            cmd.append(self.file_path.get())
            
            self.status_label.config(text="正在转换中...（未响应为正常！！）")
            self.window.update()
            
            # 执行转换
            process = subprocess.run(cmd, capture_output=True, text=True)
            
            if process.returncode == 0:
                output_dir = self.output_path.get() if self.output_path.get() else "dist"
                messagebox.showinfo("成功", f"转换完成！\n可执行文件保存在 {output_dir} 文件夹中。")
                self.status_label.config(text="转换成功！")
            else:
                messagebox.showerror("错误", f"转换失败！\n{process.stderr}")
                self.status_label.config(text="转换失败！")
                
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")
            self.status_label.config(text="转换失败！")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PyToExeConverter()
    app.run()
