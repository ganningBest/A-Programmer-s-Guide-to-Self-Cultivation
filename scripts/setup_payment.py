#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
收款码设置助手 - 项目维护者工具
Payment QR Code Setup Helper for Project Maintainers
"""

import os
import shutil
from pathlib import Path

def setup_payment_qr():
    """设置收款码"""
    print("🎯 程序员修心指南 - 收款码设置助手")
    print("=" * 50)
    
    # 项目根目录
    project_root = Path(__file__).parent.parent
    assets_dir = project_root / "assets" / "images"
    
    # 确保目录存在
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 图片目录: {assets_dir}")
    print()
    
    # 支付宝收款码设置
    print("💰 设置支付宝收款码:")
    print("请将您的收款码图片文件操作如下：")
    print("1. 将收款码图片重命名为: alipay-qr.jpg")
    print("2. 将文件放入目录: assets/images/")
    print("3. 最终路径应为: assets/images/alipay-qr.jpg")
    print()

    # 检查是否已经有文件（支持多种格式）
    target_path_jpg = assets_dir / "alipay-qr.jpg"
    target_path_png = assets_dir / "alipay-qr.png"

    if target_path_jpg.exists():
        target_path = target_path_jpg
    elif target_path_png.exists():
        target_path = target_path_png
    else:
        target_path = target_path_jpg  # 默认使用jpg
    if target_path.exists():
        print(f"✅ 发现现有收款码: {target_path}")
        size = target_path.stat().st_size
        print(f"   文件大小: {size / 1024:.1f} KB")
        return

    alipay_path = input("请输入支付宝收款码图片路径 (或直接回车手动设置): ").strip()

    if alipay_path and os.path.exists(alipay_path):
        try:
            shutil.copy2(alipay_path, target_path)
            print(f"✅ 支付宝收款码已设置: {target_path}")
        except Exception as e:
            print(f"❌ 复制失败: {e}")
    elif alipay_path:
        print("❌ 文件不存在，请检查路径")
    else:
        print("📋 请手动将收款码图片重命名为 alipay-qr.jpg 并放入 assets/images/ 目录")
    
    print()
    
    # 微信收款码设置（可选）
    print("💚 设置微信收款码 (可选):")
    print("1. 打开微信APP")
    print("2. 点击右上角'+'")
    print("3. 选择'收付款'")
    print("4. 点击'二维码收款'")
    print("5. 点击'保存收款码'")
    print()
    
    wechat_path = input("请输入微信收款码图片路径 (直接回车跳过): ").strip()
    
    if wechat_path and os.path.exists(wechat_path):
        target_path = assets_dir / "wechat-qr.png"
        try:
            shutil.copy2(wechat_path, target_path)
            print(f"✅ 微信收款码已设置: {target_path}")
            
            # 提示更新README
            print()
            print("📝 如需在README中显示微信收款码，请添加以下代码:")
            print("```markdown")
            print("**微信赞助**")
            print()
            print('<img src="assets/images/wechat-qr.png" alt="微信收款码" width="200">')
            print("```")
            
        except Exception as e:
            print(f"❌ 复制失败: {e}")
    elif wechat_path:
        print("❌ 文件不存在，请检查路径")
    else:
        print("⏭️ 跳过微信收款码设置")
    
    print()
    print("🎉 设置完成！")
    print()
    print("📋 下一步:")
    print("1. 检查图片是否正确显示")
    print("2. 测试二维码是否可以正常扫描")
    print("3. 提交代码到Git仓库")
    print("4. 在GitHub上查看效果")
    print()
    print("💡 提示:")
    print("- 建议图片大小控制在100KB以内")
    print("- 确保二维码清晰可扫描")
    print("- 可以添加简单的文字说明")
    print("- 注意保护个人隐私")

def check_images():
    """检查图片文件"""
    project_root = Path(__file__).parent.parent
    assets_dir = project_root / "assets" / "images"
    
    print("🔍 检查收款码图片:")
    print("=" * 30)
    
    # 检查支付宝（支持多种格式）
    alipay_jpg = assets_dir / "alipay-qr.jpg"
    alipay_png = assets_dir / "alipay-qr.png"

    if alipay_jpg.exists():
        size = alipay_jpg.stat().st_size
        print(f"✅ 支付宝收款码: {alipay_jpg}")
        print(f"   文件大小: {size / 1024:.1f} KB")
    elif alipay_png.exists():
        size = alipay_png.stat().st_size
        print(f"✅ 支付宝收款码: {alipay_png}")
        print(f"   文件大小: {size / 1024:.1f} KB")
    else:
        print("❌ 支付宝收款码: 未设置")
    
    # 检查微信
    wechat_path = assets_dir / "wechat-qr.png"
    if wechat_path.exists():
        size = wechat_path.stat().st_size
        print(f"✅ 微信收款码: {wechat_path}")
        print(f"   文件大小: {size / 1024:.1f} KB")
    else:
        print("⚪ 微信收款码: 未设置 (可选)")

def main():
    """主函数"""
    print("程序员修心指南 - 收款码设置助手")
    print("=" * 40)
    print("💡 提示：推荐使用 add_payment_qr.py 进行快速设置")
    print()
    print("1. 设置收款码")
    print("2. 检查现有图片")
    print("3. 退出")
    print()

    while True:
        choice = input("请选择操作 (1-3): ").strip()

        if choice == "1":
            setup_payment_qr()
            break
        elif choice == "2":
            check_images()
            break
        elif choice == "3":
            print("👋 再见！")
            break
        else:
            print("❌ 无效选择，请重新输入")

if __name__ == "__main__":
    main()
