import subprocess

# 获取支持的硬件加速方法
def get_supported_hwaccels():
    try:
        result = subprocess.run(
            ['ffmpeg', '-hwaccels'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode == 0:
            hwaccels = result.stdout.splitlines()
            hwaccels = [hw.strip() for hw in hwaccels if hw.strip()]
            if hwaccels and "Hardware acceleration methods:" in hwaccels[0]:
                hwaccels.pop(0)  # 移除无用的开头文本
            return hwaccels
        else:
            print("\n[错误] 无法获取硬件加速方法:")
            print(result.stderr)
            return []
    except Exception as e:
        print(f"\n[异常] 获取硬件加速时出错: {e}")
        return []

# 检测硬件加速是否可用
def check_hwaccels():
    supported_hwaccels = get_supported_hwaccels()
    
    if not supported_hwaccels:
        print("\n[信息] 没有检测到可用的硬件加速方法。\n")
        return

    print("\n=== 硬件加速检测开始 ===\n")

    available_hwaccels = []  # 可用的硬件加速方法
    unavailable_hwaccels = []  # 不可用的硬件加速方法

    for hwaccel in supported_hwaccels:
        print(f"-> 测试硬件加速: {hwaccel} ...", end=" ")

        try:
            result = subprocess.run(
                ['ffmpeg', '-hwaccel', hwaccel, '-i', 'test_video.mp4', '-f', 'null', '-'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode == 0:
                print("\033[92m[成功]\033[0m 硬件加速可用")  # 绿色文本
                available_hwaccels.append(hwaccel)
            else:
                print("\033[91m[失败]\033[0m 硬件加速不可用")  # 红色文本
                unavailable_hwaccels.append(hwaccel)
                print(f"   [错误详情]: {result.stderr.splitlines()[-5:]}")  # 显示最后5行错误信息

        except Exception as e:
            print("\033[91m[异常]\033[0m 运行测试时发生错误")
            unavailable_hwaccels.append(hwaccel)
            print(f"   [异常详情]: {e}")

    print("\n=== 硬件加速检测完成 ===\n")

    # 输出总结
    print("🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵硬件加速支持情况总结🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵")
    print("\n\n") 
    print(f"✅ 可用的硬件加速方法 ({len(available_hwaccels)}):")
    if available_hwaccels:
        print("   " + ", ".join(available_hwaccels))
    else:
        print("   无")

    print(f"\n❌ 不可用的硬件加速方法 ({len(unavailable_hwaccels)}):")
    if unavailable_hwaccels:
        print("   " + ", ".join(unavailable_hwaccels))
    else:
        print("   无")

    print("\n==============================\n")

# 运行检测
check_hwaccels()
input("按 Enter 键退出...")
