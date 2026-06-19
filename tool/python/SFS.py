"""没有考虑到有人会看源代码"""
import tkinter as tk
from tkinter import filedialog, messagebox
import winreg
from pathlib import Path as P
import shutil
import subprocess
from os.path import basename, splitext, samefile
import sys
def get_resource_path(relative_path):
    base_path = sys._MEIPASS
    return str(P(base_path) / relative_path)
main = tk.Tk()
main.iconbitmap(get_resource_path("ICO.ico"))
main.title("SFS_Chinese_Tool v2.1")
main.geometry("500x150")
main.minsize(500, 150)
main.maxsize(600, 200)
main.iconify()
F835QYDBTM = {"black": {"bg": "#555555","fg": "#ffffff","button_bg": "#004e8d"},"white": {"bg": "#ffffff","fg": "#000000","button_bg": "#004e8d"}}
config = {"path": "","theme": "black"}
def FSC84F9737():
    F9VB7JU4RI = ""
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam")
        path, regtype = winreg.QueryValueEx(key, "InstallPath")
        winreg.CloseKey(key)
        F6TG0P2O44 = P(path) / "steamapps" / "common" / "Spaceflight Simulator F9VB7JU4RI"
        if F6TG0P2O44.exists():
            F9VB7JU4RI = str(F6TG0P2O44)
        else:
            F9VB7JU4RI = ""
            F6TG0P2O44 = filedialog.askdirectory(title="选择游戏根目录（具备自动寻找根目录,如果你选择的不是根目录请耐心等待自动搜索,寻找成功会自动弹出窗口）")
            if F6TG0P2O44:
                folder_path = P(F6TG0P2O44)
                target_file = "Spaceflight Simulator.exe"
                found_files = list(folder_path.rglob(target_file))
                if found_files:
                    for file in found_files:
                        F9VB7JU4RI = str(file.parent)
                else:
                    ask = messagebox.askokcancel("警告", "这个文件夹及子文件夹没有目标目录，会导致工具无法运行,需要重新选择吗?")
                    if ask:
                        F0O0ZOQGC6()
                    else:
                        main.destroy()
                        exit(1)

    except Exception:
        F9VB7JU4RI = ""
        F6TG0P2O44 = filedialog.askdirectory(title="选择游戏根目录（具备自动寻找根目录,如果你选择的不是根目录请耐心等待自动搜索,寻找成功会自动弹出窗口）")
        if F6TG0P2O44:
            folder_path = P(F6TG0P2O44)
            target_file = "Spaceflight Simulator.exe"
            found_files = list(folder_path.rglob(target_file))
            if found_files:
                for file in found_files:
                    F9VB7JU4RI = file.parent
            else:
                ask = messagebox.askokcancel("警告", "这个文件夹及子文件夹没有目标目录，会导致工具无法运行,需要重新选择吗?")
                if ask:
                    F0O0ZOQGC6()
                else:
                    main.destroy()
                    exit(1)


    if F9VB7JU4RI:
        config["path"] = F9VB7JU4RI
        F0O0ZOQGC6()
        config["path"] = ""
        F0O0ZOQGC6()

        main.deiconify()
def F0O0ZOQGC6():
    if not config["path"]:
        try:
            with open("config.txt", "r", encoding="UTF-8") as r:
                for FN8D4IQX80 in r:
                    FN8D4IQX80 = FN8D4IQX80.strip()
                    if ":" in FN8D4IQX80:
                        key, FN6R4LJZ13 = FN8D4IQX80.split(":", 1)
                        if key == "path" and FN6R4LJZ13 and P(FN6R4LJZ13).is_dir():
                            config["path"] = FN6R4LJZ13
                            break
        except FileNotFoundError:
            pass
    with open("config.txt", "w", encoding="UTF-8") as f:
        path_val = config.get("path", "")
        theme_val = config.get("F6IML6CUPA", "")
        f.write(f"path:{path_val}\ntheme:{theme_val}")
    if not config["path"]:
        FSC84F9737()
    else:
        main.deiconify()
F0O0ZOQGC6()
F8YPCOR50T = config["theme"]
F6IML6CUPA = F835QYDBTM[F8YPCOR50T]
def FG83E9IYM0(w=main):
    global F8YPCOR50T, F6IML6CUPA
    try:
        w.config(bg=F6IML6CUPA["bg"])
        for FSEG49G2S7 in w.winfo_children():
            FSEG49G2S7.config(fg=F6IML6CUPA["fg"])
            if isinstance(FSEG49G2S7, tk.Button):
                FSEG49G2S7.config(bg=F6IML6CUPA["button_bg"])
            else:
                FSEG49G2S7.config(bg=F6IML6CUPA["bg"])
    except tk.TclError:
        pass
def FU8G90MA5P(w=main):
    global F8YPCOR50T, F6IML6CUPA
    if F8YPCOR50T == "black":
        F8YPCOR50T = "white"
    else:
        F8YPCOR50T = "black"
    F6IML6CUPA = F835QYDBTM[F8YPCOR50T]
    try:
        w.config(bg=F6IML6CUPA["bg"])
        for FSEG49G2S7 in w.winfo_children():
            FSEG49G2S7.config(fg=F6IML6CUPA["fg"])
            if isinstance(FSEG49G2S7, tk.Button):
                FSEG49G2S7.config(bg=F6IML6CUPA["button_bg"])
            else:
                FSEG49G2S7.config(bg=F6IML6CUPA["bg"])
    except tk.TclError:
        pass
class becameCN():
    def Language_Settings_2_txt(filename="CN"):
        with open(config["path"] + r"/Saving/Settings/LanguageSettings_2.txt", "w", encoding="utf-8") as f:
            f.write("{\n \"codeName\": \""+ filename +"\",\n \"custom\": true\n}")
    def stepMod():
        shutil.copy2(get_resource_path("SFS_HAN_MOD.dll"), config["path"] + r"/Mods/SFS_HAN_MOD.dll")
    def copyCN():
        shutil.copy2(get_resource_path("CN.txt"), config["path"] + r"/Spaceflight Simulator_Data/Custom Translations/CN.txt")
    def copyTTF():
        shutil.copy2(get_resource_path("NotoSansSC.ttf"), config["path"] + r"\Mods\SFS_HAN_MOD\NotoSansSC.ttf")
        messagebox.showinfo("", "添加字体成功")
def useBecameCN():
    try:
        becameCN.Language_Settings_2_txt()
        becameCN.stepMod()
        becameCN.copyCN()
        messagebox.showinfo("汉化成功", "汉化成功,需要重新启动游戏来加载Mod")
    except Exception:
        messagebox.showerror(message=f"汉化失败")
def fixdir():
    fixlist = ["Mods", "Saving", r"Spaceflight Simulator_Data\Custom Translations", r"Saving\Settings"]
    for fixitme in fixlist:
        # 使用 pathlib 的 / 运算符来拼接路径
        itme = P(config["path"]) / fixitme
        itme.mkdir(parents=True, exist_ok=True)
    messagebox.showinfo("提示", "修复成功")
def custom_text_file():
    custom_file = filedialog.askopenfilename(title="选择自定义文件", filetypes=[(".txt", ".txt")])
    if not custom_file:
        return
    custom_file_name = basename(custom_file)
    dst_dir = P(config["path"]) / "Spaceflight Simulator_Data" / "Custom Translations"
    dst_path = str(dst_dir / custom_file_name)
    try:
        if samefile(custom_file, dst_path):
            becameCN.Language_Settings_2_txt(splitext(custom_file_name)[0])
            messagebox.showinfo("", "自定义成功")
            return
    except FileNotFoundError:
        pass
    # 如果不是同一个文件，再执行复制
    shutil.copy2(custom_file, dst_path)
    becameCN.Language_Settings_2_txt(splitext(custom_file_name)[0])
    messagebox.showinfo("", "自定义成功")
def stepmod():
    becameCN.stepMod()
    messagebox.showinfo("", "安装MOD成功")
FG83E9IYM0()
def GUI():
    FAWYS84LZ9 = tk.Button(main, text="切换主题", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=FU8G90MA5P).grid(row=0, column=0, padx=(5, 5), pady=(5, 5))
    useBecameCNButton = tk.Button(main, text="一键汉化", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=useBecameCN).grid(row=0, column=1, padx=(5, 5), pady=(5, 5))
    startgameButton = tk.Button(main, text="启动游戏", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=lambda: subprocess.Popen(config["path"] + r"\Spaceflight Simulator.exe")).grid(row=3, column=0, padx=(5, 5), pady=(5, 5))
    fixdirbutton = tk.Button(main, text="修复目录(如果汉化不成功才使用)", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=fixdir).grid(row=2, column=1, padx=(5, 5), pady=(5, 5))
    addTTF = tk.Button(main, text="如果安装了Mod或者一键汉化后出现了口就使用ta", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=becameCN.copyTTF).grid(row=1, column=0, padx=(5, 5), pady=(5, 5))
    stepmodbutton = tk.Button(main, text="安装字体修复mod", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=stepmod).grid(row=1, column=1, padx=(5, 5), pady=(5, 5))

    custombutton = tk.Button(main, text="点击自定义文本文件(前提是你要有自定义文本文件)", bd=0, relief="flat", bg=F6IML6CUPA["button_bg"], command=custom_text_file).grid(row=2, column=0, padx=(5, 5), pady=(5, 5))
if __name__ == "__main__":
    # 初始化配置
    F0O0ZOQGC6()
    # 创建 GUI
    GUI()
    # 运行主循环
    main.mainloop()

