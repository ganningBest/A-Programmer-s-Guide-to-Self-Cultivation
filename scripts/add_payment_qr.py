#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速添加收款码到README
Quick Payment QR Code Setup
"""

import os
import shutil
from pathlib import Path

def setup_payment_qr():
    """设置收款码并更新README"""
    print("🎯 收款码快速设置工具")
    print("=" * 30)
    
    # 项目根目录
    project_root = Path(__file__).parent.parent
    assets_dir = project_root / "assets" / "images"
    readme_path = project_root / "README.md"
    
    # 确保目录存在
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 图片目录: {assets_dir}")
    print()
    
    # 获取收款码图片路径
    qr_path = input("请输入您的支付宝收款码图片路径: ").strip().strip('"')
    
    if not qr_path or not os.path.exists(qr_path):
        print("❌ 文件不存在或路径无效")
        return
    
    # 复制文件
    target_path = assets_dir / "alipay-qr.jpg"
    try:
        shutil.copy2(qr_path, target_path)
        print(f"✅ 收款码已复制到: {target_path}")
    except Exception as e:
        print(f"❌ 复制失败: {e}")
        return
    
    # 更新README
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换占位符
        old_text = '''```
┌─────────────────────┐
│                     │
│    📱 收款码位置      │
│                     │
│  请添加您的支付宝    │
│  收款码图片到此处    │
│                     │
│ assets/images/      │
│ alipay-qr.jpg       │
│                     │
└─────────────────────┘
```'''
        
        new_text = '''<div align="center">

![支付宝收款码](assets/images/alipay-qr.jpg)

</div>'''
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ README.md 已更新")
        else:
            print("⚠️ 未找到占位符，请手动更新README.md")
            print("请将以下代码添加到README.md的收款码位置：")
            print("![支付宝收款码](assets/images/alipay-qr.jpg)")
    
    except Exception as e:
        print(f"❌ 更新README失败: {e}")
    
    print()
    print("🎉 设置完成！")
    print("📋 下一步：")
    print("1. 检查README.md中的收款码显示")
    print("2. 提交代码到Git仓库")
    print("3. 在GitHub上查看效果")

if __name__ == "__main__":
    setup_payment_qr()
